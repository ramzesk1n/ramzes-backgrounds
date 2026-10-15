"""Unpack the versioned local library once; no network or third-party packages."""
import hashlib
import json
import os
import shutil
import tarfile
import tempfile
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]


def library_root():
    manifest = json.loads((ROOT / 'library.json').read_text(encoding='utf-8'))
    archive_name = manifest['archive']
    if Path(archive_name).name != archive_name:
        raise ValueError('Invalid archive name')
    expected = manifest['sha256']
    archive = ROOT / archive_name
    digest = hashlib.sha256()
    with archive.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(block)
    if digest.hexdigest() != expected:
        raise ValueError('Library archive checksum mismatch; restore it from GitHub')

    cache = ROOT / '.runtime'
    destination = cache / expected
    ready = destination / '.ready'
    if ready.is_file() and ready.read_text(encoding='utf-8') == expected:
        return destination
    if destination.exists():
        raise ValueError('Incomplete runtime directory; inspect it before retrying')
    cache.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='unpack-', dir=cache) as temporary:
        staging = Path(temporary) / 'library'
        staging.mkdir()
        count = 0
        with tarfile.open(archive, 'r:xz') as package:
            for member in package:
                path = PurePosixPath(member.name)
                if path.is_absolute() or '..' in path.parts:
                    raise ValueError('Unsafe archive path')
                target = staging.joinpath(*path.parts)
                if member.isdir():
                    target.mkdir(parents=True, exist_ok=True)
                elif member.isfile():
                    target.parent.mkdir(parents=True, exist_ok=True)
                    with package.extractfile(member) as source, target.open('wb') as output:
                        shutil.copyfileobj(source, output)
                    count += 1
                else:
                    raise ValueError('Unsupported archive entry')
        if count != manifest['source_files']:
            raise ValueError('Unexpected library file count')
        data = json.loads((staging / 'catalog.json').read_text(encoding='utf-8'))
        if data['version'] != manifest['version'] or len(data['cards']) != manifest['cards']:
            raise ValueError('Library metadata mismatch')
        (staging / '.ready').write_text(expected, encoding='utf-8')
        try:
            os.rename(staging, destination)
        except FileExistsError:
            if not ready.is_file() or ready.read_text(encoding='utf-8') != expected:
                raise
    return destination

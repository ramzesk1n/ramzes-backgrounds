#!/usr/bin/env python3
"""Build the standalone offline catalog from the bundled existing assets."""
import runpy
import shutil
from _library import ROOT, library_root

library = library_root()
runpy.run_path(str(library / 'scripts' / 'build_gallery.py'), run_name='__main__')
shutil.copyfile(library / 'index.html', ROOT / 'index.html')
print(f'Open the offline catalog: {ROOT / "index.html"}')

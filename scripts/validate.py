#!/usr/bin/env python3
"""Validate the bundled library using its existing release checks."""
import runpy
from _library import library_root

library = library_root()
runpy.run_path(str(library / 'scripts' / 'build_gallery.py'), run_name='__main__')
runpy.run_path(str(library / 'scripts' / 'validate.py'), run_name='__main__')

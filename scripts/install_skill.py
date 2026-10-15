#!/usr/bin/env python3
"""Install the bundled skill for Claude Code or Codex."""
import runpy
import sys
from _library import library_root

script = library_root() / 'scripts' / 'install_skill.py'
sys.path.insert(0, str(script.parent))
sys.argv[0] = str(script)
runpy.run_path(str(script), run_name='__main__')

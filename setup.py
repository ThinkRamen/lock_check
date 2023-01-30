import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'includes': ['resources', 'lock_check', 'lock_check_old', 'audit'], 'include_files': ['required/'],
                 'zip_include_packages': ['encodings', 'pyside6'], }
executables = [
    Executable('gui.py')
]

setup(name='lockcheck',
      version='2.0',
      description='',
      options={'build_exe': build_options},
      executables=executables)

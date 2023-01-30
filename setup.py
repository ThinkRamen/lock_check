import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'includes': ['resources', 'lock_check', 'lock_check_old', 'audit'], 'include_files': ['required/'],
                 'zip_include_packages': ['encodings', 'pyside6'], }
mac_options = {}
executables = [
    Executable('gui.py', icon='./lock.icns')
]

setup(name='lockcheck',
      version='2.0',
      description='',
      options={'build_exe': build_options, 'bdist_mac': mac_options},
      executables=executables)

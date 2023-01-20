from setuptools import setup

APP = ['gui.py']
DATA_FILES = []
OPTIONS = {
    'iconfile': 'lock.icns',
}

setup(
    name='lock_check',
    app=APP,
    py_modules=['audit.py', 'lock_check.py'],
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

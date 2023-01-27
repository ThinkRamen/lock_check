source .venv/bin/activate
pyinstaller --windowed gui.py -F \
--name 'lock_check' \
--icon='./lock.icns' \
--add-binary='/System/Library/Frameworks/Tk.framework/Tk:tk' \
--add-binary='/System/Library/Frameworks/Tcl.framework/Tcl:tcl;' \
--add-binary='/Users/admin/Documents/GitHub/lock_check/required/Firefox.app/Contents/MacOS/firefox-bin:.' \
--add-binary='/Users/admin/Documents/GitHub/lock_check/required/geckodriver:.' \
--add-data './scripts/*.sh:./scripts' \
--clean

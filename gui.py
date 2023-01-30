import sys
import os
from PySide6.QtWidgets import (QComboBox, QPushButton, QApplication,
                               QVBoxLayout, QWidget, QLabel)
from lock_check import lock_check_json, to_txt_file
from audit import audit_json
from lock_check_old import firefox_automation


class Main_Widget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # Create widgets
        self.label = QLabel('select option:')
        self.button = QPushButton('select')
        self.dropdown = QComboBox()
        self.dropdown.addItems(
            ['lock check', 'lock check + audit', 'lock check + audit (old)'])

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.dropdown)
        layout.addWidget(self.button)
        self.setLayout(layout)

        self.button.clicked.connect(self.select_option)

    def select_option(self):
        if self.dropdown.currentText() == 'lock check':
            print(os.getcwd(), lock_check_json())
            to_txt_file(lock_check_json())
        if self.dropdown.currentText() == 'lock check + audit':
            print(lock_check_json() + audit_json())
            to_txt_file(lock_check_json() + audit_json())
        if self.dropdown.currentText() == 'lock check + audit (old)':
            firefox_automation(to_txt_file(lock_check_json() + audit_json()))


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    app.setStyle('macos')
    # Create and show the form
    widget = Main_Widget()
    widget.setWindowTitle('Lock Check')
    widget.show()
    # Run the main Qt loop
    sys.exit(app.exec())

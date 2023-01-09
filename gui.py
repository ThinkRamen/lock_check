import sys
from PySide6.QtWidgets import (QComboBox, QPushButton, QApplication,
                               QVBoxLayout, QWidget, QLabel)
from lock_check import lock_check_json
from audit import audit_json


class Main_Widget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # Create widgets
        self.label = QLabel('select option:')
        self.button = QPushButton('select')
        self.dropdown = QComboBox()
        self.dropdown.addItems(['lock check', 'lock check + audit'])

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.dropdown)
        layout.addWidget(self.button)
        self.setLayout(layout)

        self.button.clicked.connect(self.select_option)

    def select_option(self):
        if self.dropdown.currentText() == 'lock check':
            print(lock_check_json())
        if self.dropdown.currentText() == 'lock check + audit':
            print(audit_json())


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

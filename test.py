

# Main Code
import sys
import os

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QAction
from PyQt5.QtGui import QIcon

class DatabaseWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Database Management System'
        self.left = 0
        self.top = 0
        self.width = 500
        self.height = 500
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create Main Window
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.main_layout = QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)

        # Create Database Buckets
        self.bucket_label = QLabel('Buckets')
        self.bucket_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.bucket_label)

        self.bucket_layout = QHBoxLayout()
        self.main_layout.addLayout(self.bucket_layout)

        self.data_label = QLabel('Data')
        self.data_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.data_label)

        self.data_layout = QHBoxLayout()
        self.main_layout.addLayout(self.data_layout)

        # Create Login Button
        self.login_button = QPushButton('Login')
        self.login_button.clicked.connect(self.on_login_button_clicked)
        self.main_layout.addWidget(self.login_button)

        self.show()

    # Create Login Method
    def on_login_button_clicked(self):
        self.close()
        self.login_window = LoginWindow()

class LoginWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Login'
        self.left = 0
        self.top = 0
        self.width = 500
        self.height = 500
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create Main Window
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.main_layout = QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)

        # Create Login Button
        self.login_button = QPushButton('Login')
        self.login_button.clicked.connect(self.on_login_button_clicked)
        self.main_layout.addWidget(self.login_button)

        self.show()

    # Create Login Method
    def on_login_button_clicked(self):
        self.close()
        self.database_window = DatabaseWindow()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    database_window = DatabaseWindow()
    sys.exit(app.exec_())
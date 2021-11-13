# This Python file uses the following encoding: utf-8
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

class MainWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.resize(500, 500)
		self.setWindowTitle('team talk tt file creator')
		self.layout = QGridLayout()
		self.setLayout(self.layout)
		self.username = QLineEdit()
		self.usernameShortcut = QShortcut(QKeySequence('alt+u'), self)
		self.usernameShortcut.activated.connect(self.username.setFocus)
		self.username.setAccessibleName('username: alt+u')
		self.layout.addWidget(self.username)
		self.username.returnPressed.connect(self.Create)

		self.password = QLineEdit()
		self.passwordShortcut = QShortcut(QKeySequence('alt+p'), self)
		self.passwordShortcut.activated.connect(self.password.setFocus)
		self.password.setAccessibleName('password: alt+p')
		self.layout.addWidget(self.password)
		self.password.returnPressed.connect(self.Create)

		self.create = QPushButton('create')
		self.layout.addWidget(self.create)
		self.create.clicked.connect(self.Create)
		self.create.setDefault(True)

		self.about = QPushButton('about')
		self.layout.addWidget(self.about)
		self.about.clicked.connect(self.About)
		self.about.setDefault(True)

		self.exit = QPushButton('exit')
		self.layout.addWidget(self.exit)
		self.exit.clicked.connect(self.Exit)
		self.exit.setDefault(True)

	def Create(self):
		try:
			config = open('config.txt', 'r', encoding="utf_8_sig")
		except:
			msgBox = QMessageBox()
			msgBox.setWindowTitle('config file not found.')
			msgBox.exec()
			return False
		line = []
		for c in config.readlines():
			line.append(c)

		if self.username.text() == '' or self.password.text() == '':
			msgBox = QMessageBox()
			msgBox.setWindowTitle('username and password field can not be empty')
			msgBox.exec()
		else:
			tt = f"""<?xml version='1.0' encoding='UTF-8' ?>
<teamtalk version='5.4'>
    <host>
        <name>{line[1].strip()}</name>
        <address>{line[3].strip()}</address>
        <tcpport>{line[5].strip()}</tcpport>
        <udpport>{line[7].strip()}</udpport>
        <encrypted>false</encrypted>
        <auth>
             <username>{self.username.text()}</username>
            <password>{self.password.text()}</password>
        </auth>
    </host>
</teamtalk>"""
			open(f'{self.username.text()}.tt', 'w', encoding='utf-8').write(tt)
			msgBox = QMessageBox()
			msgBox.setWindowTitle('tt file created successfully')
			msgBox.exec()
			self.username.setText('')
			self.password.setText('')

	def About(self):
		msgBox = QMessageBox()
		msgBox.setWindowTitle('this program is written by samaneh karimzadeh and hamid rezayi.\nTTApp version 1.0')
		msgBox.exec()

	def Exit(self):
		self.close()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
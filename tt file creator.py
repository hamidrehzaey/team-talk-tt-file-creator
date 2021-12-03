# This Python file uses the following encoding: utf-8
import sys, os, ctypes
ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

ORGANIZATION_NAME = 'Example App'
ORGANIZATION_DOMAIN = 'example.com'
APPLICATION_NAME = 'QSettings program'
SETTINGS_TRAY = 'settings/tray'

line = []

class MainWindow(QWidget):
	checkbox = None

	def __init__(self):
		super().__init__()
		self.resize(300, 325)
		self.setWindowTitle('team talk tt file creator')
		self.layout = QGridLayout()
		self.setLayout(self.layout)

		mainLabel = QLabel('this program is written by Hamid Rezayi')
		self.layout.addChildWidget(mainLabel)
		mainLabel.setGeometry(50, 10, 200, 40)

		usernameLabel = QLabel('username:')
		self.layout.addChildWidget(usernameLabel)
		usernameLabel.setGeometry(25, 65, 100, 20)

		self.username = QLineEdit()
		self.usernameShortcut = QShortcut(QKeySequence('alt+u'), self)
		self.usernameShortcut.activated.connect(self.username.setFocus)
		self.username.setAccessibleName('username: alt+u')
		self.layout.addChildWidget(self.username)
		self.username.setGeometry(100, 100, 150, 150)
		self.username.returnPressed.connect(self.Create)
		self.username.setGeometry(25, 90, 100, 20)

		passwordLabel = QLabel('password:')
		self.layout.addChildWidget(passwordLabel)
		passwordLabel.setGeometry(175, 65, 100, 20)

		self.password = QLineEdit()
		self.passwordShortcut = QShortcut(QKeySequence('alt+p'), self)
		self.passwordShortcut.activated.connect(self.password.setFocus)
		self.password.setAccessibleName('password: alt+p')
		self.layout.addChildWidget(self.password)
		self.password.setGeometry(175, 90, 100, 20)
		self.password.returnPressed.connect(self.Create)

		self.nameLabel = QLabel('server name:')
		self.layout.addChildWidget(self.nameLabel)
		self.nameLabel.setGeometry(25, 120, 100, 20)

		self.name = QLineEdit()
		self.name.setAccessibleName("server name:")
		self.layout.addChildWidget(self.name)
		self.name.setGeometry(25, 140, 100, 20)

		self.addressLabel = QLabel('server address:')
		self.layout.addChildWidget(self.addressLabel)
		self.addressLabel.setGeometry(175, 120, 100, 20)

		self.address = QLineEdit()
		self.address.setAccessibleName('server address:')
		self.layout.addChildWidget(self.address)
		self.address.setGeometry(175, 140, 100, 20)

		self.tcpLabel = QLabel('tcp port:')
		self.layout.addChildWidget(self.tcpLabel)
		self.tcpLabel.setGeometry(25, 170, 100, 20)

		self.tcp = QLineEdit()
		self.tcp.setAccessibleName('tcp port:')
		self.layout.addChildWidget(self.tcp)
		self.tcp.setGeometry(25, 190, 100, 20)

		self.udpLabel = QLabel('udp port:')
		self.layout.addChildWidget(self.udpLabel)
		self.udpLabel.setGeometry(175, 170, 100, 20)

		self.udp = QLineEdit()
		self.udp.setAccessibleName('udp port:')
		self.layout.addChildWidget(self.udp)
		self.udp.setGeometry(175, 190, 100, 20)

		self.checkbox = QCheckBox('save server name, address, tcp, udp port')
		self.checkbox.stateChanged.connect(self.Checkbox)
		self.layout.addChildWidget(self.checkbox)
		self.checkbox.setGeometry(25, 230, 250, 20)

		self.settings = QSettings()
		self.check_state = self.settings.value(SETTINGS_TRAY, False, type=bool)
		self.checkbox.setChecked(self.check_state)
		self.settings.setValue(SETTINGS_TRAY, False)
		self.checkbox.clicked.connect(self.save_checkbox_settings)

		self.create = QPushButton('create')
		self.layout.addChildWidget(self.create)
		self.create.clicked.connect(self.Create)
		self.create.setDefault(True)
		self.create.setGeometry(45, 275, 100, 25)

		self.exit = QPushButton('exit')
		self.layout.addChildWidget(self.exit)
		self.exit.clicked.connect(sys.exit)
		self.exit.setDefault(True)
		self.exit.setGeometry(155, 270, 100, 25)

		self.configfile()

		if not os.path.exists('config.txt'):
			self.checkbox.setChecked(False)

	def configfile(self):
			try:
				self.config = open('config.txt', 'r', encoding="utf_8_sig")

				for c in self.config.readlines():
					line.append(c)

				self.name.setText(line[1])
				self.address.setText(line[3])
				self.tcp.setText(line[5])
				self.udp.setText(line[7])

			except:
				pass

	def Checkbox(self, state):
		if state == Qt.CheckState.Checked.value:
			self.nameLabel.hide()
			self.name.hide()
			self.addressLabel.hide()
			self.address.hide()
			self.tcpLabel.hide()
			self.tcp.hide()
			self.udpLabel.hide()
			self.udp.hide()

			self.config = f"""ServverName:
{self.name.text()}
HostAddress:
{self.address.text()}
tcpport:
{self.tcp.text()}
udpport:
{self.udp.text()}"""

		else:
			self.nameLabel.show()
			self.name.show()
			self.addressLabel.show()
			self.address.show()
			self.tcpLabel.show()
			self.tcp.show()
			self.udpLabel.show()
			self.udp.show()

			self.configfile()

	def save_checkbox_settings(self):
		self.settings = QSettings()
		self.settings.setValue(SETTINGS_TRAY, self.checkbox.isChecked())
		self.settings.sync()

		if self.name.text() == '' or self.address.text() == '' or self.tcp.text() == '' or self.udp.text() == '':
			msgBox = QMessageBox()
			msgBox.setWindowTitle('fields are empty')
			msgBox.exec()
			self.checkbox.setChecked(False)

		else:
			try:
				self.Config = open('config.txt', 'x', encoding="utf_8_sig").write(self.config)
			except:
				pass

	def Create(self):
		if self.username.text() == '' or self.password.text() == '' or self.name.text() == '' or self.address.text() == '' or self.tcp.text() == '' or self.udp.text() == '':
			msgBox = QMessageBox()
			msgBox.setWindowTitle('fields can not be empty')
			msgBox.exec()
		else:
			tt = f"""<?xml version='1.0' encoding='UTF-8' ?>
<teamtalk version='5.4'>
    <host>
        <name>{self.name.text().strip()}</name>
        <address>{self.address.text().strip()}</address>
        <tcpport>{self.tcp.text().strip()}</tcpport>
        <udpport>{self.udp.text().strip()}</udpport>
        <encrypted>false</encrypted>
        <auth>
             <username>{self.username.text()}</username>
            <password>{self.password.text()}</password>
        </auth>
    </host>
</teamtalk>"""

			try:
				open(f'{self.username.text()}.tt', 'x', encoding='utf-8').write(tt)
			except:
				msg = QMessageBox()
				msg.setWindowTitle(f'{self.username.text()}.tt already exists') 
				msg.exec()
				return False

			msgBox = QMessageBox()
			msgBox.setWindowTitle('tt file created successfully')
			msgBox.exec()
			self.username.setText('')
			self.password.setText('')

QCoreApplication.setApplicationName(ORGANIZATION_NAME)
QCoreApplication.setOrganizationDomain(ORGANIZATION_DOMAIN)
QCoreApplication.setApplicationName(APPLICATION_NAME)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
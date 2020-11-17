from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from MainWindow import Ui_MainWindow

IMG_LOGO = QImage("./img/logo.png")
IMG_PRINCIPAL = QImage("./img/principal1.png")

class Ui_MainWindow1(object):
	def setupUi1(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(820, 610)
		MainWindow.setMinimumSize(QSize(820, 610))
		MainWindow.setMaximumSize(QSize(820, 610))
		font = QFont()
		font.setFamily("Tahoma")
		MainWindow.setFont(font)
		icon = QIcon()
		icon.addPixmap(QPixmap(IMG_LOGO), QIcon.Selected, QIcon.On)
		MainWindow.setWindowIcon(icon)
		self.firstwidget = QWidget(MainWindow)
		self.firstwidget.setMinimumSize(QSize(820, 610))
		self.firstwidget.setMaximumSize(QSize(815, 610))
		font = QFont()
		font.setFamily("Tahoma")
		self.firstwidget.setFont(font)
		self.firstwidget.setObjectName("firstwidget")
		self.verticalLayout = QVBoxLayout(self.firstwidget)
		self.verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout.setSpacing(0)
		self.verticalLayout.setObjectName("verticalLayout")
		self.frame_2 = QFrame(self.firstwidget)
		self.frame_2.setMinimumSize(QSize(820, 610))
		self.frame_2.setFrameShape(QFrame.NoFrame)
		self.frame_2.setFrameShadow(QFrame.Raised)
		self.frame_2.setObjectName("frame_2")
		self.frame_3 = QFrame(self.frame_2)
		self.frame_3.setGeometry(QRect(-20, 0, 881, 641))
		self.frame_3.setMinimumSize(QSize(0, 0))
		font = QFont()
		font.setFamily("Tahoma")
		self.frame_3.setFont(font)
		self.frame_3.setStyleSheet("\n"
"background-color: rgb(58,58,58);")
		self.frame_3.setFrameShape(QFrame.NoFrame)
		self.frame_3.setFrameShadow(QFrame.Raised)
		self.frame_3.setObjectName("frame_3")
		self.lineEdit_key = QLineEdit(self.frame_3)
		self.lineEdit_key.setGeometry(QRect(270, 360, 321, 31))
		font = QFont()
		font.setFamily("Tahoma")
		font.setPointSize(10)
		self.lineEdit_key.setFont(font)
		self.lineEdit_key.setStyleSheet("QLineEdit{\n"
"border: 3px rgb(45,45,45);\n"
"border-radius: 4px;\n"
"padding: 6px;\n"
"background-color: rgb(30,30,30);\n"
"color: rgb(190,190, 190);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(254, 101, 0)\n"
"}")
		self.lineEdit_key.setMaxLength(23)
		self.lineEdit_key.setObjectName("lineEdit_key")
		self.pushButton_validate = QPushButton(self.frame_3)
		self.pushButton_validate.setGeometry(QRect(340, 410, 181, 31))
		font = QFont()
		font.setFamily("Tahoma")
		font.setPointSize(10)
		self.pushButton_validate.setFont(font)
		self.pushButton_validate.setStyleSheet("QPushButton{\n"
"border: 2px solid rgb(60,60,60);\n"
"color: #f2f2f2;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(254,101,0), stop:1 rgb(227, 90,0));\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(220,86,0)\n"
"}\n"
"")
		self.pushButton_validate.setObjectName("pushButton_validate")
		self.label_footer_2 = QLabel(self.frame_3)
		self.label_footer_2.setGeometry(QRect(282, 580, 310, 31))
		font = QFont()
		font.setFamily("Tahoma")
		font.setPointSize(8)
		font.setBold(True)
		font.setWeight(75)
		self.label_footer_2.setFont(font)
		self.label_footer_2.setStyleSheet("color: #888")
		self.label_footer_2.setOpenExternalLinks(True)
		self.label_footer_2.setObjectName("label_footer_2")
		self.line_255 = QFrame(self.frame_3)
		self.line_255.setGeometry(QRect(20, 18, 41, 562))
		self.line_255.setFrameShape(QFrame.VLine)
		self.line_255.setFrameShadow(QFrame.Sunken)
		self.line_255.setObjectName("line_255")
		self.line_222 = QFrame(self.frame_3)
		self.line_222.setGeometry(QRect(40, 10, 777, 16))
		self.line_222.setFrameShape(QFrame.HLine)
		self.line_222.setFrameShadow(QFrame.Sunken)
		self.line_222.setObjectName("line_222")
		self.line_233 = QFrame(self.frame_3)
		self.line_233.setGeometry(QRect(40, 570, 777, 20))
		self.line_233.setFrameShape(QFrame.HLine)
		self.line_233.setFrameShadow(QFrame.Sunken)
		self.line_233.setObjectName("line_233")
		self.label_logoImagem = QLabel(self.frame_3)
		self.label_logoImagem.setGeometry(QRect(307, 80, 250, 250))
		self.label_logoImagem.setText("")
		self.label_logoImagem.setPixmap(QPixmap(IMG_PRINCIPAL))
		self.label_logoImagem.setScaledContents(True)
		self.label_logoImagem.setObjectName("label_logoImagem")
		self.label_chave = QLabel(self.frame_3)
		self.label_chave.setGeometry(QRect(297, 338, 113, 17))
		font = QFont()
		font.setFamily("Tahoma")
		font.setPointSize(9)
		self.label_chave.setFont(font)
		self.label_chave.setStyleSheet("color: #f2f2f2")
		self.label_chave.setObjectName("label_chave")
		self.line_244 = QFrame(self.frame_3)
		self.line_244.setGeometry(QRect(810, 18, 16, 562))
		self.line_244.setFrameShape(QFrame.VLine)
		self.line_244.setFrameShadow(QFrame.Sunken)
		self.line_244.setObjectName("line_244")
		self.label_iconeChave = QLabel(self.frame_3)
		self.label_iconeChave.setGeometry(QRect(273, 335, 16, 21))
		font = QFont()
		font.setFamily("Tahoma")
		font.setPointSize(12)
		self.label_iconeChave.setFont(font)
		self.label_iconeChave.setStyleSheet("color:rgb(245, 119, 41);")
		self.label_iconeChave.setScaledContents(False)
		self.label_iconeChave.setObjectName("label_iconeChave")
		self.label_statusAtivacao = QLabel(self.frame_3)
		self.label_statusAtivacao.setGeometry(QRect(280, 470, 291, 61))
		font = QFont()
		font.setFamily("Tahoma")
		font.setPointSize(12)
		self.label_statusAtivacao.setFont(font)
		self.label_statusAtivacao.setStyleSheet("color: #FF6347")
		self.label_statusAtivacao.setText("")
		self.label_statusAtivacao.setAlignment(Qt.AlignCenter)
		self.label_statusAtivacao.setObjectName("label_statusAtivacao")
		self.line_255.raise_()
		self.lineEdit_key.raise_()
		self.pushButton_validate.raise_()
		self.line_222.raise_()
		self.label_footer_2.raise_()
		self.label_logoImagem.raise_()
		self.label_chave.raise_()
		self.line_244.raise_()
		self.line_233.raise_()
		self.label_iconeChave.raise_()
		self.label_statusAtivacao.raise_()
		self.verticalLayout.addWidget(self.frame_2)
		MainWindow.setCentralWidget(self.firstwidget)

		self.retranslateUi(MainWindow)
		QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "LogroBot - IQ Automática"))
		self.lineEdit_key.setPlaceholderText(_translate("MainWindow", "XXXXX-XXXXX-XXXXX-XXXXX"))
		self.pushButton_validate.setText(_translate("MainWindow", "Validar "))
		self.label_footer_2.setText(_translate("MainWindow", "LogroBot V1.0.0 Estável - <a href=\"https://irangarcia.dev/logrobot/index.html\"><span style=\"color:rgb(245, 119, 41);\">irangarcia.dev/logrobot"))
		self.label_chave.setText(_translate("MainWindow", "Chave de Ativação:"))
		self.label_iconeChave.setText(_translate("MainWindow", "🔑"))


if __name__ == "__main__":
	import sys
	app = QApplication(sys.argv)
	MainWindow = QMainWindow()
	ui = Ui_MainWindow1()
	ui.setupUi1(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())

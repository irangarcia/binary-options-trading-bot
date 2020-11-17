from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from licensing.models import *
from licensing.methods import Key, Helpers
from iqoptionapi.stable_api import IQ_Option
from iqoptionapi.constants import ACTIVES
import time, sys
from threading import Thread, Timer
from datetime import datetime
from datetime import timezone
from datetime import timedelta
from dateutil import tz

from MainWindow import Ui_MainWindow
from ValidationPage import Ui_MainWindow1

class EmittingStream(QObject):

	textWritten = pyqtSignal(str)

	def write(self, textw):
		self.textWritten.emit(str(textw))

class First(QMainWindow, Ui_MainWindow1):
	def __init__(self, *args, **kwargs):
		super(First, self).__init__(*args, **kwargs)
		self.setupUi1(self)
		self.pushButton_validate.clicked.connect(self.validationPage)
		self.lineEdit_key.returnPressed.connect(self.validationPage)

	def validationPage(self):		
		self.hide()
		self.ui= MainWindow()
		print("Sua licença expira em: " + str(license_key.expires))

lastplayer = 0

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		self.setupUi(self)

		self._generator = None
		self._timerId = None
		sys.stdout = EmittingStream(textWritten=self.normalOutputWritten)

		self.sinais_usados = []

		self.opcaoBinaria = 'live-deal-binary-option-placed' # Binária
		self.filtro = []
		self.lucro = 0
		
		self.pushButton_login.clicked.connect(self.logar)
		self.pushButton_chooseFile.clicked.connect(self.getFiles)
		self.comboBox_chooseMode.activated.connect(self.getComboValue)
		self.realOrTraining = ['Treinamento', 'Conta Real']
		self.comboBox_chooseMode.addItems(self.realOrTraining) 
		self.opcoesListCopy = ['COPIAR ENTRADAS', 'CARREGAR LISTA']
		self.comboBox_listaCopy.addItems(self.opcoesListCopy)  
		self.comboBox_listaCopy.activated.connect(self.listaOuCopy)
		self.countries = ['Mundo','África do Sul', 'Brasil', 'Colômbia' ,'Índia','Tailândia',]
		self.comboBox_chooseCountry.addItems(self.countries)
		self.comboBox_chooseCountry.activated.connect(self.chooseCountry)
		self.check_porcentagem.stateChanged.connect(self.setarPorcentagem)
		self.pushButton_start.clicked.connect(self.start)
		self.pushButton_stop.clicked.connect(self.stop)	
		self.lineEdit_senha.returnPressed.connect(self.logar) 
		self.listaOuCopy()
		self.show()

	def setarPorcentagem(self):
		if self.check_porcentagem.isChecked() == True:
			print('Você selecionou valor em porcentagem.')
		else:
			print('Você selecionou valor unitário.')

	def logar(self):
		self.email=str(self.lineEdit_email.text())
		self.senha=str(self.lineEdit_senha.text())
		self.API = IQ_Option(self.email, self.senha)
		self.API.connect()
		if not self.API.check_connect():
			print('Erro na conexão. Tente novamente.')
			self.label_13.setText("Erro na conexão")
			self.label_13.setStyleSheet("color: #FF0000;")
		else:
			print('Conectado com sucesso!')
			self.label_13.setText("Conectado")
			self.label_13.setStyleSheet("color: #08F26E;")
			self.comboBox_chooseMode.setCurrentIndex(0)
			self.API.change_balance('PRACTICE')
			self.label_banca.setText(str(self.API.get_balance()))

	def listaOuCopy(self):
		if self.comboBox_listaCopy.currentIndex() == 0:
			self.spinBox_ranking.show()
			self.spinBox_ranking1.show()
			self.label_26.show()
			self.label_28.show()
			self.label_29.show()
			self.radioButton_Copy.show()
			self.comboBox_chooseCountry.show()
			self.spinBox_rankingFixo.show()
			self.radioButton_Posicao.show()
			self.spinBox_valorMin.show()
			self.label_30.show()
			self.label_5.hide()
			self.label_8.hide()
			self.pushButton_chooseFile.hide()
		elif self.comboBox_listaCopy.currentIndex() == 1:	
			self.label_5.show()
			self.label_8.show()
			self.pushButton_chooseFile.show()
			self.spinBox_ranking.hide()
			self.spinBox_ranking1.hide()
			self.label_26.hide()
			self.label_28.hide()
			self.label_29.hide()
			self.label_30.hide()
			self.radioButton_Copy.hide()
			self.comboBox_chooseCountry.hide()
			self.spinBox_valorMin.hide()
			self.spinBox_rankingFixo.hide()
			self.radioButton_Posicao.hide()

	def timestampConverter(self, time):  
		hora = datetime.strptime(datetime.utcfromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
		hora = hora.replace(tzinfo=tz.gettz('GMT'))

		return str(hora.astimezone(tz.gettz('America/Sao Paulo')))[:-6]

	def timestampConverterCopy(self, x, y, z):
		timestamp1, ms1 = divmod(x, 1000)
		timestamp2, ms2 = divmod(y, 1000)
		timestamp3, ms3 = divmod(z, 1000)

		entradacodt = datetime.fromtimestamp(timestamp1) + timedelta(milliseconds=ms1)
		expiracaodt = datetime.fromtimestamp(timestamp2) + timedelta(milliseconds=ms2)
		horaatualdt = datetime.fromtimestamp(timestamp3) + timedelta(milliseconds=ms3)

		entradaco = entradacodt.strftime('%Y-%m-%d %H:%M:%S')
		expiracao = expiracaodt.strftime('%Y-%m-%d %H:%M:%S')
		horaatual = horaatualdt.strftime('%Y-%m-%d %H:%M:%S')


		mintime1 = timedelta(milliseconds=x)
		mintime2 = timedelta(milliseconds=y)	
		mintime3 = timedelta(milliseconds=z)
		min1 = mintime1.seconds
		min2 = mintime2.seconds	
		min3 = mintime3.seconds	

		exptime = min2 - min1
		delaytime = min3 - min1                         
		expminutes = (exptime % 3600) // 60   
		if expminutes == 0:
			expminutes = 1                       
	
		return [entradaco, expiracao, horaatual, expminutes, delaytime]	

	def chooseCountry(self):
		if self.comboBox_chooseCountry.currentIndex() == 0:
			print('Você mudou para o Ranking Mundial.')
			self.country = "Worldwide"
		elif self.comboBox_chooseCountry.currentIndex() == 1: 
			print('Você mudou para o Ranking Sul-Africano.')
			self.country = "SA"
		elif self.comboBox_chooseCountry.currentIndex() == 2: 
			print('Você mudou para o Ranking Brasileiro.')
			self.country = "BR"
		elif self.comboBox_chooseCountry.currentIndex() == 3: 
			print('Você mudou para o Ranking Colombiano.')
			self.country = "CO"
		elif self.comboBox_chooseCountry.currentIndex() == 4: 
			print('Você mudou para o Ranking Indiano.')
			self.country = "IN"
		elif self.comboBox_chooseCountry.currentIndex() == 5: 
			print('Você mudou para o Ranking Tailândes.')
			self.country = "TH"

	def filtroRanking(self, country, numeroInicial, numeroFinal):
		self.filtro.clear()
		while True:		
			try:
				ranking = self.API.get_leader_board(self.country, self.numeroInicial, self.numeroFinal, 0)

				for n in ranking['result']['positional']:
					id = ranking['result']['positional'][n]['user_id']
					self.filtro.append(id)
			except:
				pass

			time.sleep(180)
			 #Atualiza Ranking a cada 3 minutos.

	def ajustesEntradaBinaria(self, ti):
		global lastplayer
		trades = self.API.get_live_deal(ti)
		for trade in list(trades):
			if self.check_porcentagem.isChecked() == True:
				self.valor_entrada = (int(self.spinBox_gerenciamento.value()))*(float(self.spinBox_valueEntry.value()/100))
			else: 
				self.valor_entrada = float(self.spinBox_valueEntry.value())

			self.valorMin = int(self.spinBox_valorMin.value()) 
			self.mGale = int(self.spinBox_martingale.value())
			entradacopy = trade['created_at']	
			expiracao = trade['expiration']
			horalocal = int(datetime.now(tz=timezone.utc).timestamp() * 1000)
			timecopy = self.timestampConverterCopy(entradacopy, expiracao, horalocal)

			if lastplayer != trade['user_id'] and trade['amount_enrolled'] >= int(self.valorMin) and int(timecopy[3]) < 20 and int(timecopy[4]) < 3:
				if trade['user_id'] in self.filtro:
					lastplayer = trade['user_id']
					ativo = list(ACTIVES.keys())[list(ACTIVES.values()).index(trade['active_id'])]

					print("\nNOME: "+str(trade['name'])+" | PAÍS: "+str(trade['flag'])+" | $ "+str(trade['amount_enrolled'])+"\n"+ trade['direction'].upper() + " | " +str(ativo)+" | "+str(timecopy[0])) 
					print("SUA ENTRADA: $ "+str(round(self.valor_entrada, 2))+" | DELAY: "+str(timecopy[4] + 1)+"s")

					bcall = Thread(target=self.entrada, args=(self.valor_entrada, str(ativo), trade['direction'], int(timecopy[3]), horalocal, self.mGale))
					bcall.start()

			trades.clear()
					

	def comecarCopy(self):
		self.API.subscribe_live_deal(self.opcaoBinaria, 10)

		if self.radioButton_Copy.isChecked() == True: 
			self.numeroInicial=int(self.spinBox_ranking.value())
			self.numeroFinal=int(self.spinBox_ranking1.value())
		else: 
			self.numeroInicial=int(self.spinBox_ranking.value())
			self.numeroFinal=int(self.spinBox_ranking.value())

		if self.numeroInicial == self.numeroFinal:
			print("Carregando entradas do Top " + str(self.numeroInicial))
		elif self.numeroInicial != self.numeroFinal:
			print("Carregando entradas do Top "+ str(self.numeroInicial) + " ao " + str(self.numeroFinal) +".")

		catalogo = Thread(target=self.filtroRanking, args=(self.country, self.numeroInicial, self.numeroFinal))
		catalogo.daemon = True
		catalogo.start()

		while True:
			self.ajustesEntradaBinaria(self.opcaoBinaria)
			yield 
			
		self.API.unscribe_live_deal(self.opcaoBinaria)

	def getFiles(self):
		self.filename = QFileDialog.getOpenFileName(None, 'Select a file', '', '*.txt')
		self.path = self.filename[0]    

		with open(self.path, "r") as f:
			self.text = f.read()
			self.textEdit_output.setText(self.text)

	def carregarSinais(self):
		with open(self.path, "r") as f:
			self.text = f.read()
			self.textEdit_output.setText(self.text)
			f.close()
			self.text = self.text.split('\n')
			for index, a in enumerate(self.text):
				if a == '':
					del self.text[index]
		return self.text

	def normalOutputWritten(self, textw):
		cursor = self.textEdit_terminal.textCursor()
		cursor.movePosition(QTextCursor.End)
		cursor.insertText(textw)
		self.textEdit_terminal.setTextCursor(cursor)
		self.textEdit_terminal.ensureCursorVisible()
		
	def stopWL(self, lucro, gain,loss):
		if self.lucro <= float('-' + str(abs(loss))):
			print('Stop Loss batido!')
			self.stop()
		if self.lucro >= float(abs(gain)):
			print('Stop Win batido!')
			self.stop()

	def stopWLM(self, lucro, gain,loss):
		if self.lucro <= float('-' + str(abs(loss))):
			sys.exit()
		if self.lucro >= float(abs(gain)):
			sys.exit()

	def meucheckwin(self, id_number): 
		while True:
			stat, lista = self.API.get_position_history_v2('turbo-option', 15, 0, 0, 0) #15 é a quantidade de orders passadas quiser puxar. Pode por quantas quiser.
			xindex = next((index for (index, d) in enumerate(lista['positions']) if d['raw_event']['option_id'] == id_number), -1)
			if xindex >=0:
				x = list(lista['positions'])
				lucro = x[xindex]['close_profit']
				invest = x[xindex]['invest']
				resultado = lucro - invest
				return resultado
				break

	def entrada(self, valor, par_moedas, acao_entrada, expiracao, hora_operacao, gale):
		status, id_order = self.API.buy(valor, par_moedas, acao_entrada, expiracao)
		print(id_order)
		if status:
			resultado = self.meucheckwin(id_order)
			self.lucro += round(resultado, 2)
			if self.check_porcentagem.isChecked() == True: 
				self.stopWin = (float(self.spinBox_gerenciamento.value()))*(float(int(self.spinBox_stopWin.value())/100))
				self.stopLoss = (float(self.spinBox_gerenciamento.value()))*(float(int(self.spinBox_stopLoss.value())/100))
			else: 
				self.stopWin = float(self.spinBox_stopWin.value())
				self.stopLoss = float(self.spinBox_stopLoss.value())


			if resultado > 0 :
				print('\n✅ WIN | ' + 'LUCRO: $ ' + str(round(resultado, 2)) + ' | ' + str(acao_entrada.upper()) + ' ' + str(par_moedas))
			elif resultado == 0:
				print('\nEMPATE | ' + 'LUCRO: $ ' + str(round(resultado, 2)) + ' | ' + str(acao_entrada.upper()) + ' ' + str(par_moedas))
			elif resultado < 0:
				print('\n❌ LOSS | ' + 'LUCRO: $ ' + str(round(resultado, 2)) + ' | ' + str(acao_entrada.upper()) + ' ' + str(par_moedas))

			self.stopWL(self.lucro, self.stopWin, self.stopLoss)
			if resultado < 0 and gale > 0:
				valor_com_martingale = (valor * 2.2)
				self.stopWLM(self.lucro, self.stopWin, self.stopLoss)
				print('\n🔁 MARTINGALE ' + str(gale) + ' | VALOR: $ ' + str(round(valor_com_martingale, 2)) + ' | ' + acao_entrada.upper() + ' ' + par_moedas)
				gale = gale - 1
				Thread(target=self.entrada, args=(valor_com_martingale, par_moedas, acao_entrada, expiracao, self.timestampConverter(self.API.get_server_timestamp()), gale,)).start()
				return True
			return True
		else:
			print('Não foi possivel realizar a sua entrada.')
			return False

	def martinGale(self, tipo, valor):
		if tipo == 'auto':
			return valor * 2.2

	def loopGenerator(self):
		while True:
			self.agora = self.timestampConverter(self.API.get_server_timestamp())
			for sinal in self.text:
				dados = sinal.split(',')
				if dados[0] == self.agora and sinal not in self.sinais_usados:
					self.sinais_usados.append(sinal)
					valor_entrada = (float(self.spinBox_gerenciamento.value()))*(float(self.spinBox_valueEntry.value()/100))
					par = dados[1]
					acao = dados[2].lower()
					expiracao = int(dados[3])
					gale = int(self.spinBox_martingale.value())
					print('\n' + acao.upper() + ' | ' + par + ' | ' + self.agora + '\nSUA ENTRADA: $ ' + str(valor_entrada))
					Thread(target=self.entrada, args=(valor_entrada, par, acao, expiracao, dados[0], gale,)).start()
				yield

	def start(self):
		if self.comboBox_listaCopy.currentIndex() == 0:
			print('Aplicação inicializada!')
			self.stop()  # Stop any existing timer
			self._generator = self.comecarCopy()  # Start the loop
			self._timerId = self.startTimer(0)
		else:
			self.text = self.carregarSinais()
			print('Aplicação inicializada!')
			print('Sinais prontos! Aguardando hora de entrada.')
			self.stop()  # Stop any existing timer
			self._generator = self.loopGenerator()  # Start the loop
			self._timerId = self.startTimer(0)

	def stop(self):
		if self._timerId is not None:
			print('Aplicação parada!')
			self.killTimer(self._timerId)
			self.label_banca.setText(str(self.API.get_balance()))
		self._generator = None
		self._timerId = None

	def timerEvent(self, event):
		# This is called every time the GUI is idle.
		if self._generator is None:
			return
		try:
			next(self._generator)  # Run the next iteration
		except StopIteration:
			self.stop()

	def getComboValue(self):
		if self.comboBox_chooseMode.currentIndex():
			print('Você mudou para a Conta Real.')
			self.API.change_balance('REAL')
			self.label_banca.setText(str(self.API.get_balance()))
		elif self.comboBox_chooseMode.currentIndexChanged: 
			print('Você mudou para a Conta de Treinamento.')
			self.API.change_balance('PRACTICE')
			self.label_banca.setText(str(self.API.get_balance()))


if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	w = First()
	w.show()
	sys.exit(app.exec_())
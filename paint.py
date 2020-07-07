
from PyQt5 import QtCore, QtGui, QtWidgets

import shared
#from formmodule import Ui_FormModule
#from moduleWidget import Ui_ModuleWidget

class Paint(QtWidgets.QGraphicsView):
	factor = 1.25
	def __init__(self,parent=None):
		super(Paint, self).__init__()
		self.parent = parent

	#def	__init__(self):
	#	QtWidgets.QGraphicsView.__init__(self)

		#self.setObjectName("Paint")
		
		self.scene	=	QtWidgets.QGraphicsScene()
		self.rubberBand = QtWidgets.QRubberBand(QtWidgets.QRubberBand.Rectangle, self)
		self.origin = QtCore.QPoint() 

		self.P1 = [0,0]
		self.P2 = [0,0]
		self.P3 = [0,0] #alineado con P1 x P2 y
		self.P4 = [0,0] #alineado con P2 x P1 y

		self.Pm1 = [0,0]
		self.Pm2 = [0,0]

		self.flagRelease = False
		self.flagSelection = False
		self.flagTab = False

	#	self.retranslateUi(self)
	#	QtCore.QMetaObject.connectSlotsByName(self)

		self.contextMenuEvent
		self.mousePressEvent
		self.mouseReleaseEvent
		self.mouseMoveEvent
		#self.resizeEvent

	#	print("sceneRect:",self.sceneRect())
		
		###Para realizar el zoom con teclas ctrl+ / ctrl -
		#self.selAllShort = QtWidgets.QShortcut(QtGui.QKeySequence(QtGui.QKeySequence.ZoomIn),self,context= QtCore.Qt.WidgetShortcut,)
		#self.selAllShort.activated.connect(self.zoom_in)
		#self.selAllShort = QtWidgets.QShortcut(QtGui.QKeySequence(QtGui.QKeySequence.ZoomOut),self,context= QtCore.Qt.WidgetShortcut,)
		#self.selAllShort.activated.connect(self.zoom_out)


	def retranslateUi(self, Paint):
		_translate = QtCore.QCoreApplication.translate
		Paint.setWindowTitle(_translate("Paint", "Paint"))


	def showEvent(self,event):
		print("showE")
		if self.parent.flagZoom != True:
			if self.parent.flagNormal != False: 
				self.setSceneRect(0,90,1280,523)
			else:
				self.setSceneRect(0,0,1280,523)

		if self.parent.flagCircuit != True:
			self.populateCircuit()
			self.parent.tmpTabs.append('1%')
		else:
			z = self.parent.tabWidget.currentIndex() + 1 #tab-current

			if z == 0:
				z = 1

			try:
				self.parent.tmpTabs.index(str(z)+'%')

			except:

				#-------------- For lblmodule ----------------#
				for i in range(0,len(self.parent.lblmodule),2):
					numberTab = self.parent.lblmodule[i]
					k = numberTab.replace('%','')

					if k == str(z):
						if self.flagTab != True:
							try:
								self.parent.tmpTabs.index(str(z)+'%')
								self.flagTab = True

							except:
								self.parent.tmpTabs.append(str(z)+'%')

						val = self.parent.lblmodule[i+1]
						
						self.scene.addWidget(val) 
						self.setScene(self.scene)
				
				#-------------- For labels -------------------#
				for i in range(0,len(self.parent.labels),2):
					numberTab = self.parent.labels[i]
					k = numberTab.replace('%','')

					if k == str(z):
						val = self.parent.labels[i+1]
						
						self.scene.addWidget(val)
						self.setScene(self.scene)

				#-------------- For progress -----------------#
				for i in range(0,len(self.parent.progress),2):
					numberTab = self.parent.progress[i]
					k = numberTab.replace('%','')

					if k == str(z):
						val = self.parent.progress[i+1]
						
						self.scene.addWidget(val)
						self.setScene(self.scene)

		self.populateLabel()
		self.populateZoom()

	def populateZoom(self):
		print("populateZoom")
		#print(self.parent.flagZoom)
		if len(self.parent.valueZoom) != 0:
			tr = self.parent.valueZoom[0]
			self.setTransform(tr)

			if self.parent.flagZoom != False:
				print("entraZoom")
				self.setSceneRect(0.0,0.0,0.0,0.0)

	def populateCircuit(self): 
		print("PopulateCircuit")
		self.parent.flagCircuit = True
		self.parent.listSelect.clear()

		cbText = self.parent.comboBox.currentText()
		cbText2 =  self.parent.comboBox.currentIndex()+1

		for i in range(0,len(self.parent.mylist),4):
			numberTab = self.parent.mylist[i]
			coordCell = self.parent.mylist #i+1 
			#nameCell = self.parent.mylist#[i+2]
			addrCell = self.parent.mylist[i+3].split("A=")

			z = self.parent.tabWidget.currentIndex() + 1 
			k = numberTab.replace('%','')

			if z == 0:
				z = 1

			#------------ Font labels ----------#
			font = QtGui.QFont()
			font.setFamily("Ubuntu Light")
			font.setPointSize(12)
			font.setBold(True)
			font.setWeight(75)


			#if k == str(z):
			nameCell = self.parent.mylist[i+2].split()
			nameF = nameCell[0].partition('N=')
			tmp = coordCell[i+1].split()

			#--------------- name label----------------#
			lb = QtWidgets.QLabel(nameF[2])

			lb.setFont(font)
			lb.setStyleSheet("QLabel { background-color : ghostwhite;}")
			lb.setFrameShape(QtWidgets.QFrame.Box)
			lb.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)

			#------------label options value A,V,T,S,t,TT...------------#
			lb2 = QtWidgets.QLabel(shared.DEV[int(addrCell[1])][cbText2]+cbText)

			lb2.setFont(font)
			lb2.setStyleSheet("QLabel { background-color : lightblue; color : black;  border: 1px solid black; }")
			lb2.setFrameShape(QtWidgets.QFrame.Box)
			lb2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)

			#------------------- value ProgressBar-----------------------#
			pbProgram = QtWidgets.QProgressBar()
			pbProgram.setStyleSheet("QProgressBar\n"
"{\n"
"	border: 1px solid black;\n"
"	border-radius: 0px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"	background-color: blue;\n"
"	width: 2.15px;\n"
"	margin: 0.5px;\n"
"}")
			pbProgram.setProperty("value",0)

			#----------- coord -------------#
			for i in range(2):
				if i == 0:
					y = tmp[0].partition('X=')
					coordx = int(y[2])
	
				else:
					y = tmp[1].partition('Y=')
					coordy = int(y[2])

			lb.setGeometry(QtCore.QRect(75*coordy,0+(60*coordx), 73, 18))
			lb2.setGeometry(QtCore.QRect(75*coordy,18+(60*coordx), 73, 22))
			pbProgram.setAttribute(QtCore.Qt.WA_TranslucentBackground,True)
			pbProgram.setGeometry(QtCore.QRect(75*coordy, 38+(60*coordx), 73, 19)) 

			#---------- Add list-----------#
			self.parent.lblmodule.append(numberTab)
			self.parent.lblmodule.append(lb)

			self.parent.labels.append(numberTab)
			self.parent.labels.append(lb2)

			self.parent.progress.append(numberTab)
			self.parent.progress.append(pbProgram)

			#------------------Add scene------------------#
			if k == str(z):
				self.scene.addWidget(lb)
				self.setScene(self.scene)

				self.scene.addWidget(lb2)
				self.setScene(self.scene)

				self.scene.addWidget(pbProgram)
				self.setScene(self.scene)


	def populateLabel(self):
		print("PopulateLabel")
		for i in range(0,len(self.parent.mylabel),3):
			numberTabL = self.parent.mylabel[i]
			coordCellL = self.parent.mylabel #[i+1]
			nameCellL = self.parent.mylabel[i+2]

			z = self.parent.tabWidget.currentIndex() + 1 
			k = numberTabL.replace('%','')

			if z == 0:
				z = 1

			#print("z2",z)
			#print("k2",k)
			label = nameCellL.split('#')
			number = label[1].split('$')
			lblt = QtGui.QFont("Arial",int(number[0]), QtGui.QFont.Black)
			#item = QtWidgets.QTableWidgetItem(label[0])
			lbltext = QtWidgets.QLabel(label[0])

			if number[1] == 'AT':
				lbltext.setAlignment(QtCore.Qt.AlignTop)
			else:
				lbltext.setAlignment(QtCore.Qt.AlignBottom)

			lbltext.setFont(lblt)
			lbltext.setStyleSheet("QLabel { background-color : white; }")
			#item.setFont(lblt)
			#item.setBackground(QtGui.QColor('white'))

			if k == str(z):
				tmpL = coordCellL[i+1].split()
				for i in range(2):
					if i == 0:
						y = tmpL[0].partition('X=')
						coordx = y[2]
					else:
						y = tmpL[1].partition('Y=')
						coordy = y[2]

				lbltext.move(int(coordy)*75,int(coordx)*57)
				self.scene.addWidget(lbltext)
				self.setScene(self.scene)

	def contextMenuEvent(self,event):
		print("contextEvent")
		self.rubberBand.hide()
		self.popMenu = QtWidgets.QMenu(self)
		startAct = self.popMenu.addAction('LoadPrograms/Start')
		pauseAct = self.popMenu.addAction('Pause')
		stopAct = self.popMenu.addAction('Stop')

		action = self.popMenu.exec_(self.mapToGlobal(event.pos()))

		if action == startAct:
			self.parent.btnIniciar()

		elif action == pauseAct:
			self.parent.btnPausar()
		
		elif action == stopAct:
			self.parent.btnDetener()

	def totalMylist(self):
		self.auxMylist = self.parent.newlist[:]

	def	mousePressEvent(self,event):
		if event.button() ==  QtCore.Qt.LeftButton:
			self.flagRelease = False

			self.P1[0] = event.pos().x()
			self.P1[1] = event.pos().y()

		#	print("P1:",self.P1)
			self.origin = QtCore.QPoint(event.pos())
			self.rubberBand.setGeometry(QtCore.QRect(self.origin,QtCore.QSize()))
			self.rubberBand.show()
		#	print("P1G:",event.globalPos())
		#	print("P1D:",event.localPos())


	def mouseMoveEvent(self, event):
		if self.flagRelease != True:
			if not self.origin.isNull():
				self.rubberBand.setGeometry(QtCore.QRect(self.origin,event.pos()).normalized())		


	def mouseReleaseEvent(self, event):
		if event.button() == QtCore.Qt.LeftButton:
			self.flagRelease = True
			self.P2[0] = event.pos().x()
			self.P2[1] = event.pos().y()

			self.P3[0] = self.P1[0]  #alineado con P1 x P2 y
			self.P3[1] = self.P2[1]
			
			self.P4[0] = self.P2[0]  #alineado con P2 x P1 y
			self.P4[1] = self.P1[1]

		#	print("P2:",self.P2)
		#	print("P3:",self.P3)
		#	print("P4:",self.P4)

		#	print("P2G:",event.globalPos())
		#	print("P1D:",event.localPos())

			self.populateCircuit()

	def zoomCmb(self,det):
		#print("zoom comb")
		#print("det:",det)

		if det > 0.8:
			print("flagZoom")
			self.parent.flagZoom = True
			self.setSceneRect(0.0,0.0,2000,1000) #rango a posible cambio
		else:
			self.parent.flagZoom = False
		
		scale_tr = QtGui.QTransform()
		scale_tr.scale(Paint.factor,Paint.factor)
		
		scale_tr2 = QtGui.QTransform()
		scale_tr2.scale(det,det)

		tr = scale_tr2 * scale_tr
		#print("tr:",tr)
		self.setTransform(tr)
		#print("2:",self.transform().determinant())

		self.parent.valueZoom.clear()
		self.parent.valueZoom.append(tr)

	'''
	def zoom_in(self):
		#print("zoom_in")
		scale_tr = QtGui.QTransform()
		scale_tr.scale(Paint.factor, Paint.factor)
		tr = self.transform() * scale_tr
		
		self.setTransform(tr)
		self.parent.valueZoom.clear()

		self.parent.valueZoom.append('zoom_in')
		self.parent.valueZoom.append(tr)

	def zoom_out(self):
		#print("zoom_out")
		scale_tr = QtGui.QTransform()
		scale_tr.scale(Paint.factor, Paint.factor)
		scale_inverted, invertible = scale_tr.inverted()
		
		if invertible:
			tr = self.transform() * scale_inverted
			self.setTransform(tr)

		self.parent.valueZoom.clear()
		self.parent.valueZoom.append('zoom_out')
		self.parent.valueZoom.append(tr)
	'''



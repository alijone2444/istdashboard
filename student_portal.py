from PyQt5.QtWidgets import (QApplication, QMainWindow,QLabel,QGridLayout,QPushButton,QMenu,QAction,QFrame,QScrollArea,QHBoxLayout,QWidget,QGroupBox,QCheckBox,QTableWidget,QTableWidgetItem
,QVBoxLayout,QFormLayout,QGridLayout,QMessageBox,QStackedLayout,QAbstractItemView,QHeaderView)
from PyQt5.QtGui import QFont,QPixmap,QIcon,QMovie
from PyQt5.QtCore import Qt
import sys
from reqest_and_response import RequestAndResponse



 
class Portal(QMainWindow):
	def __init__(self):
		super().__init__()
		w=1000
		h=640
		self.setStyleSheet( '''QMainWindow{background-color:black}QScrollBar{ background-color: darkgrey}QTableWidget::item {background-color:lightblue;border: 1px solid black;color:black}
			QTableWidget::item::hover{background-color:white}QTableWidget::item::selected{background-color:white}
			QHeaderView::section {border:1px solid black;}QHeaderView:section:hover{background-color:lightblue}''')

		self.setWindowTitle("Student portal")
		self.setWindowIcon(QIcon('logo'))
		self.resize(w,h)

		self.widget = QWidget(self)
		self.setCentralWidget(self.widget)
		self.gridlayout =QGridLayout(self.widget)

		self.grid3 = QGridLayout(self)
		self.label = QLabel("None",self)
		self.label.setStyleSheet("background-color:black;")
		self.label.setMaximumSize(2000,840)
		self.label.setAlignment(Qt.AlignCenter)
		self.label.setLayout(self.grid3)

		self.movie = QMovie("loader.gif")
		self.label.setMovie(self.movie)
		self.label.setScaledContents(True)
		self.movie.setSpeed(200)
		self.movie.start()

		self.hb = QHBoxLayout(self)
		self.empty_label2 = QLabel(self)
		self.empty_label2.setFixedSize(170,50)
		self.empty_label2.setStyleSheet("border:2px solid transparent")
		self.empty_label2.setLayout(self.hb)
		self.student_label = QLabel("Students",self)
		self.student_label.setStyleSheet("background-color:transparent;color:rgba(72,221,253,255);border-style:none")
		self.student_label.setMaximumSize(150,30)
		self.student_label.setAlignment(Qt.AlignCenter)
		self.student_label.setFont(QFont("arial",15))


		self.goback = QPushButton("<",self)
		self.goback.setStyleSheet('''QPushButton{background-color:black;color:red;border-radius:5px;border:2px solid red;}
			QPushButton:hover{background-color:rgb(160, 91, 60);color:red;border:2px solid red;}
			QPushButton:pressed{background-color:rgb(200, 123, 96)}
			''')
		self.goback.setFixedSize(30,30)
		self.goback.clicked.connect(lambda:portal.going_back_to_dashboard())
		self.hb.addWidget(self.goback)
		self.hb.addWidget(self.student_label)


		self.attendance = QPushButton("Attendance",self)
		self.attendance.setStyleSheet('''QPushButton{background-color:black;color:rgba(72,221,253,255);border-radius:5px;border:2px solid #52bdf6;}
			QPushButton:hover{color:white;border:2px solid white;}
			QPushButton:pressed{background-color:grey}
			''')
		self.attendance.setFixedSize(170,30)
		

		self.assembly_language = QAction("computer organization and assembly lamguage")
		self.assembly_language_lab = QAction("computer organization and assembly lamguage lab")
		self.data_structure = QAction("data structure")
		self.data_structure_lab = QAction("data structure lab")
		self.discrete_structure = QAction("discrete structure")
		self.graph_theory = QAction("graph theory")
		self.profesional_practices = QAction("professional practices",print("profesional_practices"))		
		self.menu = QMenu()

		self.menu.setStyleSheet('''QMenu{background-color:rgba(72,221,253,255);
			border:2px solid rgba(72,221,253,255);border-top:2px solid black;}
			QMenu.item.selected {color:rgba(72,221,253,255);}
			QMenu:pressed{background-color:lightblue}''')
		menu = self.menu.addMenu("courses")
		menu.addAction(self.assembly_language)
		menu.addAction(self.assembly_language_lab)
		menu.addAction(self.data_structure)
		menu.addAction(self.data_structure_lab)
		menu.addAction(self.graph_theory)
		menu.addAction(self.profesional_practices)
		menu.addAction(self.assembly_language_lab)
		self.attendance.setMenu(self.menu)


		self.result = QPushButton("results",self)
		self.result.setStyleSheet('''QPushButton{background-color:black;color:rgba(72,221,253,255);border-radius:5px;border:2px solid #52bdf6;}
			QPushButton:hover{border:2px solid white;}
			QPushButton:pressed{background-color:grey}
			''')
		self.result.setFixedSize(170,30)
		
		self.quizes = QAction("Quizes")
		self.assignments = QAction("Assignments")
		self.project = QAction("Project")
		self.presentation = QAction("presentation")
		self.oht1 = QAction("oht1")
		self.oht2 = QAction("oht2")
		self.final = QAction("final")
		self.menu_for_results = QMenu()
		self.menu_for_results.setStyleSheet('''QMenu{background-color:rgba(72,221,253,255);
			border:2px solid rgba(72,221,253,255);border-top:2px solid black;}
			QMenu.item.selected {color:rgba(72,221,253,255)}
			QMenu:pressed{background-color:lightblue}''')

		self.sub_menu_quiz = self.menu_for_results.addMenu("Quizes")
		self.sub_menu_assignment = self.menu_for_results.addMenu("Assignments")
		self.sub_menu_project = self.menu_for_results.addMenu("Project")
		self.sub_menu_presentation = self.menu_for_results.addMenu("Presentation")
		self.sub_menu_oht1 = self.menu_for_results.addMenu("OHT 1")
		self.sub_menu_oht2 = self.menu_for_results.addMenu("OHT 2")
		self.sub_menu_final = self.menu_for_results.addMenu("Final")
		self.result.setMenu(self.menu_for_results)

		self.sub_menu_quiz.addAction("computer organization and assembly language",lambda:print("hello"))
		self.sub_menu_quiz.addAction("computer organization and assembly language")
		self.sub_menu_quiz.addAction("data structure",lambda:portal.marks_table())
		self.sub_menu_quiz.addAction("data structure lab")
		self.sub_menu_quiz.addAction("graph theory")
		self.sub_menu_quiz.addAction("professional practices")

		self.sub_menu_assignment.addAction("computer organization and assembly language",lambda:print("hello"))
		self.sub_menu_assignment.addAction("computer organization and assembly language")
		self.sub_menu_assignment.addAction("data structure")
		self.sub_menu_assignment.addAction("data structure lab")
		self.sub_menu_assignment.addAction("graph theory")
		self.sub_menu_assignment.addAction("professional practices")


		self.sub_menu_project.addAction("computer organization and assembly language",lambda:print("hello"))
		self.sub_menu_project.addAction("computer organization and assembly language")
		self.sub_menu_project.addAction("data structure")
		self.sub_menu_project.addAction("data structure lab")
		self.sub_menu_project.addAction("graph theory")
		self.sub_menu_project.addAction("professional practices")


		self.sub_menu_presentation.addAction("computer organization and assembly language",lambda:print("hello"))
		self.sub_menu_presentation.addAction("computer organization and assembly language")
		self.sub_menu_presentation.addAction("data structure")
		self.sub_menu_presentation.addAction("data structure lab")
		self.sub_menu_presentation.addAction("graph theory")
		self.sub_menu_presentation.addAction("professional practices")

		self.sub_menu_oht1.addAction("computer organization and assembly language",lambda:print("hello"))
		self.sub_menu_oht1.addAction("computer organization and assembly language")
		self.sub_menu_oht1.addAction("data structure")
		self.sub_menu_oht1.addAction("data structure lab")
		self.sub_menu_oht1.addAction("graph theory")
		self.sub_menu_oht1.addAction("professional practices")

		self.sub_menu_oht2.addAction("computer organization and assembly language")
		self.sub_menu_oht2.addAction("computer organization and assembly language")
		self.sub_menu_oht2.addAction("data structure")
		self.sub_menu_oht2.addAction("data structure lab")
		self.sub_menu_oht2.addAction("graph theory")
		self.sub_menu_oht2.addAction("professional practices")


		self.sub_menu_final.addAction("computer organization and assembly language")
		self.sub_menu_final.addAction("computer organization and assembly language")
		self.sub_menu_final.addAction("data structure")
		self.sub_menu_final.addAction("data structure lab")
		self.sub_menu_final.addAction("graph theory")
		self.sub_menu_final.addAction("professional practices")


		self.formlayout = QVBoxLayout(self)
		self.empty_label = QLabel(self)
		self.empty_label.setLayout(self.formlayout)
		self.empty_label.setFixedSize(220,700)
		self.empty_label.setStyleSheet("border:10px solid #52bdf6;border-style:double;border-right:transparent")
		self.formlayout.addWidget(self.empty_label2)
		self.formlayout.addWidget(self.attendance)
		self.formlayout.addWidget(self.result)
		self.formlayout.addStretch(1)
		self.scrolle = QScrollArea(self)
		self.scrolle.setWidget(self.empty_label)
		self.scrolle.setWidgetResizable(True)
		self.scrolle.setMaximumSize(220,820)
		self.scrolle.setStyleSheet("border:2px solid #52bdf6;background-color:transparent")

		self.data_structure.triggered.connect(lambda:portal.attendance_table())
		
		self.gridlayout.addWidget(self.label,0,0,3,3)
		self.gridlayout.addWidget(self.scrolle,0,0,3,1)
	
	def attendance_table(self):
		self.attendance.setText("assembly language..")
		self.tableWidget = QTableWidget(self)
		self.tableWidget.verticalHeader().setVisible(False)	
		self.gridlayout.addWidget(self.tableWidget,1,1,2,3)
		self.tableWidget.setMaximumSize(1500,800)
		self.tableWidget.verticalHeader().setVisible(False)
		self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
		self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
		
		self.layout_for_attendance_edit = QHBoxLayout(self)

		self.attendance_label = QLabel("Your Attendance",self)
		self.attendance_label.setStyleSheet("color:black;background-color:white")
		self.attendance_label.setAlignment(Qt.AlignCenter)
		self.attendance_label.setFont(QFont("arial",12))
		self.attendance_label.setMaximumSize(1500,50)
		self.gridlayout.addWidget(self.attendance_label,0,1,1,3)
		getdata = RequestAndResponse("http://127.0.0.1:8000/faculty attendance/")
		result = getdata.get_response()
		print(result)
		ids,date,name,rollno,status= [],[],[],[],[]
		for i in range (len(result)):
			if result[i]['regno'] == 210201073:
				ids.append(result[i]['id'])
				date.append(result[i]['date'])
				name.append(result[i]['name'])
				rollno.append(result[i]['regno'])
				status.append(result[i]['status'])
		maxrow = 50
		maxcol = 5
		self.tableWidget.setRowCount(maxrow) 
		self.tableWidget.setColumnCount(maxcol)  
		currentRowCount = -1
		for i in range(len(ids)):
			currentRowCount += 1
			print("currentRowCount",currentRowCount)
			self.tableWidget.setItem(currentRowCount, 0, QTableWidgetItem(str(i+1)))
			self.tableWidget.setItem(currentRowCount, 1, QTableWidgetItem(str(date[i])))
			self.tableWidget.setItem(currentRowCount, 2, QTableWidgetItem(str(name[i])))
			self.tableWidget.setItem(currentRowCount, 3, QTableWidgetItem(str(rollno[i])))
			self.tableWidget.setItem(currentRowCount, 4, QTableWidgetItem(str(status[i])))


		
		def QString(a):
  			return (a)
		self.tableWidget.setHorizontalHeaderLabels(QString("Sr;Date;Name;Rollno;Status").split(";"))

			

	def marks_table(self):
		self.markstable = QTableWidget(self)
		self.markstable.horizontalHeader().setStretchLastSection(True)
		self.markstable.verticalHeader().setVisible(False)	
		self.gridlayout.addWidget(self.markstable,1,1,2,3)
		self.markstable.setMaximumSize(1500,800)
		self.markstable.verticalHeader().setVisible(False)
		self.markstable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
		self.markstable.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.layout_for_attendance_edit = QHBoxLayout(self)

		self.attendance_label = QLabel("Your Marks",self)
		self.attendance_label.setStyleSheet("color:black;background-color:white")
		self.attendance_label.setAlignment(Qt.AlignCenter)
		self.attendance_label.setFont(QFont("arial",12))
		self.attendance_label.setMaximumSize(1500,50)
		self.gridlayout.addWidget(self.attendance_label,0,1,1,3)
		getdata = RequestAndResponse("http://127.0.0.1:8000/quiz marks/")
		result = getdata.get_response()
		print(result)
		ids,date,name,rollno,obtainnumber,maximumnumber= [],[],[],[],[],[]
		for i in range (len(result)):
			if result[i]['typeofexam'] == "Quiz":
				ids.append(result[i]['id'])
				date.append(result[i]['date'])
				name.append(result[i]['name'])
				rollno.append(result[i]['rollno'])
				maximumnumber.append(result[i]['maxnum'])
				obtainnumber.append(result[i]['obtainnum'])

		maxrow = 50
		maxcol = 6
		self.markstable.setRowCount(maxrow) 
		self.markstable.setColumnCount(maxcol)  
		currentRowCount = -1
		for i in range(len(ids)):
			currentRowCount += 1
			print("currentRowCount",currentRowCount)
			self.markstable.setItem(currentRowCount, 0, QTableWidgetItem(str(i+1)))
			self.markstable.setItem(currentRowCount, 1, QTableWidgetItem(str(date[i])))
			self.markstable.setItem(currentRowCount, 2, QTableWidgetItem(str(name[i])))
			self.markstable.setItem(currentRowCount, 3, QTableWidgetItem(str(rollno[i])))
			self.markstable.setItem(currentRowCount, 4, QTableWidgetItem(str(maximumnumber[i])))
			self.markstable.setItem(currentRowCount, 5, QTableWidgetItem(str(obtainnumber[i])))

		
		
		def QString(a):
  			return (a)
		self.markstable.setHorizontalHeaderLabels(QString("Sr;Date;Name;Rollno;Maximum Marks;Obtain").split(";"))

			
	def going_back_to_dashboard(self):
		try:
			obj2 = RequestAndResponse("http://127.0.0.1:8000/user/")
			obj2.post_data({"user":"210201073"})	
			QApplication.processEvents()
			from dashboard import DashBoard
			dashboard.setParent(None)
			dashboard.deleteLater()
			
		except:
			print("Allah bhalla krsi")

			
app = QApplication(sys.argv)
portal = Portal()
portal.show()  
app.exec()
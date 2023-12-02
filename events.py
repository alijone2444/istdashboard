import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
# import the time module
import time
class Events(QMainWindow):
	def __init__(self):
		super().__init__()
		self.resize(1000,640)
		self.Widget = QWidget(self)
		self.setCentralWidget(self.Widget)
		self.layout = QGridLayout(self.Widget)
		self.setStyleSheet("QScrollBar{ background-color: transparent}QMainWindow{background-color:#a7573a}")

		self.background = QLabel(self)
		pixmap = QPixmap('evback')
		self.background.setPixmap(pixmap)
		self.background.setScaledContents(True)
		
		self.back_btn = QPushButton("",self)
		self.back_btn.setFixedSize(130,70)
		self.back_btn.setStyleSheet('''QPushButton{background-color: transparent;border-radius:35%;border:2px solid transparent;}''')	
		self.back_btn.clicked.connect(lambda:(print("hello")))
		self.hv1 = QGridLayout(self)
		self.empty3 = QLabel(self)	
		self.empty3.setMaximumSize(150,100)	
		self.empty3.setStyleSheet('''QLabel{background-color: transparent;border-radius:35%;border:2px solid transparent;}
		QLabel:hover{background-color :#a7573a;}''')	
		self.empty3.setLayout(self.hv1)
		self.movie2 = QMovie("backbtn.gif")
		self.empty3.setMovie(self.movie2)
		self.hv1.addWidget(self.back_btn)
		self.empty3.setScaledContents(True)
		self.movie2.setSpeed(200)
		self.movie2.start()

		self.calendar = QCalendarWidget(self)
		self.calendar.setMaximumSize(400,150)
		self.calendar.setStyleSheet('''QMenu {
    background: #a7573a;
}
QMenu::item:selected {
    background: yellow;
    border-radius: 2px;
}
#qt_calendar_navigationbar {
    background: #a7573a
}
QCalendar{background-color:#a7573a}
QCalendarWidget QTableView
{
    background-color:white;
}''')
		self.hv = QHBoxLayout(self)
		self.label1 = QLabel(self)
		self.label1.setLayout(self.hv)
		pixmap2 = QPixmap('even.png')
		self.label1.setPixmap(pixmap2)
		self.label1.setScaledContents(True)
		self.label1.setMaximumSize(360,150)


		string = ''' ->Freelancing by Nafay Jawed | 2pm | (10/01/23) | Auditorium\n-> Raashan Drive | 9am | (14/01/23) | Auditorium\n-> Qawali Night | 5pm | (15/01/23) | Raza block\n-> Signal Traffic |11am| (20/01/23) | Block 6'''

		self.empty1 = QLabel(self)
		self.empty1.setText(string)
		self.empty1.setStyleSheet("background-color:#fcf7a3;border:20px transparent")
		self.empty1.setFont(QFont("arial", 15,))
		self.empty1.setFixedSize(1500,650)
		self.empty1.setAlignment(Qt.AlignTop)
		self.empty1.setWordWrap(True)
		self.empty = QScrollArea(self)
		self.empty.setMaximumSize(1500,450)
		self.empty.setWidget(self.empty1)
        
		self.label = QLabel("None",self)
		self.label.setStyleSheet("background-color:white;border-radius:30%;border:10px solid white")
		self.label.setMaximumSize(380,80)
		self.label.setAlignment(Qt.AlignCenter)
		self.movie = QMovie("rain.gif")
		self.label.setMovie(self.movie)
		self.label.setScaledContents(True)
		self.movie.setSpeed(200)
		self.movie.start()

		self.lcdNumber = QLabel("up next:",self)
		self.lcdNumber.setStyleSheet("color: red;background-color:white;")
		self.lcdNumber.setMaximumSize(200,60)
		self.lcdNumber.setFont(QFont("arial",10))
		self.lcdNumber.setWordWrap(True)
		self.lcdNumber_seconds = QLabel("seconds",self)
		self.lcdNumber_seconds.setStyleSheet("color: black;background-color:white;padding-bottom:5px")
		self.lcdNumber_seconds.setMaximumSize(200,30)
		self.lcdNumber_seconds.setFont(QFont("ariel",24))
		self.hv2 = QVBoxLayout(self)
		self.empty4 = QLabel(self)
		self.empty4.setLayout(self.hv2)
		self.hv2.addWidget(self.lcdNumber_seconds)
		self.hv2.addWidget(self.lcdNumber)

		self.lcdNumber_seconds2 = QLabel(self)
		self.lcdNumber_seconds2.setStyleSheet("color: black;background-color:white;padding-bottom:5px")
		self.lcdNumber_seconds2.setMaximumSize(200,30)
		self.lcdNumber_seconds2.setFont(QFont("ariel",24))

		self.remaining = QLabel("Remaining Time:",self)
		self.remaining.setStyleSheet("color: black;background-color:white;padding-bottom:5px")
		self.remaining.setMaximumSize(200,30)
		self.remaining.setFont(QFont("ariel",12))
		
		self.hv3 = QVBoxLayout(self)
		self.empty5 = QLabel(self)
		self.empty5.setLayout(self.hv3)
		self.hv3.addWidget(self.remaining)
		self.hv3.addWidget(self.lcdNumber_seconds2)

		self.layout.addWidget(self.background,0,0,5,9)
		self.layout.addWidget(self.empty3,0,0,1,1)
		self.layout.addWidget(self.empty4,2,0,1,1)
		self.layout.addWidget(self.calendar,0,7,1,2)
		self.layout.addWidget(self.label,0,3,1,4)
		self.layout.addWidget(self.label1,0,3,1,6)
		self.layout.addWidget(self.empty,2,1,3,7)	
		self.layout.addWidget(self.empty5,2,8,1,1)	


		queue = ["Freelancing by Nafay Javed |2|pm ","Raashan Drive |9|am ","> Qawali Night |5|pm ","Signal Traffic |11|am"]
		self.lcdNumber.setText("next: "+queue[0])
		y = ""
		for i in queue:
			for j in i:
				x = i.split("|")
				if x[1] not in y:
					y = y+","+x[1]
		
		timequeue = y.split(",")
		timequeue.pop(0)
		print(timequeue)

		def showtime():
			current_time = QTime.currentTime()
			label_time = current_time.toString('hh:mm:ss')
			self.lcdNumber_seconds.setText(label_time)
			print("hour:",current_time.hour())
			print("minute:",current_time.minute())

		timer = QTimer(self)
		timer.timeout.connect(lambda:showtime())  
		timer.start(1000)

		current_time = QTime.currentTime()
		label_time = current_time.hour() - int(timequeue[0])
		label = label_time * 3600
		self.countdown=label
		def showremaining2():    

			if self.countdown == 0:
				timer2.stop()
				timequeue.pop(0)
				queue.pop(0)
			print("hi")
			self.countdown = self.countdown - 1
			self.lcdNumber_seconds2.setText(str(self.countdown)+"'s")

		timer2 = QTimer(self)
		timer2.timeout.connect(lambda:showremaining2())  
		timer2.start(1000)


app = QApplication([])
dashboard = Events()
dashboard.show()
app.exec()

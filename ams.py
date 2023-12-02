from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

# Subclass QMainWindow to customize your application's main window
class Feedback(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1000,640)
        self.setWindowTitle("AMS")
        self.widget = QWidget(self)
        self.setCentralWidget(self.widget)
        self.gridlayout =QGridLayout(self.widget)        
        self.setStyleSheet( '''QScrollBar{ background-color: black}''')

        self.vbox = QVBoxLayout(self)
        self.empty1 = QLabel(self)
        self.empty1.setMaximumSize(800,600)
        self.empty1.setLayout(self.vbox)

        vbox2 = QVBoxLayout(self)
        vbox3 = QVBoxLayout(self)
        vbox4 = QVBoxLayout(self)
        self.feedbacktopics = QPushButton("total feedback topics ",self)
        self.feedbacktopics.setStyleSheet('''QPushButton{background-color:#606060;border-radius:10%;border:1px solid black}
            QPushButton:hover{background-color:#404040}
            QPushButton:pressed{padding-top:5px}''')
        self.feedbacktopics.setMaximumSize(500,200)
        self.feedbacktopics.setFont(QFont("arial",12))
        self.feedbacktopics.setLayout(vbox2)
        self.feedbacktopics.clicked.connect(self.feedbackquestions)
        self.feedbacktopics_label = QLabel("7",self)
        self.feedbacktopics_label.setAlignment(Qt.AlignCenter)
        self.feedbacktopics_label.setStyleSheet("border:2px solid transparent")
        vbox2.addStretch(1)
        vbox2.addWidget(self.feedbacktopics_label)
        self.feedbackanswered = QPushButton("feedback answered",self)
        self.feedbackanswered.setStyleSheet('''QPushButton{background-color:#A0A0A0;border-radius:10%;border:1px solid black}
            QPushButton:hover{background-color:#C0C0C0}
            QPushButton:pressed{padding-top:5px}''')
        self.feedbackanswered.setMaximumSize(500,200)
        self.feedbackanswered.setFont(QFont("arial",12))
        self.feedbackanswered.setLayout(vbox3)
        self.feedbackanswered_label = QLabel("0",self)
        self.feedbackanswered_label.setAlignment(Qt.AlignCenter)
        self.feedbackanswered_label.setStyleSheet("border:2px solid transparent")
        vbox3.addStretch(1)
        vbox3.addWidget(self.feedbackanswered_label)       
        self.feedbackunanswered = QPushButton("feedback unanswered",self)
        self.feedbackunanswered.setStyleSheet('''QPushButton{background-color:white;border-radius:10%;border:1px solid black}
            QPushButton:hover{background-color:#E0E0E0}
            QPushButton:pressed{padding-top:5px}''')
        self.feedbackunanswered.setMaximumSize(500,200)
        self.feedbackunanswered.setFont(QFont("arial",12))
        self.feedbackunanswered.setLayout(vbox4)
        self.feedbackunanswered_label = QLabel("7",self)
        self.feedbackunanswered_label.setAlignment(Qt.AlignCenter)
        self.feedbackunanswered_label.setStyleSheet("border:2px solid transparent")
        vbox4.addStretch(1)
        vbox4.addWidget(self.feedbackunanswered_label)       
        self.vbox.addWidget(self.feedbacktopics)
        self.vbox.addWidget(self.feedbackanswered)
        self.vbox.addWidget(self.feedbackunanswered)

        self.label = QLabel("None",self)
        pixmap = QPixmap('feedbackbackground')
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)
        self.label.setMaximumSize(1500,840)
        self.label.setAlignment(Qt.AlignCenter)
        
        self.gridlayout.addWidget(self.label,0,0,8,6)
        
        self.photo = QLabel(self)
        self.photo.setStyleSheet("border:2px solid transparent")
        self.photo.setFixedSize(100,100)
        self.movie = QMovie("feedback.gif")
        self.photo.setMovie(self.movie)
        self.photo.setScaledContents(True)
        self.movie.setSpeed(200)
        self.movie.start()

        self.btn_back = QPushButton("<",self)
        self.btn_back.setFixedSize(50,50)
        self.btn_back.setStyleSheet('''QPushButton{background-color:#C0C0C0;border-radius:25%;border:1px solid black}
            QPushButton:hover{background-color:white}
            QPushButton:pressed{padding-right:5px}''')



        self.options = QPushButton(self)
        self.options.setFixedSize(50,50)
        self.options.setStyleSheet('''QPushButton{background-image:url(threedots);border:2px solid white;border-radius:25%}
            QPushButton:hover{border:2px solid lightgrey}
            QPushButton:pressed{border:4px solid lightgrey}
            QPushButton::menu-indicator { image: none; }''')

        self.submit = QAction("submit",self)
        self.menu = QMenu()
        self.menu.setStyleSheet('''QMenu{background-color:darkgrey;}
            QMenu:item{color:black;}
            QMenu:item:selected{color:white;}
            QMenu:pressed{background-color:lightgrey}''')
        self.menu.addAction(self.submit)
        self.options.setMenu(self.menu)
        self.submit.triggered.connect(self.getfeedback)

        hbox1 = QHBoxLayout(self)
        self.whiteline = QLabel(self)
        self.whiteline.setStyleSheet("border:2px solid black")
        self.whiteline.setLayout(hbox1)
        
        hbox1.addWidget(self.btn_back)
        hbox1.addStretch(1)
        hbox1.addWidget(self.photo)
        hbox1.addStretch(1)
        hbox1.addWidget(self.options)

        self.gridlayout.addWidget(self.empty1,2,2,3,2)
        self.gridlayout.addWidget(self.whiteline,0,0,1,6)

    def feedbackquestions(self):
        self.blur_effect = QGraphicsBlurEffect()
        self.blur_effect.setBlurRadius(5)
        self.label.setGraphicsEffect(self.blur_effect)
        self.empty1.hide()
        self.questions_grid = QGridLayout(self)
        self.hbox_for_teachers= QHBoxLayout(self)
        self.empty2 = QLabel(self)
        self.empty2.setLayout(self.hbox_for_teachers)
        self.teacher_name = QLabel("Tufail Shah",self)
        self.teacher_name.setFont(QFont("arial",15))
        self.teacher_name.setAlignment(Qt.AlignVCenter)
        
        self.teacher_photo = QLabel(self)
        self.teacher_photo.setScaledContents(True)
        self.teacher_photo.setMaximumSize(50,50)
        self.teacher_photo.setStyleSheet("QLabel{background-image:url(sirtufail);border-radius:20%}")
        self.hbox_for_teachers.addWidget(self.teacher_photo)
        self.hbox_for_teachers.addWidget(self.teacher_name)
        self.questions_empty_label = QLabel(self)
        self.questions_empty_label.setFixedSize(1000,540)
        self.questions_empty_label.setFont(QFont("Didot",10))
        self.questions_empty_label.setLayout(self.questions_grid)
        self.quesions = QLabel("Give the following answer and be authentic.",self)
        self.quesions.setFont(QFont("Didot",13))
        self.quesions.setStyleSheet("border:1px solid lightgrey")

        self.scroll = QScrollArea(self)
        self.scroll.setWidget(self.questions_empty_label)
        self.scroll.setWidgetResizable(True)
        self.scroll.setStyleSheet("background-color:transparent")

        self.empty3 = QLabel(self)
        self.bad = QLabel("Disagree",self)
        self.normal = QLabel("Neutral",self)
        self.good = QLabel("Agree",self)
        self.verygood = QLabel("Strongly agree",self)
        

        self.q1 = QLabel("1.Course objectives were understandable for me.",self)
        self.q1.setFont(QFont("arial",10))
        self.q2 = QLabel("2.Lectures ,tests and assignments were effective to achieve course learning outcomes.",self)
        self.q2.setFont(QFont("arial",10))
        self.q3 = QLabel("3.Cheating was easy during exam ",self)
        self.q3.setFont(QFont("arial",10))
        self.q4 = QLabel("4.Instructor was strict ",self)
        self.q4.setFont(QFont("arial",10))
        self.q5 = QLabel("5.Instructor was regular ",self)
        self.q5.setFont(QFont("arial",10))
        self.q6 = QLabel("6.The instructor shows interest in helping student to learn",self)
        self.q6.setFont(QFont("arial",10))
        self.q7 = QLabel("7.The course was benifitial ",self)
        self.q7.setFont(QFont("arial",10))
        self.q8 = QLabel("8.The course gave me the confidence to work in subjective areas.",self)
        self.q8.setFont(QFont("arial",10))
        self.q9 = QLabel("9.The instructional material increased my knowlege and skills in the subjective manner.",self)
        self.q9.setFont(QFont("arial",10))
        self.q10 = QLabel("10.The instructor was well prepared to deliver the contents effectively .",self)
        self.q10.setFont(QFont("arial",10))
        bg1 = QButtonGroup(self)
        self.raioC1R1 = QRadioButton(self)
        self.raioC2R1 = QRadioButton(self)
        self.raioC3R1 = QRadioButton(self)
        self.raioC4R1 = QRadioButton(self)
        bg1.addButton(self.raioC1R1)
        bg1.addButton(self.raioC2R1)
        bg1.addButton(self.raioC3R1)
        bg1.addButton(self.raioC4R1)
        
        bg2 = QButtonGroup(self)
        self.raioC1R2 = QRadioButton(self)
        self.raioC2R2 = QRadioButton(self)
        self.raioC3R2 = QRadioButton(self)
        self.raioC4R2 = QRadioButton(self)
        bg2.addButton(self.raioC1R2)
        bg2.addButton(self.raioC2R2)
        bg2.addButton(self.raioC3R2)
        bg2.addButton(self.raioC4R2)

        bg3 = QButtonGroup(self)
        self.raioC1R3 = QRadioButton(self)
        self.raioC2R3 = QRadioButton(self)
        self.raioC3R3 = QRadioButton(self)
        self.raioC4R3 = QRadioButton(self)
        bg3.addButton(self.raioC1R3)
        bg3.addButton(self.raioC2R3)
        bg3.addButton(self.raioC3R3)
        bg3.addButton(self.raioC4R3)


        bg4 = QButtonGroup(self)
        self.raioC1R4 = QRadioButton(self)
        self.raioC2R4 = QRadioButton(self)
        self.raioC3R4 = QRadioButton(self)
        self.raioC4R4 = QRadioButton(self)
        bg4.addButton(self.raioC1R4)
        bg4.addButton(self.raioC2R4)
        bg4.addButton(self.raioC3R4)
        bg4.addButton(self.raioC4R4)

        bg5 = QButtonGroup(self)
        self.raioC1R5 = QRadioButton(self)
        self.raioC2R5 = QRadioButton(self)
        self.raioC3R5 = QRadioButton(self)
        self.raioC4R5 = QRadioButton(self)
        bg5.addButton(self.raioC1R5)
        bg5.addButton(self.raioC2R5)
        bg5.addButton(self.raioC3R5)
        bg5.addButton(self.raioC4R5)

        bg6 = QButtonGroup(self)
        self.raioC1R6 = QRadioButton(self)
        self.raioC2R6 = QRadioButton(self)
        self.raioC3R6 = QRadioButton(self)
        self.raioC4R6 = QRadioButton(self)
        bg6.addButton(self.raioC1R6)
        bg6.addButton(self.raioC2R6)
        bg6.addButton(self.raioC3R6)
        bg6.addButton(self.raioC4R6)

        bg7 = QButtonGroup(self)
        self.raioC1R7 = QRadioButton(self)
        self.raioC2R7 = QRadioButton(self)
        self.raioC3R7 = QRadioButton(self)
        self.raioC4R7 = QRadioButton(self)
        bg7.addButton(self.raioC1R7)
        bg7.addButton(self.raioC2R7)
        bg7.addButton(self.raioC3R7)
        bg7.addButton(self.raioC4R7)

        bg8 = QButtonGroup(self)
        self.raioC1R8 = QRadioButton(self)
        self.raioC2R8 = QRadioButton(self)
        self.raioC3R8 = QRadioButton(self)
        self.raioC4R8 = QRadioButton(self)
        bg8.addButton(self.raioC1R8)
        bg8.addButton(self.raioC2R8)
        bg8.addButton(self.raioC3R8)
        bg8.addButton(self.raioC4R8)

        bg9 = QButtonGroup(self)
        self.raioC1R9 = QRadioButton(self)
        self.raioC2R9 = QRadioButton(self)
        self.raioC3R9 = QRadioButton(self)
        self.raioC4R9 = QRadioButton(self)
        bg9.addButton(self.raioC1R9)
        bg9.addButton(self.raioC2R9)
        bg9.addButton(self.raioC3R9)
        bg9.addButton(self.raioC4R9)

        bg10 = QButtonGroup(self)
        self.raioC1R10 = QRadioButton(self)
        self.raioC2R10 = QRadioButton(self)
        self.raioC3R10 = QRadioButton(self)
        self.raioC4R10 = QRadioButton(self)
        bg10.addButton(self.raioC1R10)
        bg10.addButton(self.raioC2R10)
        bg10.addButton(self.raioC3R10)
        bg10.addButton(self.raioC4R10)
        
        
        
        self.questions_grid.addWidget(self.quesions,0,0,2,6)
        self.questions_grid.addWidget(self.empty3,0,1,2,2)
        self.questions_grid.addWidget(self.bad,0,2,2,1)
        self.questions_grid.addWidget(self.normal,0,3,2,1)
        self.questions_grid.addWidget(self.good,0,4,2,1)
        self.questions_grid.addWidget(self.verygood,0,5,2,1)
        self.questions_grid.addWidget(self.q1,2,0,2,1)
        self.questions_grid.addWidget(self.q2,3,0,2,1)
        self.questions_grid.addWidget(self.q3,4,0,2,1)
        self.questions_grid.addWidget(self.q4,5,0,2,1)
        self.questions_grid.addWidget(self.q5,6,0,2,1)
        self.questions_grid.addWidget(self.q6,7,0,2,1)
        self.questions_grid.addWidget(self.q7,8,0,2,1)
        self.questions_grid.addWidget(self.q8,9,0,2,1)
        self.questions_grid.addWidget(self.q9,10,0,2,1)
        self.questions_grid.addWidget(self.q10,11,0,2,1)

        self.questions_grid.addWidget(self.raioC1R1,2,2,2,1)
        self.questions_grid.addWidget(self.raioC2R1,2,3,2,1)
        self.questions_grid.addWidget(self.raioC3R1,2,4,2,1)
        self.questions_grid.addWidget(self.raioC4R1,2,5,2,1)

        self.questions_grid.addWidget(self.raioC1R2,3,2,2,1)
        self.questions_grid.addWidget(self.raioC2R2,3,3,2,1)
        self.questions_grid.addWidget(self.raioC3R2,3,4,2,1)
        self.questions_grid.addWidget(self.raioC4R2,3,5,2,1)

        self.questions_grid.addWidget(self.raioC1R3,4,2,2,1)
        self.questions_grid.addWidget(self.raioC2R3,4,3,2,1)
        self.questions_grid.addWidget(self.raioC3R3,4,4,2,1)
        self.questions_grid.addWidget(self.raioC4R3,4,5,2,1)

        self.questions_grid.addWidget(self.raioC1R4,5,2,2,1)
        self.questions_grid.addWidget(self.raioC2R4,5,3,2,1)
        self.questions_grid.addWidget(self.raioC3R4,5,4,2,1)
        self.questions_grid.addWidget(self.raioC4R4,5,5,2,1)

        self.questions_grid.addWidget(self.raioC1R5,6,2,2,1)
        self.questions_grid.addWidget(self.raioC2R5,6,3,2,1)
        self.questions_grid.addWidget(self.raioC3R5,6,4,2,1)
        self.questions_grid.addWidget(self.raioC4R5,6,5,2,1)

        self.questions_grid.addWidget(self.raioC1R6,7,2,2,1)
        self.questions_grid.addWidget(self.raioC2R6,7,3,2,1)
        self.questions_grid.addWidget(self.raioC3R6,7,4,2,1)
        self.questions_grid.addWidget(self.raioC4R6,7,5,2,1)

        self.questions_grid.addWidget(self.raioC1R7,8,2,2,1)
        self.questions_grid.addWidget(self.raioC2R7,8,3,2,1)
        self.questions_grid.addWidget(self.raioC3R7,8,4,2,1)
        self.questions_grid.addWidget(self.raioC4R7,8,5,2,1)

        self.questions_grid.addWidget(self.raioC1R8,9,2,2,1)
        self.questions_grid.addWidget(self.raioC2R8,9,3,2,1)
        self.questions_grid.addWidget(self.raioC3R8,9,4,2,1)
        self.questions_grid.addWidget(self.raioC4R8,9,5,2,1)

        self.questions_grid.addWidget(self.raioC1R9,10,2,2,1)
        self.questions_grid.addWidget(self.raioC2R9,10,3,2,1)
        self.questions_grid.addWidget(self.raioC3R9,10,4,2,1)
        self.questions_grid.addWidget(self.raioC4R9,10,5,2,1)

        self.questions_grid.addWidget(self.raioC1R10,11,2,2,1)
        self.questions_grid.addWidget(self.raioC2R10,11,3,2,1)
        self.questions_grid.addWidget(self.raioC3R10,11,4,2,1)
        self.questions_grid.addWidget(self.raioC4R10,11,5,2,1)

        self.gridlayout.addWidget(self.scroll,2,0,11,6)
        self.gridlayout.addWidget(self.empty2,1,0,1,6)

    def getfeedback(self):
        values = []
        if self.raioC1R1.isChecked() == True:
            values.append(0)
        if self.raioC2R1.isChecked() == True:
            values.append(1)
        if self.raioC3R1.isChecked() == True:
            values.append(2)
        if self.raioC4R1.isChecked() == True:
            values.append(3)
      
        if self.raioC1R2.isChecked() == True:
            values.append(0)
        if self.raioC2R2.isChecked() == True:
            values.append(1)
        if self.raioC3R2.isChecked() == True:
            values.append(2)
        if self.raioC4R2.isChecked() == True:
            values.append(3)

        if self.raioC1R3.isChecked() == True:
            values.append(3)
        if self.raioC2R3.isChecked() == True:
            values.append(2)
        if self.raioC3R3.isChecked() == True:
            values.append(0)
        if self.raioC4R3.isChecked() == True:
            values.append(0)
       
        if self.raioC1R4.isChecked() == True:
            values.append(1)
        if self.raioC2R4.isChecked() == True:
            values.append(1)
        if self.raioC3R4.isChecked() == True:
            values.append(2)
        if self.raioC4R4.isChecked() == True:
            values.append(2)

        if self.raioC1R5.isChecked() == True:
            values.append(0)
        if self.raioC2R5.isChecked() == True:
            values.append(1)
        if self.raioC3R5.isChecked() == True:
            values.append(2)
        if self.raioC4R5.isChecked() == True:
            values.append(3)


        if self.raioC1R6.isChecked() == True:
            values.append(0)
        if self.raioC2R6.isChecked() == True:
            values.append(1)
        if self.raioC3R6.isChecked() == True:
            values.append(2)
        if self.raioC4R6.isChecked() == True:
            values.append(3)

        if self.raioC1R7.isChecked() == True:
            values.append(0)
        if self.raioC2R7.isChecked() == True:
            values.append(1)
        if self.raioC3R7.isChecked() == True:
            values.append(2)
        if self.raioC4R7.isChecked() == True:
            values.append(3)
        
        if self.raioC1R8.isChecked() == True:
            values.append(0)
        if self.raioC2R8.isChecked() == True:
            values.append(1)
        if self.raioC3R8.isChecked() == True:
            values.append(2)
        if self.raioC4R8.isChecked() == True:
            values.append(3)

        if self.raioC1R9.isChecked() == True:
            values.append(0)
        if self.raioC2R9.isChecked() == True:
            values.append(1)
        if self.raioC3R9.isChecked() == True:
            values.append(2)
        if self.raioC4R9.isChecked() == True:
            values.append(3)
       
        if self.raioC1R10.isChecked() == True:
            values.append(0)
        if self.raioC2R10.isChecked() == True:
            values.append(1)
        if self.raioC3R10.isChecked() == True:
            values.append(2)
        if self.raioC4R10.isChecked() == True:
            values.append(3)
        self.feedbackanswered_label.setText("1")
        self.feedbackunanswered_label.setText("6")
        self.scroll.hide()
        self.empty1.show()
        score = sum(values)
        percentage = score/30*100
        print(percentage)



app = QApplication(sys.argv)

ams = Feedback()
ams.show()

app.exec()
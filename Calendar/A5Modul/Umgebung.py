
import sys
from PyQt5.QtWidgets import *
 
def main():
    
    app = QApplication(sys.argv)
    tabs = QTabWidget()
    
    # Create tabs
    tab1 = QWidget() 
    tab2 = QWidget()
    tab3 = QWidget()
    tab4 = QWidget()
    tab5 = QWidget()
    tab6 = QWidget()
    tab7 = QWidget()
    tab8 = QWidget()
    tab9 = QWidget()
    tab10 = QWidget()
    tab11 = QWidget()
    tab12 = QWidget() 
    
 
    # Resize width and height
    tabs.resize(500, 300)
    
    # Set layout of first tab
    vBoxlayout = QVBoxLayout()
    pushButton1 =QPushButton("Start")
    pushButton2 =QPushButton("Settings")
    pushButton3 =QPushButton("Stop")
    vBoxlayout.addWidget(pushButton1)
    vBoxlayout.addWidget(pushButton2)
    vBoxlayout.addWidget(pushButton3)
    tab1.setLayout(vBoxlayout)   
     
    # Add tabs
    tabs.addTab(tab1,"Jan")
    tabs.addTab(tab2,"Feb")
    tabs.addTab(tab3,"Mar")
    tabs.addTab(tab4,"Apr") 
    tabs.addTab(tab5,"Mai") 
    tabs.addTab(tab6,"Jun") 
    tabs.addTab(tab7,"Jul")
    tabs.addTab(tab8,"Aug") 
    tabs.addTab(tab9,"Sep")
    tabs.addTab(tab10,"Okt")
    tabs.addTab(tab11,"Nov")
    tabs.addTab(tab12,"Dez") 
    
    
    # Set title and show
    tabs.setWindowTitle('Jahreskalender')
    tabs.show()
    
    sys.exit(app.exec_())
    
 
 
if __name__ == '__main__':
    main()
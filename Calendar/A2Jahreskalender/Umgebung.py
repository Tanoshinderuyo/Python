import calfunctions
import sys
from PyQt5.QtWidgets import *
#from PyQt5.QtCore import * 
 
def kalender(jahr):
    
    #Listen für schnellen Zugrif auf Monatsname und Wochentag
    monatsname = ['Januar','Februar','März','April','Mai','Juni','Juli','August','September','Oktober','November','Dezember']
    tagnamelang = ['Sonntag','Montag','Dienstag','Mittwoch','Donnerstag','Freitag','Samstag']
    tagname = ['So','Mo','Di','Mi','Do','Fr','Sa']
    
    app = QApplication(sys.argv)
    fenster = QTabWidget()	#Fenstergenerierung
    
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
    fenster.resize(750, 250)	#Fensterresizing
    
    # Add fenster
    fenster.addTab(tab1,"Jan")
    fenster.addTab(tab2,"Feb")
    fenster.addTab(tab3,"Mar")
    fenster.addTab(tab4,"Apr") 
    fenster.addTab(tab5,"Mai") 
    fenster.addTab(tab6,"Jun") 
    fenster.addTab(tab7,"Jul")
    fenster.addTab(tab8,"Aug") 
    fenster.addTab(tab9,"Sep")
    fenster.addTab(tab10,"Okt")
    fenster.addTab(tab11,"Nov")
    fenster.addTab(tab12,"Dez")
    
    #TAB 1 ========================================================================================#
    # Set layout of first tab
    vBoxlayout = QVBoxLayout()
    table = QTableWidget()
    tableItem = QTableWidgetItem()
    
    # initiate table
    #table.setWindowTitle("QTableWidget Example @pythonspot.com")
    #table.resize(400, 275)
    table.setRowCount(5)
    table.setColumnCount(7)
    
    # set labels
    table.setHorizontalHeaderLabels(str("Mo;Di;Mi;Do;Fr;Sa;So;").split(";"))
    table.setVerticalHeaderLabels(str("I;II;III;IV;V").split(";"))
    vBoxlayout.addWidget(table)
    tab1.setLayout(vBoxlayout) 
     
     
    
    #TAB 2 ========================================================================================#
    #TAB 3 ========================================================================================#
    #TAB 4 ========================================================================================#
    #TAB 5 ========================================================================================#
    #TAB 6 ========================================================================================#
    #TAB 7 ========================================================================================#
    #TAB 8 ========================================================================================#
    #TAB 9 ========================================================================================#
    #TAB 10 ========================================================================================#
    #TAB 11 ========================================================================================#
    #TAB 12 ========================================================================================#
    
    #========================================================================================#
    # Set title and show
    fenster.setWindowTitle('Jahreskalender '+str(jahr))
    fenster.show()
    return app.exec_()
    
def	main():
	jahr = int(input("Bitte geben Sie ein Jahr ein: "))
	kalender(jahr)
 
 
if __name__ == '__main__':
    main()
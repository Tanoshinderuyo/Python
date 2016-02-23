import calfunctions
import sys
from PyQt5.QtWidgets import * 
 
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
	vBoxlayout1 = QVBoxLayout()
	table = QTableWidget()
	#table.resizeColumnsToContents()
	#table.resizeRowsToContents()
	table.setRowCount(6)
	table.setColumnCount(7)
	
	# set labels
	table.setHorizontalHeaderLabels(str("Mo;Di;Mi;Do;Fr;Sa;So;").split(";"))
	table.setVerticalHeaderLabels(str("I;II;III;IV;V;VI").split(";"))
	vBoxlayout1.addWidget(table)
	tab1.setLayout(vBoxlayout1) 
	
	monat = 1
	reihe = 0
	monatlang=calfunctions.monatslaenge(jahr,monat)
	w = calfunctions.wochentag(jahr,monat,1)	
	erster = QTableWidgetItem("1")
	if w == 0:
		table.setItem(reihe, 6, erster)
		reihe += 1
	else:
		table.setItem(reihe, w-1, erster)
	
	zaehler = 2
	for tag in range(2,monatlang+1,1):
		w = calfunctions.wochentag(jahr,monat,tag)
		if(w==0):
			newitem = QTableWidgetItem(str(zaehler))
			table.setItem(reihe,6,newitem)
			reihe+=1
		elif (w==1):
			newitem = QTableWidgetItem(str(zaehler))
			table.setItem(reihe,0,newitem)
		else:
			newitem = QTableWidgetItem(str(zaehler))
			table.setItem(reihe,(w-1),newitem)
		zaehler+=1
	
	#TAB 2 ========================================================================================#
	vBoxlayout2 = QVBoxLayout()
	table2 = QTableWidget()
	#table.resizeColumnsToContents()
	#table.resizeRowsToContents()
	table2.setRowCount(6)
	table2.setColumnCount(7)
	
	# set labels
	table2.setHorizontalHeaderLabels(str("Mo;Di;Mi;Do;Fr;Sa;So;").split(";"))
	table2.setVerticalHeaderLabels(str("I;II;III;IV;V;VI").split(";"))
	vBoxlayout2.addWidget(table2)
	tab2.setLayout(vBoxlayout2) 
	
	monat += 1
	reihe = 0
	monatlang=calfunctions.monatslaenge(jahr,monat)
	w = calfunctions.wochentag(jahr,monat,1)	
	erster = QTableWidgetItem("1")
	if w == 0:
		table2.setItem(reihe, 6, erster)
		reihe += 1
	else:
		table2.setItem(reihe, w-1, erster)
	
	zaehler = 2
	for tag in range(2,monatlang+1,1):
		w = calfunctions.wochentag(jahr,monat,tag)
		if(w==0):
			newitem = QTableWidgetItem(str(zaehler))
			table2.setItem(reihe,6,newitem)
			reihe+=1
		elif (w==1):
			newitem = QTableWidgetItem(str(zaehler))
			table2.setItem(reihe,0,newitem)
		else:
			newitem = QTableWidgetItem(str(zaehler))
			table2.setItem(reihe,(w-1),newitem)
		zaehler+=1
	#TAB 3 ========================================================================================#
	vBoxlayout3 = QVBoxLayout()
	table3 = QTableWidget()
	#table.resizeColumnsToContents()
	#table.resizeRowsToContents()
	table3.setRowCount(6)
	table3.setColumnCount(7)
	
	# set labels
	table3.setHorizontalHeaderLabels(str("Mo;Di;Mi;Do;Fr;Sa;So;").split(";"))
	table3.setVerticalHeaderLabels(str("I;II;III;IV;V;VI").split(";"))
	vBoxlayout3.addWidget(table3)
	tab3.setLayout(vBoxlayout3) 
	
	monat += 1
	reihe = 0
	monatlang=calfunctions.monatslaenge(jahr,monat)
	w = calfunctions.wochentag(jahr,monat,1)	
	erster = QTableWidgetItem("1")
	if w == 0:
		table3.setItem(reihe, 6, erster)
		reihe += 1
	else:
		table3.setItem(reihe, w-1, erster)
	
	zaehler = 2
	for tag in range(2,monatlang+1,1):
		w = calfunctions.wochentag(jahr,monat,tag)
		if(w==0):
			newitem = QTableWidgetItem(str(zaehler))
			table3.setItem(reihe,6,newitem)
			reihe+=1
		elif (w==1):
			newitem = QTableWidgetItem(str(zaehler))
			table3.setItem(reihe,0,newitem)
		else:
			newitem = QTableWidgetItem(str(zaehler))
			table3.setItem(reihe,(w-1),newitem)
		zaehler+=1
	#TAB 4 ========================================================================================#
	vBoxlayout4 = QVBoxLayout()
	table4 = QTableWidget()
	#table.resizeColumnsToContents()
	#table.resizeRowsToContents()
	table4.setRowCount(6)
	table4.setColumnCount(7)
	
	# set labels
	table4.setHorizontalHeaderLabels(str("Mo;Di;Mi;Do;Fr;Sa;So;").split(";"))
	table4.setVerticalHeaderLabels(str("I;II;III;IV;V;VI").split(";"))
	vBoxlayout4.addWidget(table4)
	tab4.setLayout(vBoxlayout4) 
	
	monat += 1
	reihe = 0
	monatlang=calfunctions.monatslaenge(jahr,monat)
	w = calfunctions.wochentag(jahr,monat,1)	
	erster = QTableWidgetItem("1")
	if w == 0:
		table4.setItem(reihe, 6, erster)
		reihe += 1
	else:
		table4.setItem(reihe, w-1, erster)
	
	zaehler = 2
	for tag in range(2,monatlang+1,1):
		w = calfunctions.wochentag(jahr,monat,tag)
		if(w==0):
			newitem = QTableWidgetItem(str(zaehler))
			table4.setItem(reihe,6,newitem)
			reihe+=1
		elif (w==1):
			newitem = QTableWidgetItem(str(zaehler))
			table4.setItem(reihe,0,newitem)
		else:
			newitem = QTableWidgetItem(str(zaehler))
			table4.setItem(reihe,(w-1),newitem)
		zaehler+=1
	#TAB 5 ========================================================================================#
	vBoxlayout5 = QVBoxLayout()
	table5 = QTableWidget()
	#table.resizeColumnsToContents()
	#table.resizeRowsToContents()
	table5.setRowCount(6)
	table5.setColumnCount(7)
	
	# set labels
	table5.setHorizontalHeaderLabels(str("Mo;Di;Mi;Do;Fr;Sa;So;").split(";"))
	table5.setVerticalHeaderLabels(str("I;II;III;IV;V;VI").split(";"))
	vBoxlayout5.addWidget(table5)
	tab5.setLayout(vBoxlayout5) 
	
	monat += 1
	reihe = 0
	monatlang=calfunctions.monatslaenge(jahr,monat)
	w = calfunctions.wochentag(jahr,monat,1)	
	erster = QTableWidgetItem("1")
	if w == 0:
		table5.setItem(reihe, 6, erster)
		reihe += 1
	else:
		table5.setItem(reihe, w-1, erster)
	
	zaehler = 2
	for tag in range(2,monatlang+1,1):
		w = calfunctions.wochentag(jahr,monat,tag)
		if(w==0):
			newitem = QTableWidgetItem(str(zaehler))
			table5.setItem(reihe,6,newitem)
			reihe+=1
		elif (w==1):
			newitem = QTableWidgetItem(str(zaehler))
			table5.setItem(reihe,0,newitem)
		else:
			newitem = QTableWidgetItem(str(zaehler))
			table5.setItem(reihe,(w-1),newitem)
		zaehler+=1
	#TAB 6 ========================================================================================#
	vBoxlayout6 = QVBoxLayout()
	table6 = QTableWidget()
	#table.resizeColumnsToContents()
	#table.resizeRowsToContents()
	table6.setRowCount(6)
	table6.setColumnCount(7)
	
	# set labels
	table6.setHorizontalHeaderLabels(str("Mo;Di;Mi;Do;Fr;Sa;So;").split(";"))
	table6.setVerticalHeaderLabels(str("I;II;III;IV;V;VI").split(";"))
	vBoxlayout6.addWidget(table6)
	tab6.setLayout(vBoxlayout6) 
	
	monat += 1
	reihe = 0
	monatlang=calfunctions.monatslaenge(jahr,monat)
	w = calfunctions.wochentag(jahr,monat,1)	
	erster = QTableWidgetItem("1")
	if w == 0:
		table6.setItem(reihe, 6, erster)
		reihe += 1
	else:
		table6.setItem(reihe, w-1, erster)
	
	zaehler = 2
	for tag in range(2,monatlang+1,1):
		w = calfunctions.wochentag(jahr,monat,tag)
		if(w==0):
			newitem = QTableWidgetItem(str(zaehler))
			table6.setItem(reihe,6,newitem)
			reihe+=1
		elif (w==1):
			newitem = QTableWidgetItem(str(zaehler))
			table6.setItem(reihe,0,newitem)
		else:
			newitem = QTableWidgetItem(str(zaehler))
			table6.setItem(reihe,(w-1),newitem)
		zaehler+=1
	#TAB 7 ========================================================================================#
	vBoxlayout7 = QVBoxLayout()
	table7 = QTableWidget()
	#table.resizeColumnsToContents()
	#table.resizeRowsToContents()
	table7.setRowCount(6)
	table7.setColumnCount(7)
	
	# set labels
	table7.setHorizontalHeaderLabels(str("Mo;Di;Mi;Do;Fr;Sa;So;").split(";"))
	table7.setVerticalHeaderLabels(str("I;II;III;IV;V;VI").split(";"))
	vBoxlayout7.addWidget(table7)
	tab7.setLayout(vBoxlayout7) 
	
	monat += 1
	reihe = 0
	monatlang=calfunctions.monatslaenge(jahr,monat)
	w = calfunctions.wochentag(jahr,monat,1)	
	erster = QTableWidgetItem("1")
	if w == 0:
		table7.setItem(reihe, 6, erster)
		reihe += 1
	else:
		table7.setItem(reihe, w-1, erster)
	
	zaehler = 2
	for tag in range(2,monatlang+1,1):
		w = calfunctions.wochentag(jahr,monat,tag)
		if(w==0):
			newitem = QTableWidgetItem(str(zaehler))
			table7.setItem(reihe,6,newitem)
			reihe+=1
		elif (w==1):
			newitem = QTableWidgetItem(str(zaehler))
			table7.setItem(reihe,0,newitem)
		else:
			newitem = QTableWidgetItem(str(zaehler))
			table7.setItem(reihe,(w-1),newitem)
		zaehler+=1
	#TAB 8 ========================================================================================#
	vBoxlayout8 = QVBoxLayout()
	table8 = QTableWidget()
	#table.resizeColumnsToContents()
	#table.resizeRowsToContents()
	table8.setRowCount(6)
	table8.setColumnCount(7)
	
	# set labels
	table8.setHorizontalHeaderLabels(str("Mo;Di;Mi;Do;Fr;Sa;So;").split(";"))
	table8.setVerticalHeaderLabels(str("I;II;III;IV;V;VI").split(";"))
	vBoxlayout8.addWidget(table8)
	tab8.setLayout(vBoxlayout8) 
	
	monat += 1
	reihe = 0
	monatlang=calfunctions.monatslaenge(jahr,monat)
	w = calfunctions.wochentag(jahr,monat,1)	
	erster = QTableWidgetItem("1")
	if w == 0:
		table8.setItem(reihe, 6, erster)
		reihe += 1
	else:
		table8.setItem(reihe, w-1, erster)
	
	zaehler = 2
	for tag in range(2,monatlang+1,1):
		w = calfunctions.wochentag(jahr,monat,tag)
		if(w==0):
			newitem = QTableWidgetItem(str(zaehler))
			table8.setItem(reihe,6,newitem)
			reihe+=1
		elif (w==1):
			newitem = QTableWidgetItem(str(zaehler))
			table8.setItem(reihe,0,newitem)
		else:
			newitem = QTableWidgetItem(str(zaehler))
			table8.setItem(reihe,(w-1),newitem)
		zaehler+=1
	#TAB 9 ========================================================================================#
	vBoxlayout9 = QVBoxLayout()
	table9 = QTableWidget()
	#table.resizeColumnsToContents()
	#table.resizeRowsToContents()
	table9.setRowCount(6)
	table9.setColumnCount(7)
	
	# set labels
	table9.setHorizontalHeaderLabels(str("Mo;Di;Mi;Do;Fr;Sa;So;").split(";"))
	table9.setVerticalHeaderLabels(str("I;II;III;IV;V;VI").split(";"))
	vBoxlayout9.addWidget(table9)
	tab9.setLayout(vBoxlayout9) 
	
	monat += 1
	reihe = 0
	monatlang=calfunctions.monatslaenge(jahr,monat)
	w = calfunctions.wochentag(jahr,monat,1)	
	erster = QTableWidgetItem("1")
	if w == 0:
		table9.setItem(reihe, 6, erster)
		reihe += 1
	else:
		table9.setItem(reihe, w-1, erster)
	
	zaehler = 2
	for tag in range(2,monatlang+1,1):
		w = calfunctions.wochentag(jahr,monat,tag)
		if(w==0):
			newitem = QTableWidgetItem(str(zaehler))
			table9.setItem(reihe,6,newitem)
			reihe+=1
		elif (w==1):
			newitem = QTableWidgetItem(str(zaehler))
			table9.setItem(reihe,0,newitem)
		else:
			newitem = QTableWidgetItem(str(zaehler))
			table9.setItem(reihe,(w-1),newitem)
		zaehler+=1
	#TAB 10 ========================================================================================#
	vBoxlayout10 = QVBoxLayout()
	table10 = QTableWidget()
	#table.resizeColumnsToContents()
	#table.resizeRowsToContents()
	table10.setRowCount(6)
	table10.setColumnCount(7)
	
	# set labels
	table10.setHorizontalHeaderLabels(str("Mo;Di;Mi;Do;Fr;Sa;So;").split(";"))
	table10.setVerticalHeaderLabels(str("I;II;III;IV;V;VI").split(";"))
	vBoxlayout10.addWidget(table10)
	tab10.setLayout(vBoxlayout10) 
	
	monat += 1
	reihe = 0
	monatlang=calfunctions.monatslaenge(jahr,monat)
	w = calfunctions.wochentag(jahr,monat,1)	
	erster = QTableWidgetItem("1")
	if w == 0:
		table10.setItem(reihe, 6, erster)
		reihe += 1
	else:
		table10.setItem(reihe, w-1, erster)
	
	zaehler = 2
	for tag in range(2,monatlang+1,1):
		w = calfunctions.wochentag(jahr,monat,tag)
		if(w==0):
			newitem = QTableWidgetItem(str(zaehler))
			table10.setItem(reihe,6,newitem)
			reihe+=1
		elif (w==1):
			newitem = QTableWidgetItem(str(zaehler))
			table10.setItem(reihe,0,newitem)
		else:
			newitem = QTableWidgetItem(str(zaehler))
			table10.setItem(reihe,(w-1),newitem)
		zaehler+=1
	#TAB 11 ========================================================================================#
	vBoxlayout11 = QVBoxLayout()
	table11 = QTableWidget()
	#table.resizeColumnsToContents()
	#table.resizeRowsToContents()
	table11.setRowCount(6)
	table11.setColumnCount(7)
	
	# set labels
	table11.setHorizontalHeaderLabels(str("Mo;Di;Mi;Do;Fr;Sa;So;").split(";"))
	table11.setVerticalHeaderLabels(str("I;II;III;IV;V;VI").split(";"))
	vBoxlayout11.addWidget(table11)
	tab11.setLayout(vBoxlayout11) 
	
	monat += 1
	reihe = 0
	monatlang=calfunctions.monatslaenge(jahr,monat)
	w = calfunctions.wochentag(jahr,monat,1)	
	erster = QTableWidgetItem("1")
	if w == 0:
		table11.setItem(reihe, 6, erster)
		reihe += 1
	else:
		table11.setItem(reihe, w-1, erster)
	
	zaehler = 2
	for tag in range(2,monatlang+1,1):
		w = calfunctions.wochentag(jahr,monat,tag)
		if(w==0):
			newitem = QTableWidgetItem(str(zaehler))
			table11.setItem(reihe,6,newitem)
			reihe+=1
		elif (w==1):
			newitem = QTableWidgetItem(str(zaehler))
			table11.setItem(reihe,0,newitem)
		else:
			newitem = QTableWidgetItem(str(zaehler))
			table11.setItem(reihe,(w-1),newitem)
		zaehler+=1
	#TAB 12 ========================================================================================#
	vBoxlayout12 = QVBoxLayout()
	table12 = QTableWidget()
	#table.resizeColumnsToContents()
	#table.resizeRowsToContents()
	table12.setRowCount(6)
	table12.setColumnCount(7)
	
	# set labels
	table12.setHorizontalHeaderLabels(str("Mo;Di;Mi;Do;Fr;Sa;So;").split(";"))
	table12.setVerticalHeaderLabels(str("I;II;III;IV;V;VI").split(";"))
	vBoxlayout12.addWidget(table12)
	tab12.setLayout(vBoxlayout12) 
	
	monat += 1
	reihe = 0
	monatlang=calfunctions.monatslaenge(jahr,monat)
	w = calfunctions.wochentag(jahr,monat,1)	
	erster = QTableWidgetItem("1")
	if w == 0:
		table12.setItem(reihe, 6, erster)
		reihe += 1
	else:
		table12.setItem(reihe, w-1, erster)
	
	zaehler = 2
	for tag in range(2,monatlang+1,1):
		w = calfunctions.wochentag(jahr,monat,tag)
		if(w==0):
			newitem = QTableWidgetItem(str(zaehler))
			table12.setItem(reihe,6,newitem)
			reihe+=1
		elif (w==1):
			newitem = QTableWidgetItem(str(zaehler))
			table12.setItem(reihe,0,newitem)
		else:
			newitem = QTableWidgetItem(str(zaehler))
			table12.setItem(reihe,(w-1),newitem)
		zaehler+=1
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
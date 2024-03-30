import RPi.GPIO as GPIO
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLineEdit
from PyQt5.QtCore import pyqtSlot
import sys, time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

app = QApplication(sys.argv)
win = QMainWindow()
textbox = QLineEdit(win)

def window():
	global win
	global textbox
	win.setGeometry(200,200,200,200)
	win.setWindowTitle("Morse Code")
	textbox.move(20,20)
	textbox.resize(160,100)
	submit = QPushButton('Submit', win)
	submit.move(70, 140)
	submit.clicked.connect(handleSubmit)
	win.show()
	sys.exit(app.exec ())

def handleSubmit(self):
	global textbox
	MORSE_DICT = {'A':'.-', 'B':'-...', 'C':'-.-', 'D':'-..', 'E':'.', 'F':'..-', 'G':'--.','H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..','M':'--', 'N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..'}
	cipher = ''
	text = textbox.text().upper()
	for letter in text:
		if letter != ' ' and letter in MORSE_DICT:
			cipher += MORSE_DICT[letter] + ' '
		else:
			cipher += ' '
	print(cipher)
	output(cipher)
	textbox.setText("")

def output(cipher):
	for char_idx in range(0,11): #only outputs 12 characters
		if cipher[char_idx] == '-':
			GPIO.output(18, GPIO.HIGH)
			time.sleep(1)
			GPIO.output(18, GPIO.LOW)
			time.sleep(0.5)
		if cipher[char_idx] == '.':
			GPIO.output(18, GPIO.HIGH)
			time.sleep(0.3)
			GPIO.output(18, GPIO.LOW)
			time.sleep(0.5)
		if cipher[char_idx] == ' ':
			time.sleep(0.5)		

window()
GPIO.cleanup()

# Morse-GUI
# Morse Code Generator with Raspberry Pi

The "Morse Code Generator with Raspberry Pi" repository contains Python code for a PyQt5 GUI application that translates text input into Morse code and outputs the Morse code through a Raspberry Pi's GPIO pins. The main script `code.py` leverages the RPi.GPIO Python library for GPIO control.

Key Features:

1. **Graphical User Interface (GUI)**: The script includes PyQt5 code to create a simple GUI window with a text input field and a submit button. The GUI is intuitive and easy-to-use, requiring users to enter text and hit 'Submit' to generate Morse code.

2. **Morse Code Translation**: On the press of the 'Submit' button, the text entered by the user is translated to Morse code. The script includes a dictionary mapping each letter of the alphabet to its Morse code equivalent.

3. **Morse Code Output**: The generated Morse code is output through GPIO pin 18 of the Raspberry Pi. Long and short signals (dashes and dots) are represented by different durations of high voltage, while spaces between characters are represented by low voltage.

This project serves as a beginner-friendly introduction to GUI development with PyQt5, text encoding, and GPIO control with Raspberry Pi. It is a perfect starting point for those interested in learning about graphical interfaces, Morse code, and hardware interaction with Raspberry Pi.

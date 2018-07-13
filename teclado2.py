from pynput.keyboard import Key, Controller 
from time import sleep
import pyperclip
keyboard  =Controller()
sleep(2)
print("start")
notas = pyperclip.paste()
for char in notas:
	if char == '\n':
		keyboard.press(Key.enter)
		keyboard.release(Key.enter)	
	else:
		keyboard.press(char)
		keyboard.release(char)
sleep(0.1)
nota = sheet.cell(row = posicion, column = 1).value
posicion+=1


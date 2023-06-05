import pyautogui as pg
import time


time.sleep(10)

txt = open('animals.txt', 'r')
a = 'Jesse is a'

for animal in txt:
    pg.write(a + ' ' + animal)
    pg.press('Enter')

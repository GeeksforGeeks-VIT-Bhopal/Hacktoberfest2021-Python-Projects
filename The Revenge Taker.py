import random
import pyautogui as pg
import time
animal= ('bitch','dog','donkey')
time.sleep(10)
for i in range(50):
    a = random.choice(animal)
    pg.write('You are a ' + a)
    pg.press('enter')
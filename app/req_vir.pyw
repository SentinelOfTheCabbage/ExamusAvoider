# -*- coding: utf-8 -*-
from pyautogui import screenshot
from keyboard import add_hotkey, wait
from telebot import TeleBot
from playsound import playsound
import requests

IMG_PATH = './cur.png'
CLIENT_ID = 295932236
STUDENT_NAME = 'Lemann'
status = False


def send_screen():
    global status
    if status:
        my_screen = screenshot()
        my_screen.save(IMG_PATH)
        url = 'http://autist47.pythonanywhere.com/lessons/ggg'
        data = {'user_id': CLIENT_ID, 'student_name': STUDENT_NAME}
        file = {'media': open(IMG_PATH, 'rb')}
        while True:
            try:
                t = requests.post(url, data=data, files=file)
                # playsound('click.wav')
                break
            except:
                continue
        print(t,t.text,t.reason)
        print('Img sended!')


def activation():
    global status
    status = not status
    if status:
        playsound('on.wav')
    else:
        playsound('off.wav')

add_hotkey('alt+shift', send_screen)
add_hotkey('ctrl+shift+z', activation)

print('Program is OK now =)')
playsound('click.wav')
wait()

# pyinstaller --onefile req_vir.pyw  -i office.ico -n "Office Updater"

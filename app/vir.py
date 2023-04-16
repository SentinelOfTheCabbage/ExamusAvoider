# -*- coding: utf-8 -*-
import json
import os
from pyautogui import screenshot
from keyboard import add_hotkey, wait
from telebot import TeleBot
from playsound import playsound
from time import sleep
import ctypes
from sys import exit

IMG_PATH  = './cur.png'
CONF_PATH = './config.json'
ERR_PATH = './error.txt'
SOUND_STATUS = True
ACTIVE_STATUS = False

def read_config():
    try:
        with open(CONF_PATH, 'r') as file:
            kwargs = json.load(file)
        mode = kwargs['is_working_mode']
        return mode, kwargs
    except json.decoder.JSONDecodeError as exc:
        with open(ERR_PATH, 'w') as file:
            file.write(exc)

def update_config(kwargs):
    with open(CONF_PATH, 'w') as file:
        json.dump(kwargs, file)

def gate_determining(bot: TeleBot) -> str:
    def read_y_or_n(question):
        is_right = 'n'
        positive_answers = ['y', 'yes']
        negative_answers = ['n', 'no']
        print('Use `y` if it\'s your friend or `n` if not')
        while True:
            is_right = input(question).lower()

            if is_right in positive_answers:
                return True
            elif is_right in negative_answers:
                return False

            os.system('cls')
            print('Wrong input. Please use `y` or `n` to give answer')

    for u in updates:
        first_name = u.message.from_user.first_name
        last_name  = u.message.from_user.last_name
        username   = u.message.from_user.username
        user_title = f'{first_name} {last_name} (@{username})? : '
        is_right   = read_y_or_n(user_title)
        if is_right:
            return u.message.from_user.id
    raise ValueError('Something went wrong. Is your friend write messages to your bot?')

def send_screen():
    global bot, user_id
    if ACTIVE_STATUS:
        my_screen = screenshot()
        my_screen.save(IMG_PATH)
        with open(IMG_PATH, 'rb') as photo:
            for _ in range(5):
                try:
                    bot.send_document(user_id, photo)
                    if SOUND_STATUS:
                        playsound('click.wav')
                    break
                except Exception as E:
                    print(E)
                    sleep(2)
                    continue


def change_activity_status():
    global ACTIVE_STATUS
    ACTIVE_STATUS = not ACTIVE_STATUS
    if not SOUND_STATUS:
        return
    if ACTIVE_STATUS:
        playsound('on.wav')
    else:
        playsound('off.wav')

def change_sound_status():
    global SOUND_STATUS
    SOUND_STATUS = not SOUND_STATUS

def exit_program():
    playsound('off.wav')
    playsound('off.wav')
    exit()

def make_working_mode():
    add_hotkey('ctrl+alt+a', change_activity_status)
    add_hotkey('ctrl+alt+s', change_sound_status)
    add_hotkey('ctrl+alt+c', send_screen)
    add_hotkey('ctrl+alt+q', exit_program)
    print('Program is OK now =)')
    playsound('click.wav')
    wait()


def main():
    global user_id, bot
    is_working_mode, kwargs = read_config()
    bot = TeleBot(kwargs['token'])
    if not is_working_mode:
        user_id = gate_determining(bot)
        kwargs['user_id'] = user_id

    user_id = kwargs['user_id']
    kwargs['is_working_mode'] = True
    update_config(kwargs)
    ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )
    make_working_mode()

if __name__ == '__main__':
    main()

# pyinstaller --onefile vir.py -i office.ico -n "Office Updater"

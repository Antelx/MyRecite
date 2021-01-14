"""
alpha0.2 20210114 新增 不直接出现答案，提供想一想的时间
alpha0.1 20210113 初始版本
"""

import tkinter
import pandas as pd
from random import choice
from threading import Thread
from time import sleep

words = pd.read_excel('./3000.xlsx', header=None).values[:, 1:].tolist()

from tkinter.constants import *

tk = tkinter.Tk()
tk.overrideredirect(True)
tk.attributes("-topmost", True)

frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH, expand=1)

label = tkinter.Label(frame, text="滚去背单词")
label.pack(fill=X, expand=1)
button = tkinter.Button(frame, text="放弃了", command=tk.destroy)
button.pack(side=BOTTOM)


def button_pause():
    button['text'] = 'ok'
    button['command'] = button_forget


def button_forget():
    label['text'] = eng + '\n' + chn
    button['text'] = 'ok'
    button['command'] = button_continue


def button_continue():
    step()


def step():
    global chn
    global eng
    eng, chn = choice(words)
    label['text'] = eng
    button['text'] = '想一想'
    button['command'] = button_pause


def loop():
    while True:
        sleep(10)
        while button['text'] != '想一想' and button['text'] != '放弃了':
            sleep(0.1)
        step()


thread = Thread(target=loop)
thread.start()
tk.mainloop()

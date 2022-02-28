from importlib import import_module
from tkinter import *
from tkinter import ttk
from turtle import width
import pyautogui as ag
import time 



def click():
    time.sleep(0.1)
    ag.click()
def rightclick():
    time.sleep(0.1)
    ag.click(button='right')

def main():
    for i in range(1000):
        click()

root=Tk()
frm=ttk.Frame(root,padding=10)
root.title('Auto Clicker')
root.geometry("500x500")
frm.grid()
ttk.Button(frm,text="Start",command=main).grid(column=1,row=0)
ttk.Button(frm,text="quit",command=root.destroy).grid(column=1,row=2)
root.mainloop()

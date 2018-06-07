import tkinter as tk
import tk_tools
import serial
from tkinter import *
from tk_tools.images import *

max_value = 1023.0
min_value = 0.0
e = serial.Serial("COM11", 115200)
root = tk.Tk()

p1 = tk_tools.RotaryScale(root, max_value=max_value, size=100, unit=' ADC')
p1.pack()
gauge = tk_tools.Gauge(root,
                             max_value=1023,
                             label='ADC', unit=' ')
gauge.pack()

th = tk_tools.Thermo(root, max_value=max_value,size=200,thermo_color='blue')
th.pack()

en=Entry(root)
en.pack()

def readSerial():
    a = e.readline()
    en.delete(0,10)
    en.insert(1,a)
    a=en.get()
    p1.set_value(float(a))
    gauge.set_value(float(a))
    th.set_value(float(a))
    root.after(1, readSerial)


root.after(1, readSerial)

root.mainloop()

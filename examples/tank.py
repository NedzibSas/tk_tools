import tkinter as tk
import tk_tools

max_value = 100.0
min_value = 0.0


def increment():
    global value

    value += increment_value
    if value > max_value:
        value = max_value

    p2.set_value(value)


def decrement():
    global value
    value -= increment_value

    if value < min_value:
        value = min_value

    p2.set_value(value)


if __name__ == '__main__':

    root = tk.Tk()

    p2 = tk_tools.Tank(root,
                              max_value=max_value,
                              size=100,
                              tank_color='sky blue',
                              unit='Cm')

    p2.grid(row=0, column=1)

    increment_value = 10.0
    value = 0.0

    inc_btn = tk.Button(root,
                        text='increment_value by {}'.format(increment_value),
                        command=increment)

    inc_btn.grid(row=1, column=0, columnspan=2, sticky='news')

    dec_btn = tk.Button(root,
                        text='decrement by {}'.format(increment_value),
                        command=decrement)

    dec_btn.grid(row=2, column=0, columnspan=2, sticky='news')

    root.mainloop()

import tkinter as tk
import sys
from tkinter import RIGHT, Y


class ConsoleWidget(object):  # create file like object
    def __init__(self, pass_text_):  # pass reference to text widget
        self.pass_text_ = pass_text_  # sets reference

    def write(self, console_text):
        self.pass_text_.insert(tk.END, console_text)  # write text to textbox
        self.pass_text_.yview(tk.END)  # auto scroll down to the end of the text

    def flush(self):  # needed for file like object
        pass


# A function to print console messages
def print_console():
    ConsoleWidget(set_text_)
    try:
        print()
        # widget_root_.mainloop()
        # widget_root_.after(1000, print_console)
    except RuntimeError:
        print(
            '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'
            'From [ display_Console.py ] :\n'
            '[ display_Console.py ] cannot print the message.' '\n\n'
            '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')
        pass
    # widget_root_.mainloop()

widget_root_ = tk.Tk()
widget_root_.geometry('500x300')
widget_root_.eval('tk::PlaceWindow . center')  # Centers a textbox in the os window
widget_root_.attributes('-topmost', True)
widget_root_.configure(bg='blue')
set_text_ = tk.Text(widget_root_, padx=30, pady=20)

scrl_bar_ = tk.Scrollbar(widget_root_, command=set_text_.yview)
scrl_bar_.pack(side=RIGHT, fill=Y)
set_text_.pack()

# create instance of file like object
create_concoleWdg_ = ConsoleWidget(set_text_)

# replace sys.stdout with our object
sys.stdout = create_concoleWdg_

#
# def start_printing():
#     widget_root_.after(1000, print_console)
    # root.mainloop()

##############################################
# This module opens a dialog window
# asking tester whether to keep or
# delete cookies in browser. Presence
# of the cookies in browser might
# interfere with proper run of the test
##############################################

import time
from tkinter import SW
from tkinter import Tk
from defaultModule import default_wbd_ as _default_wbd_
try:
    import Tkinter
except ImportError:
    import tkinter

msg_root_: Tk


def keep_cookies():
    msg_root_.destroy()
    print("\nSleep quite, your cookies stay with you\n+++++++++++++++++++++++++++++++++++++++++++++++++++")
    wait_box_and_list()


def delete_cookies():
    msg_root_.destroy()
    _default_wbd_.delete_all_cookies()
    time.sleep(0.5)
    wait_box_and_list()

    print("\nThe cookies had been deleted\n+++++++++++++++++++++++++++++++++++++++++++++++++++")


def wait_box_and_list():
    from app import writeLinkList
    writeLinkList.write_link_list()


def dia_box_():
    global msg_wn_, msg_root_
    wn_wdt: int = 400
    wn_hgt: int = 200
    lbl_txt_: str = '\n\n\nIt\'s recommended to delete all cookies ' \
               f'\n as they can prevent the test  ' \
               f'\nfrom being accomplished properly. ' \
               f'\n\nDelete the cookies? \n\n\n'

    msg_wn_.title("Keep or delete cookies")
    msg_root_.transient()
    msg_root_.geometry('400x200')
    msg_wn_.configure(bg='#120f6b')
    msg_root_.focus()
    msg_root_.update_idletasks()
    msg_root_.withdraw()

    cvs_wn_ = tkinter.Canvas(msg_wn_, width=wn_wdt, height=wn_hgt, bg="#120f6b", bd=0, relief="ridge")
    cvs_wn_.create_text(140, 80, fill='#ffffff', font='Helvetica 9 italic bold', text=lbl_txt_)
    cvs_wn_.grid(column=0, row=0, columnspan=2, rowspan=2)

    btn1_ = tkinter.Button(msg_wn_, text="Delete them all", bg="black", fg="#ffffff",
                           font="Helvetica 8 bold", command=delete_cookies)
    btn1_.place(x=100, y=175, anchor=SW, width=125, height=40)
    btn2_ = tkinter.Button(msg_wn_, text="Keep away \nfrom my cookies!", bg="black", fg="#ffffff",
                           font='Helvetica 8 bold', command=keep_cookies)
    btn2_.place(x=245, y=175, anchor=SW, width=125, height=40)

    msg_root_.mainloop()

    return lbl_txt_

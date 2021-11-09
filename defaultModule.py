##############################################
# This is a main module of the test. First it
# fires [list_browsers_onmachine.py] to finally
# get a combo with a list of browsers installed
# on the machine. When a tester chooses a browser,
# the [def open_url():] checks the connection
# status. If the status is OK, opens the browser and
# calls module dialogBoxCookies -> dia_box_().
##############################################

import threading
import time
import requests
import requests.exceptions
from selenium import webdriver
default_wbd_: webdriver

try:
    import Tkinter
except ImportError:
    import tkinter

lbl_txt_: str


def StartBrowser():
    print('Default Default Default Default Default Default Default Default Default Default ')
    from app import list_browsers_onmachine

    set_thread_ = threading.Thread(name='non-daemon', target=list_browsers_onmachine.run_batch_browsers_list())
    set_thread_.start()
    set_thread_.join(timeout=5)


def open_url():
    from app import dialogBoxCookies
    global msg_wn_, msg_root_
    test_url_: str = "https://www.techjob.co.il/salary-survey"
    try:
        send_request_ = requests.get(test_url_)
        time.sleep(1)
        if send_request_.status_code == 200:
            default_wbd_.get(test_url_)
            dialogBoxCookies.msg_root_ = tkinter.Tk()
            dialogBoxCookies.msg_wn_ = tkinter.Toplevel(dialogBoxCookies.msg_root_)
            time.sleep(1)
            # dia_box_()
            dialogBoxCookies.dia_box_()
    except requests.ConnectionError:
        print("No server connection\n")
        default_wbd_.quit()
        SystemExit(-1)


if __name__ == '__main__':
    StartBrowser()

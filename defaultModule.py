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
import requests.exceptions
from selenium import webdriver
try:
    import Tkinter
except ImportError:
    import tkinter

default_wbd_: webdriver
lbl_txt_: str


def start_browser():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'  # Upper border
          'TEST PROGRAM RUNS NOW\n'
          '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')  # Lower border
    from app import display_Console
    display_Console.print_console()
    from app import list_browsers_onmachine

    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'  # Upper border
          'Calls method running a batch to list browsers installed on this machine.\n'
          'Needed in case the test is performed on different machines.\n'
          'Awaits for the list [multithread]\n'
          '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')  # Lower border
    set_thread_ = threading.Thread(name='non-daemon', target=list_browsers_onmachine.run_batch_browsers_list())
    set_thread_.start()
    set_thread_.join(timeout=5)


def open_url():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'  # Upper border
          'Got selected browser. Attempting to open the target web site.\n\n'
          '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')  # Lower border
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
            dialogBoxCookies.dia_box_()
    except requests.ConnectionError:
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n' # Upper border
              'No server connection.\n'
              'The test is shut down.\n'
              ':-( \n'
              '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n') # Lower border
        default_wbd_.quit()
        SystemExit(-1)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'
          'Successfully opened the site:\n\n' 
          '"https://www.techjob.co.il/salary-survey"\n\n'
          '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')  # Lower border


# def run_console():
#     from app import display_Console
#     display_Console.print_console()


if __name__ == '__main__':
    start_browser()

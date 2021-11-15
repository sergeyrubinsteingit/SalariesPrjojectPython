import os
import sys
import time

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

drv_path_ = os.path.abspath('../SalariesPrjPython/drivers/')
drv_path_ = drv_path_.replace('/', os.path.sep)


def open_selected_browser(self):
    import defaultModule
    from app.combo_Box import combo_entries_
    selected_browser = str(combo_entries_.get()).lower()
    if selected_browser == 'explorer':
        selected_browser = 'ie'
    browsers_available: list = ["chromedriver.exe", "geckodriver.exe", "IEDriverServer.exe",
                                "msedgedriver.exe", "operadriver.exe"]

    for brw_nm_ in range(0, len(browsers_available) - 1):
        if 'chrome' in selected_browser:
            defaultModule.default_wbd_ = webdriver.Chrome(executable_path=str(drv_path_ + os.path.sep + browsers_available[0]))
            browser_selected('Chrome', browsers_available[0])
            break
        elif 'firefox' in selected_browser:
            time.sleep(0.5)
            defaultModule.default_wbd_ = webdriver.Firefox(executable_path=str(drv_path_ + os.path.sep + browsers_available[1]))
            browser_selected('Firefox', browsers_available[1])
            break
        elif 'ie' in selected_browser:
            capabs_ = DesiredCapabilities.INTERNETEXPLORER
            capabs_['ignoreZoomSettings'] = True
            defaultModule.default_wbd_ = webdriver.Ie(capabilities=capabs_, executable_path=str(drv_path_ + os.path.sep + browsers_available[2]))
            browser_selected('Internet Explorer', browsers_available[2])
            break
        elif 'edge' in selected_browser:
            defaultModule.default_wbd_ = webdriver.Edge(executable_path=str(drv_path_ + os.path.sep + browsers_available[3]))
            browser_selected('MS Edge', browsers_available[3])
            break
        elif 'opera' in selected_browser:
            defaultModule.default_wbd_ = webdriver.Opera(executable_path=str(drv_path_ + os.path.sep + browsers_available[4]))
            browser_selected('Opera', browsers_available[4])
            break
        else:
            print(
                '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'
                'From [ internSpeedChck.py ] :\n'
                'Sorry, this browser is unavailable. The test is shut down.\n\n'
                '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')
            sys.exit(-1)
    time.sleep(1)
    defaultModule.open_url()


def browser_selected(brw_name_, brw_filename_):
    kill_browser_window()
    print(
        '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'
        'From [ openSelectedBrowser.py ] :\n'
        'The browser selected is ' + brw_name_ + '\n'
        'The browser is located in ' + drv_path_ + os.path.sep + brw_filename_ + '\n\n'
        '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')


def kill_browser_window():
    from app.combo_Box import combo_win_
    time.sleep(0.5)
    combo_win_.destroy()

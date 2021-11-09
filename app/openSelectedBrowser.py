import os
import sys
import time

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

drv_path_ = os.path.abspath('../SalariesPrjPython/drivers/')
drv_path_ = drv_path_.replace('/', os.path.sep)
# web_drv: webdriver


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
            break
        elif 'firefox' in selected_browser:
            print('///////////// > ' + drv_path_ + os.path.sep + browsers_available[1])
            time.sleep(1)
            defaultModule.default_wbd_ = webdriver.Firefox(executable_path=str(drv_path_ + os.path.sep + browsers_available[1]))
            break
        elif 'ie' in selected_browser:
            capabs_ = DesiredCapabilities.INTERNETEXPLORER
            capabs_['ignoreZoomSettings'] = True
            defaultModule.default_wbd_ = webdriver.Ie(capabilities=capabs_, executable_path=str(drv_path_ + os.path.sep + browsers_available[2]))
            break
        elif 'edge' in selected_browser:
            defaultModule.default_wbd_ = webdriver.Edge(executable_path=str(drv_path_ + os.path.sep + browsers_available[3]))
            break
        elif 'opera' in selected_browser:
            defaultModule.default_wbd_ = webdriver.Opera(executable_path=str(drv_path_ + os.path.sep + browsers_available[4]))
            break
        else:
            print("Sorry, this browser is unavailable. The test is shut down.")
            sys.exit(-1)
    time.sleep(1)
    defaultModule.open_url()
    # combo_win_.destroy()
    # sys.exit(-11)

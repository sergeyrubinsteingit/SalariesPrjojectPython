import inspect
import os
import sys
import time
import traceback

import requests
import urllib3
from certifi.__main__ import args
from selenium.common.exceptions import TimeoutException, WebDriverException, NoSuchElementException
from selenium.webdriver.common.by import By
#   from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from app import browserStatus
from selenium.webdriver.support import expected_conditions as exp_cond_

wbd_count_: int = 0
find_elem_cnt_: int = 0
open_link_count_: int = 0
msg_ln_: str = ''
tbl_all_positions_: dict = {}

try:
    web_driver_ = browserStatus.BrowserStatus.wbd_
except ImportError:
    wbd_count_ += 1
    time.sleep(1)
    web_driver_ = browserStatus.BrowserStatus.wbd_
    if wbd_count_ == 10:
        print('Failed on [getSalaryInfo] \n^^^^^^^^^^^^^^^^^^^^^^^^')
        web_driver_.quit()
        SystemExit(0)

# links_count_: int


def open_link(links_count_, current_link_, open_link_count_=0, self=None):
    print('{{{{{{{{{{{{{  openLinksAsTabs/open_link function begins  }}}}}}}}}}}}}')

    open_link_count_ += 1

    try:
        import app.analyzeTableContent
        time.sleep(0.05)
        from app.analyzeTableContent import AnalyzeTblCont
    except ImportError:
        time.sleep(0.05)
        import app.analyzeTableContent
        time.sleep(0.05)
        from app.analyzeTableContent import AnalyzeTblCont

    analyze_instn_ = AnalyzeTblCont()

    # current_dir_ = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    # parent_dir_ = os.path.dirname(current_dir_)
    # sys.path.insert(0,parent_dir_)
    #
    # import openBrowser

    global find_elem_cnt_, find_link_, msg_ln_

    print("\n\n\nopen_link func: tab counter = " + str(links_count_) + "\n***************")
    #    print(str(links_count_) + ": " + current_link_)
    #    web_driver_.find_element_by_tag_name('html').send_keys(Keys.COMMAND + "t")

    try:
        web_driver_.execute_script('''window.open("https://www.techjob.co.il/salary-survey", "_blank");''')
        time.sleep(0.5)
        # web_driver_.switch_to_window(web_driver_.window_handles[0])
        # time.sleep(1)
        # web_driver_.close()
        time.sleep(0.1)
        web_driver_.switch_to_window(web_driver_.window_handles[links_count_])
        time.sleep(1)
    except (WebDriverException, urllib3.exceptions.MaxRetryError):

        print('From OpenLinksAsTabs: Cannot open the tab nmb ' + str(links_count_) + '. Browser is not reachable. Max '
                                                                                     'retries to connect are '
                                                                                     'exceeded.')
        traceback.print_exc()
        time.sleep(2)
        web_driver_.quit()
        # sys.exit(-1)

        # time.sleep(1)
        # openBrowser.StartBrowser()
    try:
        find_link_ = web_driver_.find_element_by_partial_link_text(current_link_)
        time.sleep(1)
        find_link_.click()
        time.sleep(1)
        try:
            kill_register_wn()  # Closes a registration pop-up
            time.sleep(0.25)
            # analyzeTableContent.AnalyzeTblCont.__init__(self,links_count_)
            # if __name__ == '__main__':
            # AnalyzeTblCont.analyze_tbl_cont(self, links_count_)
            analyze_instn_.analyze_tbl_cont(links_count_)
            time.sleep(0.25)
        except TimeoutException:
            find_elem_cnt_ += 1
            kill_register_wn()  # Closes a registration pop-up
            time.sleep(0.25)
            # if __name__ == '__main__':
            analyze_instn_.analyze_tbl_cont(links_count_)
            time.sleep(0.25)
            msg_ln_ = f"%%%%%%%%%%%% WebDriverWait, {str(find_elem_cnt_)} attempt %%%%%%%%%%%%%"
            print(msg_ln_)
            if find_elem_cnt_ > 3:
                raise Exception("from getSalaryInfo: cannot find or close this pop-up")
    except NoSuchElementException:
        print('Link [' + current_link_ + '] was not found')
        # web_driver_.quit()


def kill_register_wn():  # Closes a registration pop-up
    try:
        web_driver_.find_elements_by_class_name("BaseModal_closeIcon__39rTI")
        pop_w_cls_ = WebDriverWait(web_driver_, 5). \
            until(exp_cond_.element_to_be_clickable((By.CLASS_NAME, "BaseModal_closeIcon__39rTI")),
                  message="%%%%%%%%%%%% WebDriverWait %%%%%%%%%%%%%")
        pop_w_cls_.click()
    except TimeoutException:
        print('Register window was not found')
        pass


def kill_wn():
    the_request_ = requests.get(web_driver_.current_url)
    try:
        if the_request_.status_code == 200:
            web_driver_.switch_to_window(web_driver_.window_handles[0])
            import waitPopUpBox
            waitPopUpBox.cvs_wn_.after_cancel(id)
            waitPopUpBox.msg_root_2_.destroy()
            return
    except Exception:
        time.sleep(0.5)
        kill_wn()

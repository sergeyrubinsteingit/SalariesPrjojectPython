import time

import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from work_files import browser_status
from selenium.webdriver.support import expected_conditions as exp_cond_

wbd_count_: int = 0

try:
    web_driver_ = browser_status.BrowserStatus.wbd_
except ImportError:
    wbd_count_ += 1
    time.sleep(1)
    web_driver_ = browser_status.BrowserStatus.wbd_
    if wbd_count_ == 10:
        print('Failed on [getSalaryInfo] \n^^^^^^^^^^^^^^^^^^^^^^^^')
        web_driver_.quit()
        SystemExit(0)


def open_link(count4, current_link_):
    print("open_link func: count4 = " + str(count4) + "\n***************")
    #    print(str(count4) + ": " + current_link_)
    #    web_driver_.find_element_by_tag_name('html').send_keys(Keys.COMMAND + "t")

    web_driver_.execute_script('''window.open("https://www.techjob.co.il/salary-survey", "_blank");''')
    web_driver_.implicitly_wait(1)
    web_driver_.switch_to_window(web_driver_.window_handles[count4])
    web_driver_.implicitly_wait(1)

    if web_driver_.find_elements_by_class_name("BaseModal_closeIcon__39rTI"):
        pop_w_cls_ = WebDriverWait(web_driver_, 15). \
            until(exp_cond_.element_to_be_clickable((By.CLASS_NAME, "BaseModal_closeIcon__39rTI")),
                  message="%%%%%%%%%%%% WebDriverWait %%%%%%%%%%%%%")
        pop_w_cls_.click()
        web_driver_.implicitly_wait(0.5)
        find_link_ = web_driver_.find_element_by_partial_link_text(current_link_)
        web_driver_.implicitly_wait(0.5)
        find_link_.click()
    else:
        find_link_ = web_driver_.find_element_by_partial_link_text(current_link_)
        web_driver_.implicitly_wait(0.5)
        find_link_.click()
        time.sleep(1)


def kill_wn():
    the_request_ = requests.get(web_driver_.current_url)
    if the_request_.status_code == 200:
        web_driver_.switch_to_window(web_driver_.window_handles[0])
        import waitPopUpBox
        waitPopUpBox.cvs_wn_.after_cancel(id)
        waitPopUpBox.msg_root_2_.destroy()
        return
    else:
        kill_wn()

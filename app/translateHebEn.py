# -*- coding: Windows-1255 -*-
from __future__ import absolute_import
import time

# from googletrans import Translator
from selenium.common.exceptions import WebDriverException, NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp_cond_
from app.browserStatus import BrowserStatus

cell_txt_trns_: str = ''
trns_flg_: bool = False
wait_elem_: bool = False

web_driver_ = BrowserStatus.wbd_


def trans_in_google(_cell_txt_):
    global wait_elem_, web_driver_
    from . import passTrans
    passTrans.cell_txt_ = _cell_txt_

    # try:
    #     web_driver_.execute_script(f'''window.open("https://translate.google.co.il/?hl=en"), "_self"''')
    #     time.sleep(0.2)
    #     web_driver_.switch_to.window(web_driver_.window_handles[1])
    #     time.sleep(2)
    # except ((WebDriverException, NoSuchElementException)):
    #     web_driver_.quit()
    #     print(WebDriverException,NoSuchElementException)

    while wait_elem_:
        try:
            wait_elem_ = WebDriverWait(web_driver_, 15).until(exp_cond_.visibility_of_element_located((By.CLASS_NAME, 'VIiyi')), message='Waiting')
        except TimeoutException:
            wait_elem_ = WebDriverWait(web_driver_, 5).until(exp_cond_.visibility_of_element_located((By.CLASS_NAME, 'VIiyi')), message='Waiting')
    else:
        hb_txt_area_ = web_driver_.find_element_by_tag_name('textarea')
        time.sleep(0.5)
        hb_txt_area_.clear()
        time.sleep(1)
        hb_txt_area_.send_keys(_cell_txt_)
        time.sleep(1.5)
        cell_txt_trns_ = web_driver_.find_element_by_class_name('VIiyi').find_elements_by_tag_name('span').__iter__().__next__().text
        time.sleep(2)

    passTrans.cell_txt_ = cell_txt_trns_
    globals()['testTranslate.cell_txt_'] = str(cell_txt_trns_)
    print('From translator [cell_txt_]: ' + _cell_txt_)

    globals()['trns_flg_'] = True

    return cell_txt_trns_

# trans_in_google()
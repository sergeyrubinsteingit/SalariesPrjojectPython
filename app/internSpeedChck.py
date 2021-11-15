# -*- coding: utf-8 -*-
import os
import io
import re
import sys
import time
from datetime import datetime

intr_spd_: float = 0.0


def internet_chk_speed_(intr_spd_=0.0):
    currn_dt_tm_ = datetime.now()
    dt_tm_formt_ = currn_dt_tm_.strftime('%d/%m/%Y %H:%M')

    path_target_: str = r'www.techjob.co.il'
    path_result_ = os.path.abspath("../SalariesPrjPython/pingCheck/pingOutput/ping_speed.txt").replace('/',
                                                                                                        os.path.sep)
    print(
        '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'
        'From [ internSpeedChck.py ] :\n'
        'Current time is: ' + str(dt_tm_formt_) + '\n\n'
        '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')

    try:
        log_fl_ = io.open(path_result_, 'w')
        time.sleep(0.0)
        log_fl_.write(str(dt_tm_formt_) + '\n')
        log_fl_.close()
        os.system('ping ' + path_target_ + '>>' + path_result_)
    except FileNotFoundError:
        print(
            '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'
            'From [ internSpeedChck.py ] :\n'
            'File ' + path_result_ + ' is not exists.\n\n'
            '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')
        sys.exit(-1)

    time.sleep(0.1)
    log_fl_ = io.open(path_result_, 'r')
    print('\n Whole log:\n' + log_fl_.read())
    log_fl_.close()

    log_fl_ = io.open(path_result_, 'r')
    log_list_: list = log_fl_.readlines()
    key_words_: list = ['Minimum']
    log_idx_: int
    regex_dgt_ = re.compile(r'\d+')
    res_dgts_lst_: list = []

    for log_idx_, log_ln_ in enumerate(log_list_):
        for key_idx_, key_wrds_ in enumerate(key_words_):
            if key_words_[key_idx_] in log_list_[log_idx_]:
                res_string_ = str(log_list_[log_idx_].split())
                res_string_dgts_ = (re.findall(regex_dgt_, str(res_string_)))
                res_dgts_lst_.extend(res_string_dgts_)
                for lst_itm_ in range(len(res_dgts_lst_)):
                    res_dgts_lst_[lst_itm_] = int(res_dgts_lst_[lst_itm_])
                res_dgts_lst_ = sorted(res_dgts_lst_, key=int, reverse=True)
                intr_spd_: float = round(res_dgts_lst_[0] * 0.001, 3)
                time.sleep(intr_spd_)
                print(intr_spd_)

    log_fl_.close()
    return intr_spd_

# internet_chk_speed_()


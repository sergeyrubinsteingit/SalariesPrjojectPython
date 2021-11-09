# -*- coding: utf-8 -*-

##############################################
# Runs through the table tested. Keeps lowest
# and highest salary's value in two separate
# lists. Counts an average value for each case
# and stores in the third list. Afterwards arranges
# all three lists in combined list. Then calls
# a module which writes the result to json
# [jsonWriter.write_to_json].
##############################################

import gc as garbg_coll_
import re
import sys
import threading
import time
import traceback
from selenium.webdriver.remote.webelement import WebElement
from app import clickOnLink, jsonWriter, allPositionsList, internSpeedChck
from app.allPositionsList import position_list, position_flg_
from defaultModule import default_wbd_ as _default_wbd_

tbl_all_positions_: dict = {}
all_tbls_log_: dict = {}
web_driver_ = _default_wbd_


class AnalyzeTblCont:
    def __init__(self):

        self.cell_per_row_: int
        self.position_nm_: str = ''
        self.position_flg_: bool
        self.table_title_: WebElement

        self.tbl_row_position_: dict = {}  # arranged for Json
        self.tbl_position_collection_: dict = {}  # arranged for Json
        self.tbl_all_positions_: dict = {}  # arranged for Json
        # self.all_tbls_log_: dict  # arranged for Json
        # self.all_tbls_log_ = None  # arranged for Json

        # self.tab_cnt: int

        # A variable which value should be changed with changes in Internet speed:
        self.intrn_speed_ = internSpeedChck.intr_spd_
        self.passd_tm_ = 0.0
        self.strt_time_ = time.time()
        self.curr_tm_: float = time.time()
        self.int_spd_count: int = 0

        self.salaries_top_ = []
        self.salaries_bott_ = []
        self.salaries_average_ = []

        self.slr_highest_ = []  # arranged for Json
        self.slr_lowest_ = []  # arranged for Json
        self.slr_avr_ = []  # arranged for Json

        self.key_dct_ = []

        self.get_tbl_: WebElement
        self.nmb_of_rows_: int
        self.cell_per_row_: int

        self.conditions_ = threading.Condition()
        self.task_ = threading.Thread(target=None)
        self.task_.start()

        # self.self.int_spd_count: int

    def analyze_tbl_cont(self, _links_count_):
        print('{{{{{{{{{{{{{  Analyze Tbl Content/analyze_tbl_cont function begins  }}}}}}}}}}}}}')

        internSpeedChck.internet_chk_speed_()
        int_spd_count = 0

        def call_intr_speed(_int_spd_count):
            while self.int_spd_count < 20:
                self.int_spd_count += 1
                print('call_intr_speed(self.int_spd_count) : self.int_spd_count = ' + str(self.int_spd_count))
                time.sleep(self.intrn_speed_)
                self.conditions_.acquire()
            else:
                print('#:>D ' * 100)
                internSpeedChck.internet_chk_speed_()  # Call a function to get a current Internet speed
                self.intrn_speed_ = internSpeedChck.intr_spd_
                time.sleep(self.intrn_speed_)
                self.conditions_.notify()
                self.conditions_.release()
                return self.intrn_speed_

        self.conditions_ = threading.Condition()
        # noinspection PyTypeChecker
        self.task_ = threading.Thread(target=call_intr_speed(int_spd_count))
        self.task_.start()

        allPositionsList.position_flg_ = False

        print('_links_count_ = ' + str(_links_count_))

        get_tbl_ = web_driver_.find_element_by_tag_name('tbody')
        time.sleep(1)

        nmb_of_rows_ = get_tbl_.find_elements_by_tag_name('tr').__len__()
        cell_per_row_ = 0

        for cell_with_txt_ in range(0, get_tbl_.find_elements_by_tag_name('tr')[1].find_elements_by_tag_name(
                'td').__len__()):
            if get_tbl_.find_elements_by_tag_name('tr')[1].find_elements_by_tag_name('td')[cell_with_txt_].text != '':
                cell_per_row_ += 1
        time.sleep(self.intrn_speed_)
        print('<<<<<<<< Var self.intrn_speed_ = ' + str(self.intrn_speed_) + ' Msg 1; from AnalizeContent >>>>>>>>')

        print('cell_per_row_ = ' + str(cell_per_row_) + '+-' * 70 + '\n')
        print('\n(((((((((((((( clickOnLink.links_count_ = ' + str(_links_count_) + ' )))))))))))))\n')

        salaries_top_ = []
        regex_top_ = re.compile(r'\d+(?!.*-)')

        salaries_bott_ = []
        regex_bott_ = re.compile(r'^\d+?(?=-\d)')

        salaries_average_ = []

        key_dct_ = []

        slr_highest_ = []  # arranged for Json
        slr_lowest_ = []  # arranged for Json
        slr_avr_ = []  # arranged for Json

        self.table_title_ = web_driver_.find_elements_by_class_name('SalaryTableTitle_salaryTableTitle__RQsQt')[0].text
        print('\n' + '+-' * 70 + '\n')
        print('The  TABLE\'\s title is: ' + self.table_title_)
        print('\n' + '+-' * 70 + '\n')

        for row_nmb_ in range(1, nmb_of_rows_):
            self.position_nm_ = get_tbl_.find_elements_by_tag_name('tr')[row_nmb_].find_elements_by_tag_name('td')[
                0].text
            time.sleep(self.intrn_speed_)
            print('<<<<<<<< Var self.intrn_speed_ = ' + str(self.intrn_speed_) + ' Msg 2; from AnalizeContent >>>>>>>>')
            position_list(self.position_nm_, position_flg_)
            time.sleep(self.intrn_speed_)
            print('<<<<<<<< Var self.intrn_speed_ = ' + str(self.intrn_speed_) + ' Msg 3; from AnalizeContent >>>>>>>>')

            # Gets header text for each column;
            # Replaces Hebrew with English;
            # Forms a dictionary of keywords for further usage in Json files
            for cell_nmb_ in range(1, cell_per_row_):  # For all the cells in the row
                key_wrd_ = get_tbl_.find_elements_by_tag_name('tr')[0].find_elements_by_tag_name('th')[cell_nmb_].text
                key_wrd_ = key_wrd_.replace('שנים', 'years')
                key_wrd_ = key_wrd_.replace('תחום', 'field')
                key_wrd_ = key_wrd_.replace('ניהול', 'Management')
                key_dct_.append(key_wrd_)

                # From each cell in the row gets text, if the text exists
                # and remove 'ש"ח' word in Hebrew
                cell_txt_ = get_tbl_.find_elements_by_tag_name('tr')[row_nmb_].find_elements_by_tag_name('td')[
                    cell_nmb_].text
                cell_txt_ = cell_txt_.replace('ש"ח', '')
                if cell_txt_ != '':
                    cell_txt_ = cell_txt_
                else:
                    cell_txt_ = '1'
                # Copies high salary digital values only to new list:
                top_value_: list = re.findall(regex_top_, cell_txt_)
                salaries_top_.extend(top_value_)
                salaries_top_ = [list_item_ for list_item_ in salaries_top_ if
                                 list_item_ != []]  # Clears empty spaces in the list
                # Copies low salary digital values only to new list
                bott_value_ = re.findall(regex_bott_, cell_txt_)
                salaries_bott_.extend(bott_value_)
                salaries_bott_ = [list_item_ for list_item_ in salaries_bott_ if
                                  list_item_ != []]  # Clears empty spaces in the list
                # Forms a dictionary - high salaries:
                slr_highest_.append({key_dct_[cell_nmb_ - 1]: salaries_top_[cell_nmb_ - 1]})
                time.sleep(self.intrn_speed_ / 2)
                print('<<<<<<<< Var self.intrn_speed_ = ' + str(
                    self.intrn_speed_) + ' Msg 4; from AnalizeContent >>>>>>>>')
                slr_lowest_.append({key_dct_[cell_nmb_ - 1]: salaries_bott_[cell_nmb_ - 1]})
                time.sleep(self.intrn_speed_)
                print('<<<<<<<< Var self.intrn_speed_ = ' + str(
                    self.intrn_speed_) + ' Msg 5; from AnalizeContent >>>>>>>>')
                # Calculates an average salary and forms a corresponding dictionary:
                if cell_nmb_ + 1 == cell_per_row_:
                    salaries_average_.clear()
                    slr_avr_.clear()
                    for avrg_cnt_ in range(0, len(salaries_top_)):
                        slr_avrg_ = (int(salaries_top_[avrg_cnt_]) + int(salaries_bott_[avrg_cnt_])) / 2
                        salaries_average_.append(slr_avrg_)
                        slr_avr_.append({key_dct_[avrg_cnt_]: slr_avrg_})
                    time.sleep(1)
                    self.tbl_row_position_[
                        '[ Highest ]'] = slr_highest_  # Here goes a HIGH salary for specified position
                    self.tbl_row_position_['[ Lowest ]'] = slr_lowest_  # Here goes a LOW salary for specified position
                    self.tbl_row_position_[
                        '[ Average ]'] = slr_avr_  # Here goes an AVERAGE salary for specified position

                    time.sleep(self.intrn_speed_)
                    print('<<<<<<<< Var self.intrn_speed_ = ' + str(
                        self.intrn_speed_) + ' Msg 6; from AnalizeContent >>>>>>>>')

                    self.tbl_all_positions_[
                        str(self.position_nm_)] = self.tbl_row_position_  # All positions for specified field
                    time.sleep(0.05)
                    self.tbl_row_position_ = {}

            if row_nmb_ == nmb_of_rows_ - 1:
                all_tables_logging(self.table_title_, self.position_nm_,
                                   self.tbl_all_positions_)  # adds all tables' data to united dictionary; sends the dict to be written to Json
                time.sleep(self.intrn_speed_)
                print('<<<<<<<< Var self.intrn_speed_ = ' + str(
                    self.intrn_speed_) + ' Msg 7; from AnalizeContent >>>>>>>>')
                self.tbl_all_positions_ = {}

        print('<<<<<<< analyzeTableContent: len(web_driver_.window_handles) = ' + str(
            len(web_driver_.window_handles)) + ' >>>>>>>')
        print('<<<<<<< analyzeTableContent: len(clickOnLink.all_links_) = ' + str(
            len(clickOnLink.all_links_)) + ' >>>>>>>')
        time.sleep(1)
        return self.tbl_all_positions_


if __name__ == '__main__':
    AnalyzeTblCont()


def all_tables_logging(_table_title_, _position_nm_, _tbl_all_positions_):
    all_tbls_log_[str(_table_title_)] = _tbl_all_positions_  # All the fields with corresponding positions

    if len(clickOnLink.all_links_) + 1 == len(web_driver_.window_handles):
        print('All tables log:\n' + str(all_tbls_log_))
        jsonWriter.write_to_json(all_tbls_log_)
        time.sleep(1)
        try:
            allPositionsList.position_flg_ = True
            position_list(_position_nm_, position_flg_)
        except TypeError:
            print('From Analize... print position list:')
            traceback.print_exc()
            # web_driver_.quit()
        web_driver_.quit()

# Here runs a garbage collector
garbg_coll_.enable()

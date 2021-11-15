# -*- coding: Windows-1255 -*-

#####################################
# This module writes a data
# gathered in the tested site (tables' data)
# into json.
#####################################
from defaultModule import default_wbd_ as _default_wbd_
import gc as garbg_coll_
import json
import os
import sys
import time
import io

count_write_js_: int = 0
encoding_obj_: str = ''
logs_collector_: dict = {}
js_dir_path_ = '../SalariesPrjPython/json_files/'


def write_to_json(all_tbls_cont_):
    global encoding_obj_, path_to_json_file_

    print('all_tbls_cont_ are ' + str(all_tbls_cont_) + '\n')
    print(
        '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'
        'From [ jsonWriter.py ] :\n'
        'Total of tables tested: ' + str(all_tbls_cont_) + '\n\n'
        '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')

    enc_lst_ = ['iso-8859-8', 'cp1252', 'utf-8', 'Windows-1255']
    print(
        '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'
        'From [ jsonWriter.py ] :\n'
        'Encoding list contains:\n ' + str(enc_lst_) + '\n\n'
        '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')

    for enc_from_lst_ in (enc_lst_):
        path_to_json_file_ = js_dir_path_ + 'all_tables_log_' + str(enc_from_lst_) + '.json'
        print(
            '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'
            'From [ jsonWriter.py ] :\n'
            'File is: ' + str(path_to_json_file_) + '\n'
            'Encoding is: ' + str(enc_from_lst_) + '\n\n'
            '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')

        with io.open(path_to_json_file_, 'w', encoding=enc_from_lst_) as json_rep_:
            time.sleep(5)
            if os.path.exists(path_to_json_file_):

                try:
                    all_tbls_encoded_ = str(all_tbls_cont_).encode(encoding=enc_from_lst_, errors='strict').decode(
                        enc_from_lst_, errors='strict')
                    time.sleep(0.05)
                    json.dump(all_tbls_encoded_, json_rep_, ensure_ascii=False)
                    json_rep_.close()
                    time.sleep(0.2)
                    working_encod_ = enc_from_lst_
                    time.sleep(1)
                    read_jsons(working_encod_, path_to_json_file_)
                except UnicodeError:
                    print('jsonWriter: UnicodeError:\n' + str(UnicodeError))
                    print(
                        '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'
                        'From [ jsonWriter.py ] :\n'
                        'UnicodeError:\n' + str(UnicodeError) + '\n\n'
                        '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')
                    json_rep_.close()
                    time.sleep(0.05)
                    os.remove(path_to_json_file_)
                    continue
            else:
                print(
                    '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'
                    'From [ jsonWriter.py ] :\n'
                    'File ' + str(path_to_json_file_) + ' was not found.\n\n'
                    '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')
    _default_wbd_.quit()
    sys.exit()


def read_jsons(work_enc_, _path_to_json_file_):
    print(
        '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'
        'From [ jsonWriter.py ] :\n'
        'Function [ read_jsons ] begins.\n'
        'Function [ read_jsons ] : working encoding is: ' + str(work_enc_) + '\n\n'
        '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')

    with io.open(_path_to_json_file_, 'r', encoding=str(work_enc_)) as open_fl_:
        print(
            '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'
            'From [ jsonWriter.py ] :\n'
            'Function [ read_jsons ] : open_fl_: ' + str(open_fl_) + '\n'
            'Function [ read_jsons ] : working encoding is: ' + str(work_enc_) + '\n\n'
            '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')

        try:
            time.sleep(0.1)
            json_fl_txt_ = open_fl_.readline()
            print(
                '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'
                'From [ jsonWriter.py ] :\n'
                'Function [ read_jsons ] : Text from Json: ' + json_fl_txt_ + '\n\n'
                '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')
        except FileNotFoundError:
            time.sleep(0.1)
            print(
                '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'
                'From [ jsonWriter.py ] :\n'
                'Function [ read_jsons ] : File ' + str(open_fl_) + ' not found.\n\n'
                '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')
        time.sleep(2)


# Garbage collector
garbg_coll_.enable()

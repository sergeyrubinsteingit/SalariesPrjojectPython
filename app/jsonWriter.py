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

    enc_lst_ = ['iso-8859-8', 'cp1252', 'utf-8', 'Windows-1255']
    print('write_to_json: enc_lst_ is ' + str(enc_lst_))

    for enc_from_lst_ in (enc_lst_):
        path_to_json_file_ = js_dir_path_ + 'all_tables_log_' + str(enc_from_lst_) + '.json'

        print('write_to_json: File is ' + str(path_to_json_file_))
        print('write_to_json: Encoding is ' + str(enc_from_lst_))

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
                    json_rep_.close()
                    time.sleep(0.05)
                    os.remove(path_to_json_file_)
                    continue
            else:
                print('((((( File ' + path_to_json_file_ + ' was not found )))))')
    _default_wbd_.quit()
    sys.exit()


def read_jsons(work_enc_, _path_to_json_file_):
    print('&&&&&&&&&&&  read_jsons begins  &&&&&&&&&&&')
    print('&&&&&&&&&&&  read_jsons: working_encod_ is ' + str(work_enc_) + '  &&&&&&&&&&&')

    with io.open(_path_to_json_file_, 'r', encoding=str(work_enc_)) as open_fl_:
        print('((((((((((((((((( read_jsons(): open_fl_: ' + str(open_fl_) + ')))))))))))))))))')
        print('{{{{{{ read_jsons(): working_encod_ is ' + str(work_enc_) + ' }}}}}}')

        try:
            time.sleep(0.1)
            json_fl_txt_ = open_fl_.readline()
            print('******->  ' + json_fl_txt_)
        except FileNotFoundError:
            time.sleep(0.1)
            print('{{{{read_jsons(): File ' + str(open_fl_) + ' not found}}}}')
        time.sleep(2)


garbg_coll_.enable()

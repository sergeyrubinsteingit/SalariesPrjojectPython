# -*- coding: Windows-1255 -*-
from __future__ import absolute_import

import threading

from . import analyzeTableContent

from . import translateHebEn

event_: threading.Event = threading.Event()
set_thread_ = threading.Thread()
set_thread_.start()


class PassTrans(object):

    def __init__(self):

        # cell_txt_ = 'בודק תוכנה'
        cell_txt_ = analyzeTableContent.position_nm_

        translateHebEn.trans_in_google(cell_txt_)

        while translateHebEn.trns_flg_ is not True:
            event_.wait()
        else:
            print('From test, [cell_txt_]: ' + cell_txt_)
            event_.set()
            # translateHebEn.web_driver_.quit()
            # sys.exit(0)

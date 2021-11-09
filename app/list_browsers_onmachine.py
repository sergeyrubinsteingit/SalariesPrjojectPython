import os
import subprocess
import sys

browser_hint_: list = ['firefox', 'chrome', 'edge', 'ie', 'opera', 'safari']
browser_names_: list = []


def run_batch_browsers_list():
    print('>>>>>   browsers_list.bat  >>>>>>> '
          + os.path.abspath("../SalariesPrjPython/ListBrowsers/browsers_list.bat").replace('/', os.path.sep))
    from app.combo_Box import call_combo_box
    list_browsers_ = subprocess.check_output(os.path.abspath("../SalariesPrjPython/ListBrowsers/browsers_list.bat").replace('/', os.path.sep))
    # creates and overwrites the browsers_py_.txt:
    brws_listfile_ = open(os.path.abspath("../SalariesPrjPython/ListBrowsers/browsers_py_.txt").replace('/', os.path.sep), "w")
    brws_listfile_.write(str(list_browsers_))
    brws_listfile_.close()

    # opens and read the browsers_py_.txt:
    brws_listfile_ = open(os.path.abspath("../SalariesPrjPython/ListBrowsers/browsers_py_.txt").replace('/', os.path.sep), "r")
    str_browsers_ = str(brws_listfile_.read().lower())
    browser_names_.append('Select a browser:')
    for brw_name_ in browser_hint_:
        if brw_name_ in str_browsers_:
            if brw_name_ == "ie":
                brw_name_ = "explorer"
            browser_names_.append(str(brw_name_).capitalize())
    print(str("browser_names_" + str(browser_names_)))
    brws_listfile_.close()

    # runs combobox
    try:
        subprocess.run([call_combo_box(browser_names_)], timeout=5)
    except subprocess.TimeoutExpired as time_exp_:
        print('Problem in running a combobox')
        print(time_exp_)
        sys.exit(0)


if __name__ == '__main__':
    run_batch_browsers_list()

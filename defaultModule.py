import time
from app import browserStatus
from tkinter import SW
import requests.exceptions
import requests

try:
    import Tkinter
except ImportError:
    import tkinter

wn_wdt: int = 400
wn_hgt: int = 200

msg_root_: tkinter.Tk = tkinter.Tk()
msg_wn_ = tkinter.Toplevel(msg_root_)

cvs_wn_: tkinter.Canvas
lbl_txt_: str


class StartBrowser:

    def __init__(self):
        try:
            send_request_ = requests.get(browserStatus.BrowserStatus.get_url_)
            time.sleep(1)
            if send_request_.status_code == 200:
                browserStatus.BrowserStatus.wbd_.get(browserStatus.BrowserStatus.get_url_)
                time.sleep(1)
                dia_box_()
        #       browser_status.wbd_.maximize_window()
        except requests.ConnectionError:
            print("No server connection\n")
            browserStatus.BrowserStatus.wbd_.quit()
            SystemExit(-1)


def keep_cookies():
    msg_root_.destroy()
    print("\nSleep quite, your cookies stay with you\n+++++++++++++++++++++++++++++++++++++++++++++++++++")
    wait_box_and_list()


def delete_cookies():
    msg_root_.destroy()
    browserStatus.BrowserStatus.wbd_.delete_all_cookies()
    time.sleep(0.5)
    wait_box_and_list()

    print("\nThe cookies had been deleted\n+++++++++++++++++++++++++++++++++++++++++++++++++++")


def wait_box_and_list():
    write_link_list()


def dia_box_():
    global cvs_wn_, lbl_txt_
    lbl_txt_ = '\n\n\nIt\'s recommended to delete all cookies ' \
               f'\n as they can prevent the test  ' \
               f'\nfrom being accomplished properly. ' \
               f'\n\nDelete the cookies? \n\n\n'

    msg_wn_.title("Keep or delete cookies")
    msg_root_.transient()
    msg_root_.geometry('400x200')
    msg_wn_.configure(bg='#120f6b')
    msg_root_.focus()
    msg_root_.update_idletasks()

    # msg_root_.overrideredirect(1)
    msg_root_.withdraw()

    cvs_wn_ = tkinter.Canvas(msg_wn_, width=wn_wdt, height=wn_hgt, bg="#120f6b", bd=0, relief="ridge")
    cvs_wn_.create_text(140, 80, fill='#ffffff', font='Helvetica 9 italic bold', text=lbl_txt_)
    cvs_wn_.grid(column=0, row=0, columnspan=2, rowspan=2)

    btn1_ = tkinter.Button(msg_wn_, text="Delete them all", bg="black", fg="#ffffff",
                           font="Helvetica 8 bold", command=delete_cookies)
    btn1_.place(x=100, y=175, anchor=SW, width=125, height=40)
    btn2_ = tkinter.Button(msg_wn_, text="Keep away \nfrom my cookies!", bg="black", fg="#ffffff",
                           font='Helvetica 8 bold', command=keep_cookies)
    btn2_.place(x=245, y=175, anchor=SW, width=125, height=40)

    msg_root_.mainloop()

    return lbl_txt_


def write_link_list():
    from app import createLinkListXML
    time.sleep(2)
    print('\nBrowser and Links \n####################')
    web_driver_ = browserStatus.BrowserStatus.wbd_

    ol_tag_ = web_driver_.find_element_by_xpath('//*[@id="__next"]/div/main/div[3]/div[2]/ol[2]')
    li_tag_ = ol_tag_.find_elements_by_tag_name("li")
    li_tag_list_ = []
    count_: int = 0
    for childNode in range(len(li_tag_)):
        current_li_tag_ = li_tag_[count_]
        link_txt_ = current_li_tag_.find_element_by_tag_name("a")
        #    print(link_txt_.text)
        li_tag_list_.append(link_txt_.text)
        count_ += 1

    print('from KEEP_cookies: WaitBox starts')

    time.sleep(0.5)
    createLinkListXML.create_xml(li_tag_list_)
    print('from start_wait_box(): WaitBox starts')
    # import waitPopUpBox
    # waitPopUpBox.WaitBox(waitPopUpBox.cvs_wn_, waitPopUpBox.lbl_txt_, waitPopUpBox.tm_, waitPopUpBox.tm_cnt_,
    #                     waitPopUpBox.cnt_range_, waitPopUpBox.msg_root_2_)'''


if __name__ == '__main__':
    StartBrowser()
import time
import tkinter

cvs_wn_: tkinter.Label
lbl_txt_: str = ''
tm_: int = 0
tm_cnt_: int = 0
cnt_range_: int = 100

wn_wdt: int = 400
wn_hgt: int = 300

flg_click_: bool
flg_click_ = False


class WaitBox(object):
    print('\nclass WaitBox begins\n_________________________________\n')

    def __init__(self, cvs_wn_, lbl_txt_, tm_, tm_cnt_, cnt_range_, msg_root_2_):

        self.cvs_wn_ = cvs_wn_
        self.lbl_txt_ = lbl_txt_
        self.tm_ = tm_
        self.tm_cnt_ = tm_cnt_
        self.cnt_range_ = cnt_range_
        self.msg_root_2_ = msg_root_2_
        #self.msg_wn_2_ = msg_wn_2_
        #self.flg_click_ = flg_click_

        # msg_root_2_.withdraw()
        # msg_root_2_.update_idletasks()

        time.sleep(1)
        self.change_label()

        #self.msg_root_2_.mainloop()

        print('\nclass WaitBox, method __init__ begins\n_________________________________\n')

    def change_label(self):
        print('Change label\n' + str(self.lbl_txt_))

        while self.tm_ < 100:
            #    print('change_label: the_request_ = ' + str(getSalaryInfo.open_link().th))
            self.tm_ += 1
            self.tm_cnt_ = self.cnt_range_ - self.tm_
            self.lbl_txt_ = 'Please wait till the program builds XML file.' \
                            f'\nThis window will disappear then the file is ready' \
                            f'\nProcessing of this file may take a while.' \
                            f'\n {str(self.tm_)}% is ready.'

            cvs_wn_.config(text=self.lbl_txt_)
            self.cvs_wn_.after(200, self.change_label)
            self.cvs_wn_.mainloop()

        if self.tm_ > 100:
            self.cvs_wn_.after_cancel(id)
            import openLinksAsTabs
        #    getSalaryInfo.kill_wn()
            return


msg_root_2_: tkinter.Tk = tkinter.Tk()
#   msg_wn_2_ = tkinter.Toplevel(msg_root_2_)
msg_root_2_.geometry('400x300')
msg_root_2_.title('Please wait till a file is processed')
msg_root_2_.transient()
msg_root_2_.focus()
cvs_wn_ = tkinter.Label(msg_root_2_, width=wn_wdt, height=wn_hgt, bg="#120f6b")
cvs_wn_.place(x=40, y=30)
cvs_wn_.config(font=('Helvetica', 16))
cvs_wn_.config(fg='#0000ee')
cvs_wn_.pack()


#   app = WaitBox(cvs_wn_, lbl_txt_, tm_, tm_cnt_, cnt_range_, msg_root_2_, msg_wn_2_, flg_click_)
import sys
import tkinter as tk_inter_
from tkinter import ttk as get_ttk_


combo_win_ = tk_inter_.Tk()
# creates combobox
string_var_ = tk_inter_.StringVar
combo_entries_ = get_ttk_.Combobox(combo_win_, width=30, textvariable=string_var_)


def call_combo_box(_brows_names_):
    # creates combo window
    combo_win_.title('Select a browser')
    combo_win_.geometry('250x200')
    combo_win_.configure(bg='orange')
    combo_win_.eval('tk::PlaceWindow . center')  # Centers a combo in the os window
    combo_win_.attributes('-topmost', True)

    # labels the window
    get_ttk_.Label(combo_win_, text="Please select a browser:",
                   background="orange", foreground="black",
                   font=(["Helvetica", "sans-serif"], 15)).place(relx=.5, rely=.2, anchor="center")

    # adds combo drop menu
    from app import openSelectedBrowser
    combo_entries_['values'] = _brows_names_
    combo_entries_.current(0)
    combo_entries_.bind("<<ComboboxSelected>>", openSelectedBrowser.open_selected_browser)
    combo_entries_.place(relx=.5, rely=.4, anchor="center")

    # adds quit button
    get_ttk_.Button(combo_win_, text="Cancel the test",
                    command=cancel_test).place(relx=.5, rely=.8, anchor="center")

    combo_win_.mainloop()


def cancel_test():
    combo_win_.destroy()
    sys.exit(0)



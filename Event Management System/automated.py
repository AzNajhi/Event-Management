from tkinter import *
from tkinter import messagebox
import options
import autotable

def auto_ui(root, auto_button, manual_button):
    # 1 Remove automated & manual button
    auto_button.destroy()
    manual_button.destroy()

    # 2 Creating widgets for automated planning UI
    global frame_dsa_id
    global frame_dsa
    global frame_staffid
    global days_label
    global days_entry
    global session_label
    global session_entry
    global attend_label
    global attend_entry
    global staffid_label
    global entry_list

    frame_dsa_id = Frame(root)
    frame_dsa = Frame(frame_dsa_id)
    frame_staffid = Frame(frame_dsa_id)

    void_label = Label(frame_dsa, text="", font=("TkDefaultFont 10"))
    days_label = Label(frame_dsa, text="Days:", font=("TkDefaultFont 10"))
    days_entry = Entry(frame_dsa, width=10, font=("TkDefaultFont 10"),
                    validate="key", validatecommand=(root.register(validate_number), "%P"))
    session_label = Label(frame_dsa, text="Sessions:", font=("TkDefaultFont 10"))
    session_entry = Entry(frame_dsa, width=10, font=("TkDefaultFont 10"),
                    validate="key", validatecommand=(root.register(validate_number), "%P"))
    attend_label = Label(frame_dsa, text="Attendants:", font=("TkDefaultFont 10"))
    attend_entry = Entry(frame_dsa, width=10, font=("TkDefaultFont 10"),
                    validate="key", validatecommand=(root.register(validate_number), "%P"))
    entry_list = [Entry(frame_staffid, width=15, font=("TkDefaultFont 10"))]
    staffid_label = Label(frame_staffid, text="Staff IDs:", font=("TkDefaultFont 10"))
    plus_button = Button(frame_staffid, pady=0.5,text="+", command=lambda: add_entry(plus_button, minus_button))
    minus_button = Button(frame_staffid, pady=0.5, text="-", command=lambda: remove_entry(plus_button, minus_button), state=DISABLED)

    cont_button = Button(root, text="Continue", font=("TkDefaultFont 10"), command=lambda: conti(root))
    back_button = Button(root, padx=10, text="Back", font=("TkDefaultFont 10"), command=lambda: back(root, frame_dsa, frame_staffid, cont_button, back_button))

    display_widget(void_label, plus_button, minus_button, cont_button, back_button)

# Displaying widgets
def display_widget(void_label, plus_button, minus_button, cont_button, back_button):
    frame_dsa.grid(row=1, column=0, padx=10, pady=25, sticky=N)
    frame_staffid.grid(row=1, column=1, padx=10, pady=25, sticky=N)
    frame_dsa_id.grid(row=1, columnspan=2, padx=20, sticky=N)

    void_label.grid(row=0, columnspan=2)
    days_label.grid(row=1 , column=1, sticky=E)
    days_entry.grid(row=1, column=2, padx=5)
    session_label.grid(row=2, column=1, sticky=E)
    session_entry.grid(row=2, column=2, padx=5)
    attend_label.grid(row=3, column=1, sticky=E)
    attend_entry.grid(row=3, column=2, padx=5)

    staffid_label.grid(row=0, column=0)
    plus_button.grid(row=0, column=1)
    minus_button.grid(row=0, column=2)
    for x in range(len(entry_list)):
        entry_list[x].grid(row=x+1, columnspan=3)

    cont_button.grid(row=2, column=1, sticky=E, padx=20, pady=10)
    back_button.grid(row=2, column=0, sticky=W, padx=20, pady=10)

def add_entry(plus_button, minus_button):
    if len(entry_list) < 10:
        new_entry = Entry(frame_staffid, width=15, font=("TkDefaultFont 10"))
        entry_list.append(new_entry)
        new_entry.grid(row=len(entry_list), columnspan=3)
        update_buttons(plus_button, minus_button)

def remove_entry(plus_button, minus_button):
    if len(entry_list) > 1:
        removed_entry = entry_list.pop()
        removed_entry.grid_remove()
        update_buttons(plus_button, minus_button)

def update_buttons(plus_button, minus_button):
    if len(entry_list) > 0:
        plus_button.config(state=NORMAL)
        minus_button.config(state=NORMAL)
    else:
        minus_button.config(state=DISABLED)

def conti(root):
    if days_entry.get() == "" or session_entry.get() == "" or attend_entry.get() == "":
        messagebox.showinfo("Warning Message", f"Please insert all Days, Sessions and Attendants fields.")
        return
    days = int(days_entry.get())
    sessions = int(session_entry.get())
    attendants = int(attend_entry.get())
    remove_duplicate()
    staffid_list = []
    for x in entry_list:
        if x.get() != "":
            staffid_list.append(x.get())
    autotable.arrange_table(root, days, sessions, attendants, staffid_list)

def remove_duplicate():
    global entry_list
    entry_set = set()
    new_entry_list = []
    for x in entry_list:
        if x.winfo_exists():
            value = x.get()
            if value not in entry_set:
                entry_set.add(value)
                new_entry_list.append(x)
            else:
                x.destroy()
    entry_list = new_entry_list

def validate_number(entry):
    if entry == "" or entry.isnumeric():
        return True
    else:
        return False

def back(root, frame_dsa, frame_staffid, cont_button, back_button):
    frame_dsa.destroy()
    frame_staffid.destroy()
    cont_button.destroy()
    back_button.destroy()
    options.options(root)
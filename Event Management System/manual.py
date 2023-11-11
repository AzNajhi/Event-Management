from tkinter import *
from tkinter import messagebox
import options
import manualtable

def manual_ui(root, auto_button, manual_button):
    # Remove automated & manual button
    auto_button.destroy()
    manual_button.destroy()

    # Creating widgets for manual planning UI
    global days_entry
    global session_entry
    global attend_entry

    frame = Frame(root)

    days_label = Label(frame, text="Days:", font=("TkDefaultFont 10"))
    days_entry = Entry(frame, width=10, font=("TkDefaultFont 10"), 
                validate="key", validatecommand=(root.register(validate_number), "%P"))

    session_label = Label(frame, text="Sessions:", font=("TkDefaultFont 10"))
    session_entry = Entry(frame, width=10, font=("TkDefaultFont 10"),
                    validate="key", validatecommand=(root.register(validate_number), "%P"))

    attend_label = Label(frame, text="Attendants:", font=("TkDefaultFont 10"))
    attend_entry = Entry(frame, width=10, font=("TkDefaultFont 10"),
                    validate="key", validatecommand=(root.register(validate_number), "%P"))

    cont_button = Button(root, text="Continue", font=("TkDefaultFont 10"), command=lambda: conti(root))
    back_button = Button(root, padx=10, text="Back", font=("TkDefaultFont 10"), command=lambda: back(root, frame, cont_button, back_button))

    #Displaying widgets
    frame.grid(row=1, columnspan=2, pady=30, sticky=N)

    days_label.grid(row=0 , column=0, sticky=E)
    days_entry.grid(row=0, column=1, padx=5)
    session_label.grid(row=1, column=0, sticky=E)
    session_entry.grid(row=1, column=1, padx=5)
    attend_label.grid(row=2, column=0, sticky=E)
    attend_entry.grid(row=2, column=1, padx=5)

    cont_button.grid(row=2, column=1, sticky=E, padx=20, pady=10)
    back_button.grid(row=2, column=0, sticky=W, padx=20, pady=10)

def conti(root):
    if days_entry.get() == "" or session_entry.get() == "" or attend_entry.get() == "":
        messagebox.showinfo("Warning Message", f"Please insert all Days, Sessions and Attendants fields.")
        return
    days = int(days_entry.get())
    sessions = int(session_entry.get())
    attendants = int(attend_entry.get())
    manualtable.arrange_table(root, days, sessions, attendants)

def validate_number(entry):
    if entry == "" or entry.isnumeric():
        return True
    else:
        return False

def back(root, frame, cont_button, back_button):
    cont_button.destroy()
    back_button.destroy()
    frame.destroy()
    options.options(root)
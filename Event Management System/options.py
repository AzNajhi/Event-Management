from tkinter import *
import automated
import manual

def options(root):
    #Create Widget
    frame = Frame(root)
    title = Label(root, text="Event Management System:",
                padx=20 ,pady= 10,
                font=("TkDefaultFont 12 bold"))
    auto_button = Button(frame, text="Automated Planning",
                        padx=24, pady=10,
                        font=("TkDefaultFont 10"),
                        command=lambda: automated.auto_ui(root, auto_button, manual_button))
    manual_button = Button(frame, text="Manual Planning",
                        padx=35, pady=10,
                        font=("TkDefaultFont 10"),
                        command=lambda: manual.manual_ui(root, auto_button,manual_button))

    # Display Widget
    frame.grid(row=1, columnspan=2, pady=30, padx=30, sticky=N)
    title.grid(row=0, columnspan=2, sticky=N)
    auto_button.grid(row=0, columnspan=2, padx=15, sticky=N)
    manual_button.grid(row=1, columnspan=2, padx=15, sticky=N)
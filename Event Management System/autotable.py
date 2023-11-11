from tkinter import *
from tkinter import messagebox
import autosave
import random

class Sessions:
    def __init__(self):
        self.assigned_staff = []
        self.button = None
        self.label = None
    
    def session_clicked(self):
        for x in range(days):
            for y in range(sessions):
                if session_list[x][y].button == self.button:
                    session_list[x][y].label.grid(row=0, pady=10, sticky=S)
                    session_list[x][y].button.config(state="disabled")
                else:
                    session_list[x][y].label.grid_forget()
                    session_list[x][y].button.config(state="normal")
    
def arrange_table(root, day, session, attendant, staffid_list):

    # Creating list of sessions
    global days
    global sessions
    global attendants
    global session_list

    days = day
    sessions = session
    attendants = attendant
    session_list = [[[0 for _ in range(attendants)]
                for _ in range(sessions)]
                for _ in range(days)]

    # Calculating total staff needed
    totalstaff_needed = 0
    for x in range(days):
        for y in range(sessions):
            staff_needed = attendants // 10 
            if attendants % 10 != 0:
                staff_needed += 1
            totalstaff_needed += staff_needed

    assigned_list = []
    totalstaff_given = len(staffid_list)
    for x in range(days):
        for y in range(sessions):
            if totalstaff_needed <= totalstaff_given:

                # Creating session objects and adding them into the list
                session_list[x][y] = Sessions()
                for z in range(staff_needed):
                    remaining = len(staffid_list)

                    # Assigning staffs as session objects' attribute randomly
                    staffid = staffid_list.pop(random.randint(0, remaining-1))
                    if staffid != "" and staffid not in assigned_list:
                        session_list[x][y].assigned_staff.append(staffid)
                        assigned_list.append(staffid)
            else:
                display_warning(totalstaff_needed, totalstaff_given)
                return
    
    # Proceed to create widget to display event schedule when requirements are met
    if len(assigned_list) == totalstaff_needed:
        table_window = Toplevel(root)
        frame_assignedstaff = Frame(table_window)
        frame_table = Frame(table_window)
        table_window.title("Automated Planning Table")
        save_button = Button(table_window, padx=20, text="Save", font=("TkDefaultFont 10"), command=lambda: autosave.save(session_list, days, sessions))
        save_button.grid(row=2, padx=20, pady=10, sticky=E)
        days_label = []
        for x in range(days):
            day = Label(frame_table, text=f"Day {x+1}")
            days_label.append(day)
            for y in range(sessions):
                session_list[x][y].label = Label(frame_assignedstaff, text=f"Assigned Staff: {session_list[x][y].assigned_staff}", font=("TkDefaultFont 10"))
                frame_assignedstaff.grid(row=0, sticky=N)
                session_list[x][y].button = Button(frame_table, text=f"Session {y+1}", width=10, height=4)
                session_list[x][y].button.config(command=session_list[x][y].session_clicked)
        display_table(days_label, sessions, frame_table)

# Displaying schedule
def display_table(days_label, sessions, frame_table):
    for x in range(days):
        days_label[x].grid(row=x, column=0, padx=10)
        for y in range(sessions):
            session_list[x][y].button.grid(row=x, column=y+1)
    frame_table.grid(row=1, padx=20, pady=20, sticky=N)

def display_warning(totalstaff_needed, totalstaff_given):
    messagebox.showinfo("Warning Message", f"Insufficient Staff! Please provide {totalstaff_needed-totalstaff_given} more staff(s).")
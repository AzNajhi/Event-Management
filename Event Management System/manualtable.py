from tkinter import *
import manualsave

class Sessions:
    def __init__(self):
        self.form_dict = {}
        self.button = None
        self.label = None
        self.color = None

    def session_clicked(self):
        self.remove_duplicates()
        message = self.check_duplicates()
        self.display_form()
        self.update_color()
        self.check_requirement(message)
        
    def remove_duplicates(self):
        for x in range(days):
            for y in range(sessions):
                entry_set = set()
                new_entry_list = []
                for z in session_list[x][y].form_dict["entry_list"]:
                    if z.winfo_exists():
                        value = z.get()
                        if value not in entry_set:
                            entry_set.add(value)
                            new_entry_list.append(z)
                        else:
                            z.destroy()
                session_list[x][y].form_dict["entry_list"] = new_entry_list

    def check_duplicates(self):
        staffID_positions = {}
        for x in range(days):
            for y in range(sessions):
                for z in session_list[x][y].form_dict["entry_list"]:
                    if z.get() != "":
                        staff_id = z.get()
                        if staff_id in staffID_positions:
                            staffID_positions[staff_id].append((x, y))
                        else:
                            staffID_positions[staff_id] = [(x, y)]

        message = "Duplicate IDs found:\n"
        for staff_id, positions in staffID_positions.items():
                if len(positions) > 1:
                    positions_text = "\n".join([f"(D:{day + 1}, S:{session + 1})" for day, session in positions])
                    message += f"'{staff_id}' at {positions_text}\n"
        duplicate_message.config(text=message)
        if message == "Duplicate IDs found:\n":
            return "Proceed"
        else:
            return "Stop"

    def update_color(self):
        # Gather assigned staffID for each session
        for x in range(days):
            for y in range(sessions):
                assigned_list = []
                entry_list = session_list[x][y].form_dict["entry_list"]
                for z in range(len(entry_list)):
                    if entry_list[z].get() != "" and entry_list[z].get() not in assigned_list:
                        assigned_list.append(entry_list[z].get())

                # Update cells color
                if assigned_list:
                    ratio = attendants / len(assigned_list)
                    if ratio > 0 and ratio < 10:
                        session_list[x][y].color = "green"
                        session_list[x][y].button.configure(bg="#7ade89")
                    if ratio >= 10 and ratio < 15:
                        session_list[x][y].color = "yellow"
                        session_list[x][y].button.configure(bg="#d9de7a")
                    if ratio >= 15:
                        session_list[x][y].color = "red"
                        session_list[x][y].button.configure(bg="#e69487")
                else:
                    session_list[x][y].color = "light gray"
                    session_list[x][y].button.configure(bg="light gray")

    def display_form(self):
        for x in range(days):
            for y in range(sessions):

                # Disable clicked button and display its form
                if session_list[x][y].button == self.button:
                    session_list[x][y].form_dict.get("label").grid(row=0, column=0)
                    session_list[x][y].form_dict.get("plus_button").grid(row=0, column=1)
                    session_list[x][y].form_dict.get("minus_button").grid(row=0, column=2)
                    entry_list = session_list[x][y].form_dict.get("entry_list")
                    for z in range(len(entry_list)):
                        entry_list[z].grid(row=z+1, columnspan=3)
                    session_list[x][y].button.config(state="disabled")

                # Enable unclicked button and hide their form
                else:
                    session_list[x][y].form_dict.get("label").grid_forget()
                    session_list[x][y].form_dict.get("plus_button").grid_forget()
                    session_list[x][y].form_dict.get("minus_button").grid_forget()
                    entry_list = session_list[x][y].form_dict.get("entry_list")
                    for z in range(len(entry_list)):
                        entry_list[z].grid_forget()
                    session_list[x][y].button.config(state="normal")

    def check_requirement(self, message):
        total_green = 0
        total_yellow = 0
        total_red = 0
        total_lightgray = 0
        for x in range(days):
            for y in range(sessions):
                if session_list[x][y].color == "green":
                    total_green += 1
                if session_list[x][y].color == "yellow":
                    total_yellow += 1
                if session_list[x][y].color == "red":
                    total_red += 1
                if session_list[x][y].color == "light gray":
                    total_lightgray += 1
        yellow_percent = total_yellow/(sessions*days)
        if total_lightgray == 0 and total_red == 0 and yellow_percent <= 0.1 and message == "Proceed":
            save_button.config(state="normal")
        else:
            save_button.config(state="disabled")

    def add_entry(self):
        for x in range(days):
            for y in range(sessions):
                if session_list[x][y].form_dict["plus_button"] == self.form_dict["plus_button"]:
                    new_entry = Entry(frame_form)
                    session_list[x][y].form_dict["entry_list"].append(new_entry)
                    new_entry.grid(row=1+len(session_list[x][y].form_dict["entry_list"]), columnspan=3)
        self.update_buttons()

    def remove_entry(self):
        for x in range(days):
            for y in range(sessions):
                if session_list[x][y].form_dict["minus_button"] == self.form_dict["minus_button"]:
                    if len(session_list[x][y].form_dict["entry_list"]) > 1:
                        removed_entry = session_list[x][y].form_dict["entry_list"].pop()
                        removed_entry.grid_remove()
        self.update_buttons()

    def update_buttons(self):
        if len(self.form_dict["entry_list"]) > 0:
            self.form_dict["plus_button"].config(state=NORMAL)
            self.form_dict["minus_button"].config(state=NORMAL)
        else:
            self.form_dict["minus_button"].config(state=DISABLED)

def arrange_table(root, day, session, attendant):
    global days
    global sessions
    global attendants
    global session_list
    global table_window
    global frame_table
    global frame_form
    global frame_message
    global duplicate_message
    global save_button

    # 1 Create list of sessions
    days = day
    sessions = session
    attendants = attendant
    session_list = [[[0 for _ in range(attendants)]
                for _ in range(sessions)]
                for _ in range(days)]

    # 2 Calculate total staff needed
    totalstaff_needed = 0
    for x in range(days):
        for y in range(sessions):
            staff_needed = attendants // 10 
            if attendants % 10 != 0:
                staff_needed += 1
            totalstaff_needed += staff_needed

    # 3 Create session objects and adding them into their list 
    for x in range(days):
        for y in range(sessions):
            session_list[x][y] = Sessions()

    # 4 Create table widget to display event's schedule
    table_window = Toplevel(root)
    frame_table = Frame(table_window)
    frame_form = Frame(table_window)
    frame_message = Frame(table_window)
    table_window.title("Manual Planning Table")
    save_button = Button(table_window, padx=20, text="Save", font=("TkDefaultFont 10"), command=lambda: manualsave.save(session_list, days, sessions))
    save_button.grid(row=2, columnspan=3, padx=20, pady=10, sticky=E)
    days_label = []
    for x in range(days):
        day = Label(frame_table, text=f"Day {x+1}")
        days_label.append(day)
        for y in range(sessions):
            session_list[x][y].button = Button(frame_table, text=f"Session {y+1}", width=10, height=4, bg="light gray")
            session_list[x][y].button.config(command=session_list[x][y].session_clicked)

    # 5 Create form widgets and adding them into their dictionary
    for x in range(days):
        for y in range(sessions):
            label = Label(frame_form, text="Staff IDs:", font=("TkDefaultFont 10"))
            entry_list = [Entry(frame_form)]
            session_list[x][y].form_dict["label"] = label
            session_list[x][y].form_dict["entry_list"] = entry_list
            session_list[x][y].form_dict["plus_button"] = Button(frame_form, text="+", command=session_list[x][y].add_entry)
            session_list[x][y].form_dict["minus_button"] = Button(frame_form, text="-", command=session_list[x][y].remove_entry, state=DISABLED)

    duplicate_message = Label(frame_message, text="Duplicate IDs found:")
    # 6 Create message box widgets to display duplicate staff IDs and their positions
    display_table(days_label, duplicate_message)

# 7 Display event's schedule
def display_table(days_label, duplicate_message):
    for x in range(days):
        days_label[x].grid(row=x, column=0, padx=10)
        for y in range(sessions):
            session_list[x][y].button.grid(row=x, column=y+1)
    duplicate_message.grid(padx=20, pady=20)
    frame_table.grid(row=0, column=0, padx=10, pady=20, sticky=N)
    frame_message.grid(row=0, column=1, pady=20, sticky=N)
    frame_form.grid(row=0, column=2, padx=20, pady=20, sticky=N)
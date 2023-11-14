from tkinter import *
import options

if __name__ == "__main__":
    try:
        root = Tk()
        root.title("Mezza9 Solutions")
        root.iconbitmap(r"Icon\Mezza9-Icon.ico")
        options.options(root)
        root.mainloop()
    except Exception as e:
        print(f"An error occurred: {e}")
        input("Press Enter to exit...")
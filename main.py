from tkinter import Tk
from src.application import Application

if __name__ == "__main__":
    root = Tk()
    app = Application(master=root)
    app.mainloop()


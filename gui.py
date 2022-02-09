"""
    Simple GUI to Librus bot
"""

import tkinter as tk
from tkinter import BOTTOM

class Application(tk.Tk):
    """
        Librus GUI
    """
    def __init__(self):
        super().__init__()
        self.login, self.password  = "", ""
        self.geometry("400x300")
        self.title("Librus Bot")
        self.resizable(0, 0)

    def get_entry_values(self):
        """ Getting values from input """
        
        self.login = self.login_entry.get()
        self.password = self.password_entry.get()
        self.destroy()

    def create_elements(self):
        """ Creating and placing elements """

        self.main_label = tk.Label(text = "LOGOWANIE", font = ("Verdana", 15), fg = "red")
        self.main_label.pack(pady = 20)
        self.login_label = tk.Label(text = "Login: ", font = ("Verdana", 14))
        self.login_label.place(x = 10, y = 100)
        self.password_label = tk.Label(text = "Password: ", font = ("Verdana", 14))
        self.password_label.place(x = 10, y = 170)
        self.login_entry = tk.Entry()
        self.login_entry.place(x = 110, y = 105)
        self.password_entry = tk.Entry()
        self.password_entry.place(x = 140, y = 175)
        self.button = tk.Button(text = "Zaloguj", command = self.get_entry_values)
        self.button.pack(side=BOTTOM, pady = 20)

if __name__ == "__main__":
    app = Application()
    app.create_elements()
    app.mainloop()

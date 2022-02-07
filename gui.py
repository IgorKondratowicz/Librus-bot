import tkinter as tk
from tkinter import BOTTOM, LEFT, font

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.title("Librus Bot")
        self.resizable(0, 0)
        self.createElements()

    def getEntryValues(self):
        self.login = self.login_entry.get()
        self.password = self.password_entry.get()
        self.destroy()
    

    def createElements(self):
        #labels
        self.main_label = tk.Label(text = "LOGOWANIE", font = ("Verdana", 15), fg = "red")
        self.main_label.pack(pady = 20)

        self.login_label = tk.Label(text = "Login: ", font = ("Verdana", 14))
        self.login_label.place(x = 10, y = 100)

        self.password_label = tk.Label(text = "Password: ", font = ("Verdana", 14))
        self.password_label.place(x = 10, y = 170)

        #inputs
        self.login_entry = tk.Entry()
        self.login_entry.place(x = 110, y = 105)

        self.password_entry = tk.Entry()
        self.password_entry.place(x = 140, y = 175)

        #submit button
        self.button = tk.Button(text = "Zaloguj", command = self.getEntryValues).pack(side=BOTTOM, pady = 20)

if __name__ == "__main__":
    app = Application()
    app.mainloop()
    
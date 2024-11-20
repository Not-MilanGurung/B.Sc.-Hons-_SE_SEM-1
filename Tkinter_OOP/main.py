import tkinter as tk
from register import Register
from login import Login
class Main:

    def __init__(self, root):
        self.root = root
        self.root.title('Booking System!')
        self.root.geometry('600x400')
        self.root.config(bg='RoyalBlue')
        self.showregister()

    def showlogin(self):
        clearscreen(self)
        Login(self.root)
    
    def showregister(self):
        clearscreen(self)
        Register(self.root)
    
def clearscreen(self):
    for widget in self.root.winfo_children():
        widget.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    Main(root)
    root.mainloop()
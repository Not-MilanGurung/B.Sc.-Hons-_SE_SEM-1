import tkinter as tk

class Login:
    def __init__(self, root):
        self.root = root
        self.header()

    def header(self):
        tk.Label(text='Login Page', font='TimesNewRoman 32').grid()
        tk.Button(text='Register page', command=self.gotologin).grid()
    
    def gotologin(self):
        Register(self.root)
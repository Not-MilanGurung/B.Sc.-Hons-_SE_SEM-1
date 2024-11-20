import tkinter as tk
from login import Login

class Register:
    
    def __init__(self, root):
        self.root = root

        text = tk.Label( text="Register", font="TimesNewRoman 28")
        text.grid(row=0, column=2,pady=10)


        fL = tk.Label(text="First Name", font='TimesNewRoman')
        fL.grid(row=1, column=1,pady=10, padx=10)
        mL = tk.Label(text="Middle Name", font='TimesNewRoman')
        mL.grid(row=1, column=2,padx=10, pady=10)
        lL = tk.Label(text="Last Name", font='TimesNewRoman')
        lL.grid(row=1, column=3,padx=10,pady=10)
        self.fname = tk.Entry()
        self.mname = tk.Entry()
        self.lname = tk.Entry()
        self.fname.grid(row=2, column=1,padx=10)
        self.mname.grid(row=2, column=2,padx=10)
        self.lname.grid(row=2, column=3,padx=10)

        phoneL = tk.Label( text="Phone Number", font='TimesNewRoman')
        phoneL.grid(row=3, column=1,pady=10)
        emailL = tk.Label( text="Email", font='TimesNewRoman')
        emailL.grid(row=3, column=3,pady=10)
        self.phone = tk.Entry()
        self.email = tk.Entry()
        self.phone.grid(row=4, column=1,padx=10)
        self.email.grid(row=4, column=3,padx=10)

        addL = tk.Label( text="Address", font='TimesNewRoman')
        addL.grid(row=5, column=1,pady=10)
        self.address = tk.Entry()
        self.address.grid(row=6, column=1,padx=10)
        # tk.Label(self, text='Gender', font='TimesNewRoman').grid(row=9, column=1,pady=10)
        # radioMale = tk.Radiobutton(self, text='Male', value='male')
        # radioMale.grid(row=9, column=2)
        # radioFemale = tk.Radiobutton(self, text='Female', value='female')
        # radioFemale.grid(row=9, column=3)


        button1 = tk.Button( text ="Login Page", command=self.showlogin)
        button1.grid(row = 7, column = 1, padx = 10, pady = 10)
    
    def showlogin(self):
        clearscreen(self)
        Login(self.root)

def clearscreen(self):
    for widget in self.root.winfo_children():
        widget.destroy()


import tkinter as tk
from tkinter import ttk


class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp 
    def __init__(self, *args, **kwargs): 
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = tk.Frame(self)  
        container.pack(side = "top", fill = "both", expand = True) 
        
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {}  
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Login, Register):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with 
            # for loop
            self.frames[F] = frame 
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
         
        # label of frame Layout 2
        label = ttk.Label(self, text ="Startpage")
         
        # putting the grid in its place by using
        # grid
        label.grid(row = 0, column = 0, padx = 100, pady = 10) 

        button1 = ttk.Button(self, text ="Login",
        command = lambda : controller.show_frame(Login))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 0, padx = 350, pady = 10)
  
        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text ="Register",
        command = lambda : controller.show_frame(Register))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 0, padx = 100, pady = 10)
  
class Login(tk.Frame):
     
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        from middleware import insert 

        def save():
            username = user.get()
            age = age_entry.get()
            grade = grade_entry.get()
            insert(username, age, grade)
            ttk.Message(text='Saved sucessfully')

        userL = ttk.Label(self, text='Username')
        userL.grid(row=0, column=0, padx=10, pady=10)
        user = ttk.Entry(self)
        user.grid(row=0, column=1, padx=10, pady=10)

        ageL = ttk.Label(self, text='Age')
        ageL.grid(row=1, column=0, padx=10, pady=10)
        age_entry = ttk.Entry(self)
        age_entry.grid(row=1, column=1, padx=10, pady=10)

        gradeL = ttk.Label(self, text='Grade')
        gradeL.grid(row=2, column=0, padx=10, pady=10)
        grade_entry = ttk.Entry(self)
        grade_entry.grid(row=2, column=1, padx=10, pady=10)

        button1 = ttk.Button(self, text='Save', command=save)
        button1.grid(row=3, column=0, padx=10,pady=20)

        button1 = ttk.Button(self, text ="StartPage", command = lambda : controller.show_frame(StartPage))
        button1.grid(row = 5, column = 1, padx = 10, pady = 10)  

class Register(tk.Frame):
     
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        text = ttk.Label(self, text="Register", font="TimesNewRoman 28")
        text.grid(row=0, column=2,pady=10)

        fL = ttk.Label(self, text="First Name", font='TimesNewRoman')
        fL.grid(row=1, column=1,pady=10, padx=10)
        mL = ttk.Label(self, text="Middle Name", font='TimesNewRoman')
        mL.grid(row=1, column=2,padx=10, pady=10)
        lL = ttk.Label(self, text="Last Name", font='TimesNewRoman')
        lL.grid(row=1, column=3,padx=10,pady=10)
        fname = ttk.Entry(self)
        mname = ttk.Entry(self)
        lname = ttk.Entry(self)
        fname.grid(row=2, column=1,padx=10)
        mname.grid(row=2, column=2,padx=10)
        lname.grid(row=2, column=3,padx=10)

        phoneL = ttk.Label(self, text="Phone Number", font='TimesNewRoman')
        phoneL.grid(row=3, column=1,pady=10)
        emailL = ttk.Label(self, text="Email", font='TimesNewRoman')
        emailL.grid(row=3, column=3,pady=10)
        phone = ttk.Entry(self)
        email = ttk.Entry(self)
        phone.grid(row=4, column=1,padx=10)
        email.grid(row=4, column=3,padx=10)

        addL = ttk.Label(self, text="Address", font='TimesNewRoman')
        addL.grid(row=5, column=1,pady=10)
        address = ttk.Entry(self)
        address.grid(row=6, column=1,padx=10)
        ttk.Label(self, text='Gender', font='TimesNewRoman').grid(row=9, column=1,pady=10)
        radioMale = ttk.Radiobutton(self, text='Male', value='male')
        radioMale.grid(row=9, column=2)
        radioFemale = ttk.Radiobutton(self, text='Female', value='female')
        radioFemale.grid(row=9, column=3)

        userL = ttk.Label(self, text="User Name", font='TimesNewRoman')
        userL.grid(row=7, column=1,pady=10)
        passL= ttk.Label(self, text="Password", font='TimesNewRoman')
        passL.grid(row=7, column=3,pady=10)
        userName = ttk.Entry(self)
        password = ttk.Entry(self, show='*')
        userName.grid(row=8, column=1,padx=10)
        password.grid(row=8, column=3,padx=10)

        store = ttk.Button(self, text='Store')
        store.grid(row=10, column= 2)
        button1 = ttk.Button(self, text ="StartPage", command = lambda : controller.show_frame(StartPage))
        button1.grid(row = 10, column = 1, padx = 10, pady = 10)  


app = tkinterApp()
app.geometry('800x500')
app.mainloop()

import tkinter as meow

root = meow.Tk()
root.title('Registeration')
root.geometry('700x700')

meow.Label(text="Register", font="TimesNewRoman 28").grid(row=0, column=2,pady=10)

meow.Label(text="First Name", font='TimesNewRoman').grid(row=1, column=1,pady=10, padx=100)
meow.Label(text="Middle Name", font='TimesNewRoman').grid(row=1, column=2,padx=10, pady=10)
meow.Label(text="Last Name", font='TimesNewRoman').grid(row=1, column=3,padx=10,pady=10)
fname = meow.Entry()
mname = meow.Entry()
lname = meow.Entry()
fname.grid(row=2, column=1,padx=10)
mname.grid(row=2, column=2,padx=10)
lname.grid(row=2, column=3,padx=10)

meow.Label(text="Phone Number", font='TimesNewRoman').grid(row=3, column=1,pady=10)
meow.Label(text="Email", font='TimesNewRoman').grid(row=3, column=3,pady=10)
phone = meow.Entry()
email = meow.Entry()
phone.grid(row=4, column=1,padx=10)
email.grid(row=4, column=3,padx=10)

meow.Label(text="Address", font='TimesNewRoman').grid(row=5, column=1,pady=10)
address = meow.Entry()
address.grid(row=6, column=1,padx=10)

meow.Label(text="User Name", font='TimesNewRoman').grid(row=7, column=1,pady=10)
meow.Label(text="Password", font='TimesNewRoman').grid(row=7, column=3,pady=10)
userName = meow.Entry()
password = meow.Entry(show='M')
userName.grid(row=8, column=1,padx=10)
password.grid(row=8, column=3,padx=10)

meow.Button(text='Store').grid(row=9, column= 2)

root.mainloop()

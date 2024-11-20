import tkinter as jeff
from middleware import insert 

def save():
    username = user.get()
    age = age_entry.get()
    grade = grade_entry.get()
    insert(username, age, grade)
    jeff.Message(text='Saved sucessfully')


root = jeff.Tk()
root.title('Passing Values')
root.geometry('500x500')

jeff.Label(text='Username').grid(row=0, column=0, padx=10, pady=10)
user = jeff.Entry()
user.grid(row=0, column=1, padx=10, pady=10)

jeff.Label(text='Age').grid(row=1, column=0, padx=10, pady=10)
age_entry = jeff.Entry()
age_entry.grid(row=1, column=1, padx=10, pady=10)

jeff.Label(text='Grade').grid(row=2, column=0, padx=10, pady=10)
grade_entry = jeff.Entry()
grade_entry.grid(row=2, column=1, padx=10, pady=10)

button1 = jeff.Button(text='Save', command=save)
button1.grid(row=3, column=0, padx=10,pady=20)

root.mainloop()
import tkinter as tk

tk.Label(text="Login Page").grid(row=1, column=1)
tk.Label(text="Email").grid(row=2, column=2)
tk.Entry(width=50).grid(row=3, column=2)
tk.Label(text="Text 3 *").grid(row=3, column=2)
tk.Entry(width=50).grid(row=5, column=2)
tk.Button(text="Submit").grid()

tk.mainloop()
from tkinter import *

# ---------- PASSWORD GENERATOR ---------- #

# ---------- SAVE PASSWORD ---------- #

# ---------- UI SETUP ---------- #

window = Tk()
window.title('Password Manager')

window.config(background="white")
r = Label(bg="red", width=20, height=5)
r.grid(row=0, column=0)

g = Label(bg="green", width=20, height=5)
g.grid(row=1, column=1)

b = Label(bg="blue", width=20,height=5)
b.grid(row=2, column=0)

window.config(padx=20, pady=20)


#Labels
website_label = Label(text="Website")

window.mainloop()
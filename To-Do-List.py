from tkinter import *
app = Tk()
app.title("To do list")
app.geometry("720x480")
app.resizable(False,False)
app.config(bg="#242424")


title = Label(app,text="To-Do List",font=("consolas",18),bg="#242424",fg="#fff")
title.pack()

text = StringVar()
task_entry = Entry(app, width=34,textvariable=text,font=("consolas",12))

# Buttons
add = Button(app, text="Add", width=5,font=("consolas",12))
add.place(x = 202,y = 110)

remove = Button(app, text="Remove", width=6,font=("consolas",12))
remove.place(x = 450,y = 110)

mark = Button(app, text="Add", width=12,font=("consolas",12))
mark.place(x = 300,y = 130)

save = Button(app, text="Add", width=5,font=("consolas",12))
save.place(x = 205,y = 150)

load = Button(app, text="Add", width=6,font=("consolas",12))
load.place(x = 450,y = 150)

# List box
list_box = Listbox(app, height=15,width=45, font=("consolas",12))
list_box.place(x = 170, y = 200)

app.mainloop()

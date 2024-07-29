from tkinter import *
from PIL import ImageTk,Image
from Register import reg
import sqlite3
from HomePage import *

def login():
    global playerid, name
    conn = sqlite3.connect('demo.db')
    c = conn.cursor()
    for row in c.execute("Select * from user"):
        playerid = row[0]
        name = row[1]
        uname = row[3]
        password = row[4]
        if(username.get()==uname and pwd.get()==password):
            lbl = Label(frame, text="Valid user", fg="#8B008B", bg="black", padx=10, pady=10, font=('Arial Black', 26))
            demo(name, playerid)
            break
        else:
            lbl = Label(frame, text="Invalid user", fg="#8B008B", bg="black", padx=10, pady=10, font=('Arial Black', 24))
    lbl.grid_forget()
    lbl.place(x=200,y=600)

    username.delete(0,END)
    pwd.delete(0,END)
    conn.commit()
    conn.close()

#setting environment
log = Tk()
log.title("User Login")
log.geometry("700x750")

# Defining image
img = ImageTk.PhotoImage(Image.open(".\\resources\\login2.jpg"))

# defining frame
frame = LabelFrame(log)

# defining labels
background = Label(frame, image=img)
lbl1 = Label(frame, text="Login to play Games!!!", fg="#8B008B", bg="black", padx=30, pady=20, font=('Algerian', 34))
lbl2 = Label(frame, text="Username:", fg="#8B008B", bg="black", padx=10, pady=10, font=('Arial Black', 24))
lbl3 = Label(frame, text="Password:", fg="#8B008B", bg="black", padx=10, pady=10, font=('Arial Black', 24))

# defining entry fields
username = Entry(frame,width=16,font=('Adobe Fangsong Std R', 18),border=5,bg='black',fg="white")

pwd = Entry(frame,show="*",width=16,font=('Adobe Fangsong Std R', 18),border=5,bg='black',fg="white")

#defining buttons
login = Button(frame, text="LOGIN",fg='#8B008B',bg="black",font=('Arial Black', 18),border=5,command=login)
reg = Button(frame, text="REGISTOR NOW!",fg='#8B008B',bg="black",font=('Arial Black', 18),border=5, command=reg)

# Putting widgets on the screen
frame.pack()
background.grid(row=0, column=0, rowspan=3, columnspan=2)

lbl1.grid(row=0, column=0, columnspan=2)

lbl2.place(x=140,y=280)
lbl3.place(x=140,y=385)

username.place(x=350,y=300)
pwd.place(x=350,y=400)

login.place(x=140,y=500)
reg.place(x=350,y=500)

log.mainloop()

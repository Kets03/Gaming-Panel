from tkinter import *
from AllFunctions import *
from PIL import ImageTk, Image

def reg():
    def insert():
        if(fname.get()!="" and lname.get()!="" and uname.get()!="" and pwd.get()!=""):
            regUser(fname.get(), lname.get(), uname.get(), pwd.get())
            fname.delete(0, END)
            lname.delete(0, END)
            uname.delete(0, END)
            pwd.delete(0, END)
            register.grid_forget()
            lbl = Label(frame, text="User registered successfully!!!", fg="#8B008B", bg="black", padx=30, pady=20, font=('Algerian', 28))
            lbl.grid(row=5,column=0,columnspan=2)
        else:
            lbl = Label(frame, text="Please enter valid details", fg="#8B008B", bg="black", padx=30, pady=20, font=('Algerian', 28))
            lbl1.grid_forget()
            lbl.grid(row=0, column=0, columnspan=2)

    reg = Toplevel()
    reg.title("Register Now")
    reg.geometry("700x750")
    global img
    # Defining image
    img = ImageTk.PhotoImage(Image.open(".\\resources\\login2.jpg"))

    # defining frame
    frame = LabelFrame(reg)
    background = Label(frame, image=img)
    lbl1 = Label(frame, text="Enter your credentials", fg="#8B008B", bg="black", padx=30, pady=20, font=('Algerian', 30))
    lbl2 = Label(frame, text="First Name:", fg="#8B008B", bg="black", padx=10, pady=10, font=('Arial Black', 24))
    lbl3 = Label(frame, text="Last Name:", fg="#8B008B", bg="black", padx=10, pady=10, font=('Arial Black', 24))
    lbl4 = Label(frame, text="Username:", fg="#8B008B", bg="black", padx=10, pady=10, font=('Arial Black', 24))
    lbl5 = Label(frame, text="Set Password:", fg="#8B008B", bg="black", padx=10, pady=10, font=('Arial Black', 24))

    fname = Entry(frame,width=16,font=('Adobe Fangsong Std R', 18),border=5,bg='black',fg="white")
    lname = Entry(frame,width=16,font=('Adobe Fangsong Std R', 18),border=5,bg='black',fg="white")
    uname = Entry(frame,width=16,font=('Adobe Fangsong Std R', 18),border=5,bg='black',fg="white")
    pwd = Entry(frame,width=16,font=('Adobe Fangsong Std R', 18),border=5,bg='black',fg="white")

    register = Button(frame, text="REGISTER", fg='#8B008B', bg="black", font=('Arial Black', 18), border=5,command= insert)
    # Putting widgets on the screen
    frame.pack()
    background.grid(row=0, column=0, rowspan=6, columnspan=2)

    lbl1.grid(row=0, column=0, columnspan=2)
    lbl2.grid(row=1,column=0)
    lbl3.grid(row=2, column=0)
    lbl4.grid(row=3, column=0)
    lbl5.grid(row=4, column=0)

    fname.grid(row=1,column=1)
    lname.grid(row=2, column=1)
    uname.grid(row=3, column=1)
    pwd.grid(row=4, column=1)

    register.grid(row=5,column=0,columnspan=2)
    reg.mainloop()
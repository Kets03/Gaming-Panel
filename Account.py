from tkinter import *
from PIL import ImageTk, Image
from AllFunctions import *

def account(playid):
    global playerid, img, background, asteroid, snake, dodgeblock
    playerid = playid
    acc = Toplevel()
    acc.title("Account")
    acc.geometry("700x600")

    # Defining images
    img = ImageTk.PhotoImage(Image.open(".\\resources\\Acc.jpg"))

    # defining frame
    frame = LabelFrame(acc)

    for row in fetchscores(playerid):
        snake = row[0]
        asteroid = row[1]
        dodgeblock = row[2]

    # defining labels
    background = Label(frame, image=img)
    lbl1 = Label(frame,text="Account Details", fg="#8B008B", bg="black", padx=30, pady=20, font=('Algerian', 40))
    lbl2 = Label(frame, text="High Scores:", fg="#8B008B", bg="black", padx=10, pady=10, font=('Arial Black', 32))
    lbl3 = Label(frame, text="Snake Game: "+str(snake), fg="#8B008B", bg="black", padx=10, pady=10, font=('Arial Black', 24))
    lbl4 = Label(frame, text="Asteroid Game: "+str(asteroid), fg="#8B008B", bg="black", padx=10, pady=10, font=('Arial Black', 24))
    lbl5 = Label(frame, text="Block-Dodge Game: "+str(dodgeblock), fg="#8B008B", bg="black", padx=10, pady=10, font=('Arial Black', 24))

    #defining buttons
    Exit = Button(frame, text="Exit", fg='#8B008B', bg="black", font=('Arial Black', 24), border=5, command=quit)

    # Putting widgets on the screen
    frame.pack()
    background.pack()
    lbl1.place(x=120,y=70)
    lbl2.place(x=100,y=180)
    lbl3.place(x=80,y=270)
    lbl4.place(x=80,y=330)
    lbl5.place(x=80,y=380)

    Exit.place(x=300,y=480)

    acc.mainloop()
#account((1132200002))
from tkinter import *
from PIL import ImageTk, Image
from snake import *
from connect4 import *
from DodgeBlock import *
from Asteroids import *
from t import *
from Account import *
#from TTT import *

def homepage(name,playid):
    global firstname, playerid,img, background
    firstname=name
    playerid=playid
    hp = Toplevel()
    hp.title("Home page")
    hp.geometry("700x750")

    # Defining images
    img = ImageTk.PhotoImage(Image.open(".\\resources\\login2.jpg"))
    snakeImg = ImageTk.PhotoImage(Image.open(".\\resources\\snake.jpeg"))
    connect4Img = ImageTk.PhotoImage(Image.open(".\\resources\\Connect4.jpeg"))
    dodgeblockImg = ImageTk.PhotoImage(Image.open(".\\resources\\block dodge.jpeg"))
    tttImg = ImageTk.PhotoImage(Image.open(".\\resources\\ttt.jpeg"))
    asteroidImg = ImageTk.PhotoImage(Image.open(".\\resources\\asteroidimg.jpeg"))

    # defining frame
    frame = LabelFrame(hp)

    # defining labels
    background = Label(frame, image=img)

    snakegame = Label(frame, image= snakeImg)
    connect4game = Label(frame, image=connect4Img)
    dodgeblockgame = Label(frame, image=dodgeblockImg)
    tttgame = Label(frame, image=tttImg)
    asteroidgame = Label(frame, image=asteroidImg)

    lbl1 = Label(frame,text="Welcome "+firstname+" !", fg="#8B008B", bg="black", padx=30, pady=20, font=('Algerian', 30))

    #defining buttons
    acc = Button(frame, text="Account",fg='#8B008B',bg="black",font=('Arial Black', 18),border=5,command=lambda: account(playerid))

    #Game Buttons
    snakeButton = Button(frame, text="Play",fg='green',bg="black",font=('Arial Black', 15),border=5,command=lambda: snake(playerid))
    connect4Button = Button(frame, text="Play", fg='blue', bg="grey", font=('Arial Black', 15), border=5,command=connect4)
    dodgeblockButton = Button(frame, text="Play", fg='white', bg="blue", font=('Arial Black', 15), border=5,command=lambda: dodge(playerid))
    tttButton = Button(frame, text="Play", fg='green', bg="white", font=('Arial Black', 15), border=5,command=t)
    AsteroidButton = Button(frame, text="Play", fg='blue', bg="black", font=('Arial Black', 15), border=5,command=lambda: asteroid(playerid))

    # Putting widgets on the screen
    frame.pack()
    background.grid(row=0, column=0, rowspan=5, columnspan=5)
    lbl1.grid(row=0,column=0,columnspan=5)

    snakegame.place(x=70,y=160)
    snakeButton.place(x=100,y=275)

    dodgeblockgame.place(x=440, y=160)
    dodgeblockButton.place(x=500, y=275)

    asteroidgame.place(x=250,y=160)
    AsteroidButton.place(x=300,y=275)

    tttgame.place(x=150,y=380)
    tttButton.place(x=200,y=505)

    connect4game.place(x=350, y=380)
    connect4Button.place(x=410, y=500)

    acc.grid(row=4,column=0,columnspan=5)

    hp.mainloop()

def demo(name,playid):
    firstname = name
    playerid = playid
    homepage(firstname,playerid)
#demo("Ketaki",1132200001)
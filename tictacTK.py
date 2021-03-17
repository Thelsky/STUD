# Abdulrahman Alsaykhan
# 371109436
from tkinter import *
from tkinter import messagebox
from tkinter import font as tkFont

# making the board we gona play on
board = ['1 ', '2 ', '3 ', '4', '5', '6', '7', '8', '9']

game = Tk()
game.title('TicTac')
player1 = 'X'
player2 = 'O'
counter = 0
f1 = tkFont.Font(family='Helvetica', size=25, weight='bold')

# here we deside who will play and start drow X and O on the buttons


def draw(slot):
    global counter
    if counter % 2 == 0:
        board[slot] = player1
    elif counter % 2 != 0:
        board[slot] = player2
    changeButt(slot)
    header.grid(row=0, column=0, columnspan=3)
    # print(board)
    counter += 1
    if counter > 4:
        checkWin()

# here where the buttons change when we click on them


def changeButt(slot):
    if slot == 0:
        if counter % 2 == 0:
            a1.config(text=player1)
        elif counter % 2 != 0:
            a1.config(text=player2)
        a1.config(state=DISABLED)

    elif slot == 1:
        if counter % 2 == 0:
            a2.config(text=player1)
        elif counter % 2 != 0:
            a2.config(text=player2)
        a2.config(state=DISABLED)

    elif slot == 2:
        if counter % 2 == 0:
            a3.config(text=player1)
        elif counter % 2 != 0:
            a3.config(text=player2)
        a3.config(state=DISABLED)

    elif slot == 3:
        if counter % 2 == 0:
            a4.config(text=player1)
        elif counter % 2 != 0:
            a4.config(text=player2)
        a4.config(state=DISABLED)

    elif slot == 4:
        if counter % 2 == 0:
            a5.config(text=player1)
        elif counter % 2 != 0:
            a5.config(text=player2)
        a5.config(state=DISABLED)

    elif slot == 5:
        if counter % 2 == 0:
            a6.config(text=player1)
        elif counter % 2 != 0:
            a6.config(text=player2)
        a6.config(state=DISABLED)

    elif slot == 6:
        if counter % 2 == 0:
            a7.config(text=player1)
        elif counter % 2 != 0:
            a7.config(text=player2)
        a7.config(state=DISABLED)

    elif slot == 7:
        if counter % 2 == 0:
            a8.config(text=player1)
        elif counter % 2 != 0:
            a8.config(text=player2)
        a8.config(state=DISABLED)

    elif slot == 8:
        if counter % 2 == 0:
            a9.config(text=player1)
        elif counter % 2 != 0:
            a9.config(text=player2)
        a9.config(state=DISABLED)

# here will check if anyone win or tie after 9 turn


def checkWin():

    msg1 = "Congrats Player " + board[0] + " Won The Game !!! "
    msg2 = "Congrats Player " + board[4] + " Won The Game !!! "
    msg3 = "Congrats Player " + board[8] + " Won The Game !!! "
    msg4 = "Congrats Player " + board[2] + " Won The Game !!! "
    msg5 = "wow It seems we have a DRAW ! "
    if board[1] == board[2] == board[0] or board[0] == board[4] == board[8] or board[0] == board[3] == board[6]:
        messagebox.showinfo(
            title="We  have winner!", message=msg1)
    elif board[1] == board[4] == board[7] or board[3] == board[4] == board[5]:
        messagebox.showinfo(
            title="We  have winner!", message=msg2)
    elif board[2] == board[5] == board[8] or board[6] == board[7] == board[8]:
        messagebox.showinfo(
            title="We  have winner!", message=msg3)
    elif board[2] == board[4] == board[6]:
        messagebox.showinfo(
            title="We  have winner!", message=msg4)
    elif counter >= 9:
        messagebox.showinfo(
            title="Equally smart or Equally Stupid :P ", message=msg5)

# here we make the button and how it look


header = Label(game, text='Have Fun!', font=f1)
header.grid(row=0, column=0, columnspan=3)
a1 = Button(game, text=' ', borderwidth=20, padx=55,
            pady=50, command=lambda: draw(0), font=f1)
a1.grid(row=1, column=0)
a2 = Button(game, text=' ', borderwidth=20, padx=55,
            pady=50, command=lambda: draw(1), font=f1)
a2.grid(row=1, column=1)
a3 = Button(game, text=' ', borderwidth=20,  padx=55,
            pady=50, command=lambda: draw(2), font=f1)
a3.grid(row=1, column=2)
a4 = Button(game, text=' ', borderwidth=20, padx=55,
            pady=50, command=lambda: draw(3), font=f1)
a4.grid(row=2, column=0)
a5 = Button(game, text=' ', borderwidth=20, padx=55,
            pady=50, command=lambda: draw(4), font=f1)
a5.grid(row=2, column=1)
a6 = Button(game, text=' ', borderwidth=20, padx=55,
            pady=50, command=lambda: draw(5), font=f1)
a6.grid(row=2, column=2)
a7 = Button(game, text=' ', borderwidth=20, padx=55,
            pady=50, command=lambda: draw(6), font=f1)
a7.grid(row=3, column=0)
a8 = Button(game, text=' ', borderwidth=20,  padx=55,
            pady=50, command=lambda: draw(7), font=f1)
a8.grid(row=3, column=1)
a9 = Button(game, text=' ', borderwidth=20, padx=55,
            pady=50, command=lambda: draw(8), font=f1)
a9.grid(row=3, column=2)


game.mainloop()

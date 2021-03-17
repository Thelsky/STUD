from tkinter import *
from tkinter import messagebox

bord = ['1 ', '2 ', '3 ', '4', '5', '6', '7', '8', '9']

root = Tk()
area = {}
player1 = 'X'
player2 = 'O'
counter = 0

# def ifitsempyt(x):
# return bord[x] = ' '


def draw(slot):
    if counter % 2 == 0:
        bord[slot] = player2
    elif counter % 2 != 0:
        bord[slot] = player1
    if slot == 1:
        if counter % 2 == 0:
            a1.config(text=player2)
        elif counter % 2 != 0:
            a1.config(text=player1)
        a1.config(state=DISABLED)
    elif slot == 2:
        if counter % 2 == 0:
            a2.config(text=player2)
        elif counter % 2 != 0:
            a2.config(text=player1)
        a2.config(state=DISABLED)
    elif slot == 3:
        if counter % 2 == 0:
            a3.config(text=player2)
        elif counter % 2 != 0:
            a3.config(text=player1)
        a3.config(state=DISABLED)
    elif slot == 4:
        if counter % 2 == 0:
            a4.config(text=player2)
        elif counter % 2 != 0:
            a4.config(text=player1)
        a4.config(state=DISABLED)
    elif slot == 5:
        if counter % 2 == 0:
            a5.config(text=player2)
        elif counter % 2 != 0:
            a5.config(text=player1)
        a5.config(state=DISABLED)
    elif slot == 6:
        if counter % 2 == 0:
            a6.config(text=player2)
        elif counter % 2 != 0:
            a6.config(text=player1)
        a6.config(state=DISABLED)
    elif slot == 7:
        if counter % 2 == 0:
            a7.config(text=player2)
        elif counter % 2 != 0:
            a7.config(text=player1)
        a7.config(state=DISABLED)
    elif slot == 8:
        if counter % 2 == 0:
            a8.config(text=player2)
        elif counter % 2 != 0:
            a8.config(text=player1)
        a8.config(state=DISABLED)
    elif slot == 9:
        if counter % 2 == 0:
            a9.config(text=player2)
        elif counter % 2 != 0:
            a9.config(text=player1)
        a9.config(state=DISABLED)


def winning(areaz):
    win1 = 'Gongerats' + areaz[1] + 'win the game'
    win2 = 'Gongerats' + areaz[4] + 'win the game'
    win3 = 'Gongerats' + areaz[7] + 'win the game'
    win4 = 'Gongerats' + areaz[1] + 'win the game'
    win5 = 'Gongerats' + areaz[3] + 'win the game'
    win6 = 'Gongerats' + areaz[7] + 'win the game'
    win7 = 'Gongerats' + areaz[8] + 'win the game'
    win8 = 'Gongerats' + areaz[9] + 'win the game'
    if counter > 5:
        if areaz[1] == areaz[2] == areaz[3]:
            messagebox.showinfo(title='You win', message=win1)
        elif areaz[4] == areaz[5] == areaz[6]:
            messagebox.showinfo(title='You win', message=win2)
        elif areaz[7] == areaz[8] == areaz[9]:
            messagebox.showinfo(title='You win', message=win3)
        elif areaz[1] == areaz[5] == areaz[9]:
            messagebox.showinfo(title='You win', message=win4)
        elif areaz[3] == areaz[5] == areaz[7]:
            messagebox.showinfo(title='You win', message=win5)
        elif areaz[7] == areaz[4] == areaz[1]:
            messagebox.showinfo(title='You win', message=win6)
        elif areaz[8] == areaz[5] == areaz[2]:
            messagebox.showinfo(title='You win', message=win7)
        elif areaz[9] == areaz[6] == areaz[3]:
            messagebox.showinfo(title='You win', message=win8)
    if counter == 9:
        messagebox('Game Over it\'s tie')


header = Label(root, text='Hello')
header.grid(row=0, column=0, columnspan=3)
a1 = Button(root, text=' ', borderwidth=45, padx=2,
            pady=2, command=lambda: draw(1))
a1.grid(row=2, column=0)
a2 = Button(root, text=' ', borderwidth=45, padx=2,
            pady=2, command=lambda: draw(2))
a2.grid(row=0, column=0)
a3 = Button(root, text=' ', borderwidth=45, padx=2,
            pady=2, command=lambda: draw(3))
a3.grid(row=0, column=0)
a4 = Button(root, text=' ', borderwidth=45, padx=2,
            pady=2, command=lambda: draw(4))
a4.grid(row=0, column=0)
a5 = Button(root, text=' ', borderwidth=45, padx=2,
            pady=2, command=lambda: draw(5))
a5.grid(row=0, column=0)
a6 = Button(root, text=' ', borderwidth=45, padx=2,
            pady=2, command=lambda: draw(6))
a6.grid(row=0, column=0)
a7 = Button(root, text=' ', borderwidth=45, padx=2,
            pady=2, command=lambda: draw(7))
a7.grid(row=0, column=0)
a8 = Button(root, text=' ', borderwidth=45, padx=2,
            pady=2, command=lambda: draw(8))
a8.grid(row=0, column=0)
a9 = Button(root, text=' ', borderwidth=45, padx=2,
            pady=2, command=lambda: draw(9))
a9.grid(row=0, column=0)


root.mainloop()

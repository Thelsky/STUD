# abdulrahman alsaykhan
# 371109436


from tkinter import *
import tkinter as tk
import sqlite3
import difflib
import webbrowser
import folium


class db():
    def __init__(self):
        self.link = sqlite3.connect('Mosques_DataBase.db')
        self.c = self.link.cursor()
        try:
            self.c.execute(""" CREATE TABLE records (
                identry integer UNIQUE,
                nameentry text,
                typeEntry text,
                adsentry text,
                clat int,
                clon int,
                imentry text
            )""")
            self.link.commit()
        except sqlite3.OperationalError:
            None

    def displayAll(self):
        link = sqlite3.connect('Mosques_DataBase.db')
        c = link.cursor()
        c.execute("SELECT * FROM records")
        r = c.fetchall()
        listbox.delete(0, 'end')
        for i in r:
            listbox.insert(END, i)
        print(r)
        link.commit()
        link.close()

    def insert(self, identry, nameentry, t, adsentry, clat, clon, imentry):
        # Creating DataBase
        link = sqlite3.connect('Mosques_DataBase.db')
        c = link.cursor()
        c.execute("INSERT INTO records VALUES(:identry, :nameentry, :typeEntry, :adsentry, :clat, :clon, :imentry)",
                  {
                      'identry': identry.get(),
                      'nameentry': nameentry.get(),
                      'typeEntry': t.get(),
                      'adsentry': adsentry.get(),
                      'clat': clat.get(),
                      'clon': clon.get(),
                      'imentry': imentry.get()
                  })
        link.commit()
        # clear fields
        identry.delete(0, END)
        nameentry.delete(0, END)
        t.set('        Select        ')
        adsentry.delete(0, END)
        clat.delete(0, END)
        clon.delete(0, END)
        imentry.delete(0, END)

    def delete(self, identry):
        link = sqlite3.connect('Mosques_DataBase.db')
        c = link.cursor()
        c.execute("DELETE from records WHERE identry = " + identry.get())
        link.commit()
        link.close()

    def search(self, nameentry):
        link = sqlite3.connect('Mosques_DataBase.db')
        c = link.cursor()
        x = nameentry.get()
        c.execute("SELECT nameentry FROM records ")
        r = c.fetchall()
        # Find close matchs
        l1 = [item for t in r for item in t]
        m = difflib.get_close_matches(x, l1, 10, 0.5)
        listbox.delete(0, 'end')
        # remove repeated elements
        i1 = 0
        for i in m:
            try:
                if i == m[i1+1]:
                    m.remove(i)
            except IndexError:
                pass
        # get records
        for i in m:
            c.execute("SELECT * FROM records WHERE nameentry =?", (i,))
            n = c.fetchall()
            for j in n:
                listbox.insert(END, j)
        link.commit()
        link.close()

    def onmap(self):
        global listbox, viewBox, scrollbar
        slct = LabelFrame(root, text='Select', padx=100, pady=10)
        slct.grid(row=6, column=0, padx=5, pady=5)
        h1 = Label(slct, text='Please enter the ID of the Mosque you want ')
        h1.grid(row=0, column=0, columnspan=3)
        idl = Label(slct, text='ID ')
        idl.grid(row=1, column=0)
        slctentry = Lotfi(slct)
        slctentry.grid(row=1, column=1)
        get = Button(slct, text='Get Record', command=lambda: onmapg(
            slctentry.get()), padx=5, pady=0)
        get.grid(row=1, column=2)
        # Frame for view box
        viewBox = LabelFrame(root, text=' View Box', padx=5, pady=8)
        # Scroll bar
        scrollbar = Scrollbar(viewBox)
        scrollbar.pack(side=RIGHT, fill=Y)
        # List box
        listbox = Listbox(
            viewBox, bd=0, yscrollcommand=scrollbar.set, width=80, height=19)
        listbox.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=listbox.yview)
        viewBox.grid(row=1, column=5, rowspan=10,
                     padx=2, pady=2, ipadx=1, ipady=1)

    def update(self):
        global listbox, viewBox, scrollbar, slct, slctentry
        slct = LabelFrame(root, text='Select', padx=100, pady=10)
        slct.grid(row=6, column=0, padx=5, pady=5)
        h1 = Label(slct, text='Please enter the ID of the Mosque you want ')
        h1.grid(row=0, column=0, columnspan=5)
        idl = Label(slct, text='ID ')
        idl.grid(row=1, column=0)
        slctentry = Lotfi(slct)
        slctentry.grid(row=1, column=1)
        get = Button(slct, text='Get Record', command=lambda: updates(
            slctentry.get()), padx=5, pady=0)
        get.grid(row=1, column=2)
        # Frame for view box
        viewBox = LabelFrame(root, text=' View Box', padx=5, pady=8)
        # Scroll bar
        scrollbar = Scrollbar(viewBox)
        scrollbar.pack(side=RIGHT, fill=Y)
        # List box
        listbox = Listbox(
            viewBox, bd=0, yscrollcommand=scrollbar.set, width=80, height=19)
        listbox.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=listbox.yview)
        viewBox.grid(row=1, column=5, rowspan=10,
                     padx=2, pady=2, ipadx=1, ipady=1)

    def __del__(self):
        self.link.close()


def updates(D):
    global listbox, viewBox, scrollbar, slct, slctentry
    link = sqlite3.connect('Mosques_DataBase.db')
    c = link.cursor()
    c.execute("SELECT * FROM records WHERE identry =?", (D,))
    r = c.fetchall()
    print(r)
    for i in r:
        identry.insert(0, i[0])
        nameentry.insert(0, i[1])
        t.set(i[2])
        adsentry.insert(0, i[3])
        clat.insert(0, i[4])
        clon.insert(0, i[5])
        imentry.insert(0, i[6])
    supmit = Button(slct, text='Submit update', command=supmitupdate, width=31)
    supmit.grid(row=2, column=0, columnspan=3)
    # Frame for view box
    viewBox = LabelFrame(root, text=' View Box', padx=5, pady=8)
    # Scroll bar
    scrollbar = Scrollbar(viewBox)
    scrollbar.pack(side=RIGHT, fill=Y)
    # List box
    listbox = Listbox(
        viewBox, bd=0, yscrollcommand=scrollbar.set, width=80, height=20)
    listbox.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=listbox.yview)
    viewBox.grid(row=1, column=5, rowspan=10, padx=2, pady=2, ipadx=1, ipady=1)
    link = sqlite3.connect('Mosques_DataBase.db')
    c = link.cursor()
    c.execute("SELECT * from records WHERE identry = " + identry.get())
    r = c.fetchall()
    for i in r:
        listbox.insert(END, i)
    link.commit()
    link.close()


def supmitupdate():
    global slctentry
    link = sqlite3.connect('Mosques_DataBase.db')
    c = link.cursor()
    print(slctentry)
    c.execute("""UPDATE records SET
        'nameentry' = :nameentry,
        'typeEntry' = :t,
        'adsentry' = :adsentry,
        'clat' = :clat,
        'clon' = :clon,
        'imentry' = :imentry

        WHERE identry = :identry""",
              {
                  'nameentry': nameentry.get(),
                  't': t.get(),
                  'adsentry': adsentry.get(),
                  'clat': clat.get(),
                  'clon': clon.get(),
                  'imentry': imentry.get(),
                  'identry': slctentry.get()
              })
    link.commit()
    link.close()


def onmapg(D):
    link = sqlite3.connect('Mosques_DataBase.db')
    c = link.cursor()
    c.execute("SELECT clat FROM records WHERE identry =?", (D,))
    r1 = c.fetchall()
    l1 = [item for t in r1 for item in t]
    print(l1)
    c.execute("SELECT clon FROM records WHERE identry =?", (D,))
    r2 = c.fetchall()
    l2 = [item for t in r2 for item in t]
    print(l2)
    om = "map0.html"
    mp = folium.Map(location=[float(l1[0]), float(l2[0])], zoom_start=10)
    mp.save(om)
    webbrowser.open(om, new=2)


class Lotfi(tk.Entry):
    def __init__(self, master=None, max_len=5, **kwargs):
        self.var = tk.StringVar()
        self.max_len = max_len
        tk.Entry.__init__(self, master, textvariable=self.var, **kwargs)
        self.old_value = ''
        self.var.trace('w', self.check)

    def check(self, *args):
        if len(self.get()) <= self.max_len:
            self.old_value = self.get()  # accept change
        else:
            self.var.set(self.old_value)  # reject change


# Creating GUI with Tkinter
# GUI Start
root = Tk()
root.title("Mosques Management System")

# Header
header = Label(
    root, text='Welcome To The Mosques Management System', padx=5, pady=5)
header.grid(row=0, column=0, columnspan=10)


# Fourm Frame
Fourm = LabelFrame(root, text='Records Entries ', padx=10, pady=5)
Fourm.grid(row=1, column=0, columnspan=4, rowspan=3, padx=5, pady=5)
# Fourm
# ID
idlabel = Label(Fourm, text=' ID ', padx=5, pady=5)
idlabel.grid(row=1, column=0)
identry = Lotfi(Fourm)
identry.grid(row=1, column=1)
# Type
typelabel = Label(Fourm, text=' Type ', padx=5, pady=5)
typelabel.grid(row=2, column=0)
typeoptions = [' Category A ', ' Category B ', ' Category C ']
t = StringVar(root)
t.set('        Select        ')
typeEntry = OptionMenu(Fourm, t, *typeoptions)
typeEntry.grid(row=2, column=1)
# Coordeinates
clabel = Label(Fourm, text=' Coordinates ', padx=5, pady=5)
clabel.grid(row=3, column=0)
cfram = LabelFrame(Fourm)
cfram.grid(row=3, column=1)
clat = Entry(cfram, width=10)
clat.grid(row=0, column=0)
clon = Entry(cfram, width=10)
clon.grid(row=0, column=1)
# Name
namelabel = Label(Fourm, text=' Name ', padx=5, pady=5)
namelabel.grid(row=1, column=3)
nameentry = Entry(Fourm)
nameentry.grid(row=1, column=4)
# Address
adslabel = Label(Fourm, text=' Address ', padx=5, pady=5)
adslabel.grid(row=2, column=3)
adsentry = Entry(Fourm)
adsentry.grid(row=2, column=4)
# Imam Name
imlabel = Label(Fourm, text=' Imam Name ', padx=5, pady=5)
imlabel.grid(row=3, column=3)
imentry = Entry(Fourm)
imentry.grid(row=3, column=4)


# Actions Frame
Actions = LabelFrame(root, text='Actions', padx=20, pady=5)
Actions.grid(row=4, column=0, columnspan=4, rowspan=2, padx=5, pady=5)
# Buttons
# Display All
displayAll = Button(Actions, text='Display All',
                    command=lambda: db.displayAll(0), padx=5, pady=5, width=15)
displayAll.grid(row=4, column=1, padx=5, pady=5)
# Add Entry
addEntry = Button(Actions, text='Add Entry', command=lambda: v.insert(
    identry, nameentry, t, adsentry, clat, clon, imentry), padx=5, pady=5, width=15)
addEntry.grid(row=5, column=1, padx=5, pady=5)
# Search By Name
search = Button(Actions, text='Search By Name',
                command=lambda: v.search(nameentry), padx=5, pady=5, width=15)
search.grid(row=4, column=2, padx=5, pady=5)
# Delete Entry
delete = Button(Actions, text='Delete Entry',
                command=lambda: v.delete(identry), padx=5, pady=5, width=15)
delete.grid(row=5, column=2, padx=5, pady=5)
# Update Entry
update = Button(Actions, text='Update Entry',
                command=lambda: db.update(0), padx=5, pady=5, width=15)
update.grid(row=4, column=3, padx=5, pady=5)
# Display on Map
onMap = Button(Actions, text='Display on Map',
               command=lambda: db.onmap(0), padx=5, pady=5, width=15)
onMap.grid(row=5, column=3, padx=5, pady=5)


# Frame for view box
viewBox = LabelFrame(root, text=' View Box', padx=5, pady=8)
# Scroll bar
scrollbar = Scrollbar(viewBox)
scrollbar.pack(side=RIGHT, fill=Y)
# List box
listbox = Listbox(viewBox, bd=0, yscrollcommand=scrollbar.set,
                  width=80, height=13)
listbox.pack(side="left", fill="both", expand=True)
scrollbar.config(command=listbox.yview)
viewBox.grid(row=1, column=5, rowspan=10, padx=2, pady=2, ipadx=1, ipady=1)

# GUI End


v = db()

# Main loop
root.mainloop()

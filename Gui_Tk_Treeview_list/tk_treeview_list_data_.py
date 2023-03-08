import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import tkinter.messagebox as mb


class ListData(ThemedTk):
    def __init__(self):
        super(ListData, self).__init__()

        self.geometry('800x600')
        self.title('Liste der personenbezogenen Daten')
        self.style = ttk.Style(self)
        self.style.theme_use('alt')

        self.frame = ttk.Frame(self)
        self.frame.pack()
        ttk.Label(self.frame, text='Vorname, Name').grid(row=0, column=0, padx=10, pady=(5, 10))
        self.nameEntry = ttk.Entry(self.frame)
        self.nameEntry.grid(row=0, column=1, padx=10, pady=(5, 10))

        ttk.Label(self.frame, text='Geburtstag').grid(row=1, column=0, padx=10, pady=(5, 10))
        self.birthdayEntry = ttk.Entry(self.frame)
        self.birthdayEntry.grid(row=1, column=1, padx=10, pady=(5, 10))

        ttk.Label(self.frame, text='Telefonnummer').grid(row=2, column=0, padx=10, pady=(5, 10))
        self.phoneNrEntry = ttk.Entry(self.frame)
        self.phoneNrEntry.grid(row=2, column=1, padx=10, pady=(5, 10))

        self.button = ttk.Button(self, text='Eintragen', command=self.addEntry, state= tk.NORMAL)
        self.button.pack()
        columns = ('Vorname, Name', 'Geburtstag', 'Telefonnummer') 
        self.tree = ttk.Treeview(self, columns= columns, show='headings', selectmode='extended')

        for column in columns:
            self.makeHeading(column)
            self.makeColumn(column)
        self.tree.pack(padx=10, pady=10)

    def makeHeading(self, column):
        self.tree.heading(column, text= column)

    def makeColumn(self, column):
        self.tree.column(column, anchor=tk.E, minwidth=0, stretch=tk.NO)

    def addEntry(self):
        name = self.nameEntry.get()
        birthday = self.birthdayEntry.get()
        phone = self.phoneNrEntry.get()

        if len(name) < 2 or len(birthday) < 6 or len(phone) < 8:
            mb.showerror('Error', 'Fehler bei der Eingabe von Vorname, Name, Geburtstag  oder Telefonnummer')
            return
        self.tree.insert('', tk.END, values=(name, birthday, phone))

mylist = ListData()
mylist.mainloop()

# Praxisaufgabe:
# Schreibe eine Klasse, welcher bei der Initialisierung 
# eine Liste mit Strings übergeben wird. Die Klasse soll sich dann
# selbst darum kümmern, dass entsprechend viele 
# Checkbuttons angelegt werden und ein Button zum Auslesen der
# Checkbuttons
# Bsp :
# prog_lang = ['Python', 'C#', 'C++', 'C', 'Ruby', 'Perl', 'Java']

import tkinter as tk 

class Languages(tk.Tk):
    def __init__(self):
        super(Languages, self).__init__()       

        self.languages = ['Python', 'C#', 'C++', 'C', 'Ruby', 'Perl', 'Java']
        self.values = []
        for language in self.languages:
            varTk = tk.IntVar()  
            varTk.set(0)
            self.values.append(varTk)
            
        for index, language in enumerate(self.languages):
            checkBox = self.makeCheckBox(language, index)
            checkBox.pack(anchor = 'w')

        self.button = self.makeButton()
        self.button.pack(expand=True, fill='both')
            
    def makeCheckBox(self, text, index):
        return tk.Checkbutton(self, text = text, font = 'arial 12 bold', variable = self.values[index],
                              height = 2, padx= 10)
                           
    def get_status(self):
        for index, language in enumerate(self.languages):
            print(language, self.values[index].get())  
        
    def makeButton(self):
        return tk.Button(self, text='Show', font = 'arial 12 bold', command=self.get_status)
                   
myapp = Languages()
myapp.mainloop()

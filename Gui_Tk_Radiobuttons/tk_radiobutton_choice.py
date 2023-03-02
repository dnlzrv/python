import tkinter as tk 

class Preference(tk.Tk):
    def __init__(self, optionsListe):
        super(Preference, self).__init__()
        self.geometry('300x200')
        self.title('Choice')
        self.label = tk.Label(self, text = 'Wählen Sie Ihre Präferenz', font=('Helvetica bold', 14)).pack(side= tk.TOP)
        self.optionsListe = optionsListe
        
        self.frame = tk.Frame(self).pack()
        self.variable = tk.IntVar()
        self.variable.set(0)
        self.font = 'Helvetica 10 bold'
        
        for index, option in enumerate(self.optionsListe):
            tk.Radiobutton(self.frame, text= option, font= self.font, variable= self.variable, value = index+1).pack(anchor='w')
            
        tk.Button(self, text= 'Bestätigen', font=self.font, command= self.onButtonClick).pack()
            
    def onButtonClick(self):
        print(self.variable.get())
                   
        
if '__main__'==__name__:
    choiceSugar = ['mit Zucker', 'ohne Zucker', 'mit Zuckerersatz']
    choice = Preference(choiceSugar)
    choice.mainloop()
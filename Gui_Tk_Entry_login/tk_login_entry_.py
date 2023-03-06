# Schreibe ein Login-Fenster. Darin sollen enthalten sein:
# 1) Label: oben, text='Login'
# 2) Frame: mit Inhalt: Label + Entry für Benutzername + Passwort
# 3) Button: text='Login'
# 4) 2 Radiobuttons nebeneinander: "Remember me", "Don't remember me"

import tkinter as tk 
from tkinter import ttk
from ttkthemes import ThemedTk
 

class LoginApp(ThemedTk):
    def __init__(self):
        super(LoginApp, self).__init__()
        self.geometry('300x300')
        self.title('Einloggen')
        
        self.style = ttk.Style(self)
        self.style.theme_use('blue')
        
        self.username = tk.StringVar()
        self.userpass = tk.StringVar()

        self.frame = ttk.Frame(self)
        self.frame.grid()
        self.labelUser = ttk.Label(self, text= 'Login').grid(row=0, column=0, padx=10, pady=(20, 5), sticky='w')
        self.username.trace("w", lambda name, index, mode, sv=self.username: self.onUserNameChanged(self.username))

        self.entryUser = ttk.Entry(self, textvariable= self.username).grid(row=0, column=1, padx=10, pady=(20, 5))
        
        self.labelPass = ttk.Label(self, text= 'Passwort').grid(row=1, column=0, padx=10, pady=(5, 20), sticky='w')
        self.userpass.trace("w", lambda name, index, mode, sv=self.userpass: self.onPasswordChanged(self.userpass))
        self.entryPass = ttk.Entry(self, textvariable= self.userpass, show="*").grid(row=1, column=1, padx=10, pady=(5, 20))
       
        self.buttonSubmit = ttk.Button(self, text= 'Submit', command = self.onButtonClick, state= tk.DISABLED)
        self.buttonSubmit.grid(row=3, column=1, padx=10, pady=(5, 20))

    def onUserNameChanged(self, sv):
        self.updateSubmitButton()
        print(self.username.get())
        return True
    
    def onPasswordChanged(self, sv):
        self.updateSubmitButton()
        print(self.userpass.get())
        return True

    def onButtonClick(self):
        print(self.username.get(), ':', self.userpass.get())
    
    def updateSubmitButton(self):
        if self.isUsernameValid() and self.isPasswortValid():
            self.buttonSubmit['state'] = tk.NORMAL
        else:
            self.buttonSubmit['state'] = tk.DISABLED
        
    def isUsernameValid(self):
        return len(self.username.get()) >= 3
    
    def isPasswortValid(self):
        return len(self.userpass.get()) >= 8
    
if '__main__'==__name__:
          
    myapp = LoginApp()
    myapp.mainloop()
        
# Schreibe ein Login-Fenster. Darin sollen enthalten sein:
# 1) Label: oben, text='Login'
# 2) Frame: mit Inhalt: Label + Entry für Benutzername + Passwort
# 3) Button: text='Login'

import tkinter as tk 

class LoginApp(tk.Tk):
    def __init__(self):
        super(LoginApp, self).__init__()
        self.geometry('300x300')
        self.title('Einloggen')
        
        self.username = tk.StringVar()
        self.userpass = tk.StringVar()

        self.frame = tk.Frame(self)
        self.frame.grid()
        self.labelUser = tk.Label(self, text= 'Login').grid(row= 1, column= 1)
        self.username.trace("w", lambda name, index, mode, sv=self.username: self.onUserNameChanged(self.username))

        self.entryUser = tk.Entry(self, textvariable= self.username).grid(row= 1, column= 2, columnspan=3, sticky='nesw')
        
        self.labelPass = tk.Label(self, text= 'Passwort').grid(row= 2, column= 1)
        self.userpass.trace("w", lambda name, index, mode, sv=self.userpass: self.onPasswordChanged(self.userpass))
        self.entryPass = tk.Entry(self, textvariable= self.userpass, show="*").grid(row= 2, column= 2, columnspan=3, sticky='nesw')
       
        self.buttonSubmit =tk.Button(self, text= 'Submit', command = self.onButtonClick, state= tk.NORMAL).grid(row= 3, column= 2, columnspan=3)

    def onUserNameChanged(self, sv):
        print(self.username.get())
        return True
    
    def onPasswordChanged(self, sv):
        print(self.userpass.get())
        return True

    def onButtonClick(self):
        print(self.username.get(), ':', self.userpass.get())
        
    def isUsernameValid(self):
        return len(self.username.get()) >= 3
    
    def isPasswortValid(self):
        return len(self.userpass.get()) >= 8
    
if '__main__'==__name__:
          
    myapp = LoginApp()
    myapp.mainloop()
        
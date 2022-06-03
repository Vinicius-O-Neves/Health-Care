from tkinter import *

from healthcare.MainApplication import MainApplication
from healthcare.data.firebase.FirebaseDb import FirebaseDb
from healthcare.resources.Colors import Colors


class LoginScreen:

    def __int__(self):
        self.loginScreen = Tk()
        self.loginScreen.title("Login")
        self.loginScreen.configure(bg=Colors().backgroundColor)
        self.app_width = 386
        self.app_height = 680
        self.screen_width = self.loginScreen.winfo_screenwidth()
        self.screen_height = self.loginScreen.winfo_screenheight()
        self.x = (self.screen_width / 2) - (self.app_width / 2)
        self.y = (self.screen_height / 2) - (self.app_height / 2) - 30
        self.loginScreen.geometry(f'{self.app_width}x{self.app_height}+{int(self.x)}+{int(self.y)}')

        # imgLogo = ImageTk.PhotoImage(Image.open("C:/Users/fslim/OneDrive/Desktop/Health Care 2/healthcare/resources/drawable/healthcareLogo.png"))
        # logo = Label(image=imgLogo)
        # logo.pack()
        # logo.place(x=104, y=27)
        # logo.configure(bg=Colors().backgroundColor)

        screenTitle = Label(self.loginScreen, text="Health care", font=("IBM Plex Sans Devanagari", 30))
        screenTitle.pack()
        screenTitle.place(x=82, y=205, width=222, height=43)
        screenTitle.configure(bg=Colors().backgroundColor, fg=Colors().titleColor)

        loginText = Label(self.loginScreen, text="Login", font=("IBM Plex Sans Devanagari", 20))
        loginText.pack()
        loginText.place(x=30, y=279)
        loginText.configure(bg=Colors().backgroundColor)

        emailText = Label(self.loginScreen, text="Email", font=("IBM Plex Sans Devanagari", 14))
        emailText.pack()
        emailText.place(x=46, y=330, height=19)
        emailText.configure(bg=Colors().backgroundColor)

        self.emailInput = Entry(self.loginScreen, font=("IBM Plex Sans Devanagari", 14))
        self.emailInput.pack()
        self.emailInput.place(x=46, y=354, width=294, height=34)
        self.emailInput.configure(bg=Colors().entryColor)

        passwordText = Label(self.loginScreen, text="Password", font=("IBM Plex Sans Devanagari", 14))
        passwordText.pack()
        passwordText.place(x=46, y=409)
        passwordText.configure(bg=Colors().backgroundColor)

        self.passwordInput = Entry(self.loginScreen, font=("IBM Plex Sans Devanagari", 14))
        self.passwordInput.pack()
        self.passwordInput.place(x=46, y=433, width=294, height=34)
        self.passwordInput.configure(bg=Colors().entryColor)

        noAccount = Label(self.loginScreen, text="Ainda não possui uma conta?", font=("IBM Plex Sans Devanagari", 10))
        noAccount.pack()
        noAccount.place(x=35, y=475, width=208)
        noAccount.configure(bg=Colors().backgroundColor)

        registerText = Label(self.loginScreen, text="Registre-se", font=("IBM Plex Sans Devanagari", 10, "bold"))
        registerText.pack()
        registerText.place(x=240, y=475, width=103)
        registerText.configure(bg=Colors().backgroundColor)

        loginButton = Button(self.loginScreen,
                             text="Login",
                             font=("IBM Plex Sans Devanagari", 16),
                             command=self.login
                             )
        loginButton.pack()
        loginButton.place(x=29, y=549, width=328, height=40)
        loginButton.configure(bg=Colors().entryColor)

        self.loginScreen.mainloop()

    def login(self):
        self.firebaseDb = FirebaseDb()
        login = self.firebaseDb.login(self.emailInput.get(), self.passwordInput.get())

        if login:
            self.loginScreen.destroy()
            MainApplication().__int__()

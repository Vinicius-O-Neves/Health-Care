from tkinter import *
from PIL import ImageTk, Image
from healthcare.resources.Colors import Colors
from healthcare.data.firebase.FirebaseDb import FirebaseDb

registerScreen = Tk()
registerScreen.geometry("386x787")
registerScreen.title("Register")
registerScreen.configure(bg=Colors().backgroundColor)

imgLogo = ImageTk.PhotoImage(Image.open("C:/Users/fslim/OneDrive/Desktop/Health Care 2/"
                                        "healthcare/resources/drawable/pharmacist 1.png"))
logo = Label(image=imgLogo)
logo.pack()
logo.place(x=100, y=27)
logo.configure(bg=Colors().backgroundColor)

screenTitle = Label(registerScreen, text="Health care", font=("IBM Plex Sans Devanagari", 30))
screenTitle.pack()
screenTitle.place(x=82, y=205, width=222, height=43)
screenTitle.configure(bg=Colors().backgroundColor, fg=Colors().titleColor)

registerText = Label(registerScreen, text="Registre-se", font=("IBM Plex Sans Devanagari", 20))
registerText.pack()
registerText.place(x=30, y=279)
registerText.configure(bg=Colors().backgroundColor)

emailText = Label(registerScreen, text="Email", font=("IBM Plex Sans Devanagari", 14))
emailText.pack()
emailText.place(x=46, y=330, height=19)
emailText.configure(bg=Colors().backgroundColor)

emailInput = Entry(registerScreen)
emailInput.pack()
emailInput.place(x=46, y=354, width=294, height=34)
emailInput.configure(bg=Colors().entryColor)

cpfText = Label(registerScreen, text="CPF", font=("IBM Plex Sans Devanagari", 14))
cpfText.pack()
cpfText.place(x=46, y=400, height=19)
cpfText.configure(bg=Colors().backgroundColor)

cpfInput = Entry(registerScreen)
cpfInput.pack()
cpfInput.place(x=46, y=424, width=294, height=34)
cpfInput.configure(bg=Colors().entryColor)

passwordText = Label(registerScreen, text="Password", font=("IBM Plex Sans Devanagari", 14))
passwordText.pack()
passwordText.place(x=46, y=470, height=19)
passwordText.configure(bg=Colors().backgroundColor)

passwordInput = Entry(registerScreen)
passwordInput.pack()
passwordInput.place(x=46, y=494, width=294, height=34)
passwordInput.configure(bg=Colors().entryColor)

passwordCheck = Label(registerScreen, text="Confirme o Password", font=("IBM Plex Sans Devanagari", 14))
passwordCheck.pack()
passwordCheck.place(x=46, y=540, height=19)
passwordCheck.configure(bg=Colors().backgroundColor)

passwordCheckInput = Entry(registerScreen)
passwordCheckInput.pack()
passwordCheckInput.place(x=46, y=564, width=294, height=34)
passwordCheckInput.configure(bg=Colors().entryColor)

noRegister = Label(registerScreen, text="Já possui uma conta?", font=("IBM Plex Sans Devanagari", 10))
noRegister.pack()
noRegister.place(x=35, y=600, width=208)
noRegister.configure(bg=Colors().backgroundColor)

loginText = Label(registerScreen, text="Login", font=("IBM Plex Sans Devanagari", 10, "bold"))
loginText.pack()
loginText.place(x=240, y=600, width=60)
loginText.configure(bg=Colors().backgroundColor)

firebaseDb=FirebaseDb(emailInput.get(),passwordInput.get())
registerButton = Button(registerScreen, text="Registre-se", font=("IBM Plex Sans Devanagari", 16),command=self.validate)
registerButton.pack()
registerButton.place(x=29, y=650, width=328, height=40)
registerButton.configure(bg=Colors().entryColor)

registerScreen.mainloop()

def validate(self):
    if self.passwordInput.get() == self.passwordCheckInput:
        self.firebaseDb.login()
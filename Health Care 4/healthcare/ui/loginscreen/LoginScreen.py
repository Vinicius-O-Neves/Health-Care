from tkinter import *
from PIL import ImageTk, Image
from healthcare.resources.Colors import Colors
from healthcare.data.firebase.FirebaseDb import FirebaseDb

loginScreen = Tk()
loginScreen.geometry("386x787")
loginScreen.title("Login")
loginScreen.configure(bg=Colors().backgroundColor)

imgLogo = ImageTk.PhotoImage(Image.open("C:/Users/fslim/OneDrive/Desktop/Health Care 2/healthcare/resources/drawable/healthcareLogo.png"))
logo = Label(image=imgLogo)
logo.pack()
logo.place(x=104, y=27)
logo.configure(bg=Colors().backgroundColor)

screenTitle = Label(loginScreen, text="Health care", font=("IBM Plex Sans Devanagari", 30))
screenTitle.pack()
screenTitle.place(x=82, y=205, width=222, height=43)
screenTitle.configure(bg=Colors().backgroundColor, fg=Colors().titleColor)

loginText = Label(loginScreen, text="Login", font=("IBM Plex Sans Devanagari", 20))
loginText.pack()
loginText.place(x=30, y=279)
loginText.configure(bg=Colors().backgroundColor)

emailText = Label(loginScreen, text="Email", font=("IBM Plex Sans Devanagari", 14))
emailText.pack()
emailText.place(x=46, y=330, height=19)
emailText.configure(bg=Colors().backgroundColor)

emailInput = Entry(loginScreen)
emailInput.pack()
emailInput.place(x=46, y=354, width=294, height=34)
emailInput.configure(bg=Colors().entryColor)

passwordText = Label(loginScreen, text="Password", font=("IBM Plex Sans Devanagari", 14))
passwordText.pack()
passwordText.place(x=46, y=409)
passwordText.configure(bg=Colors().backgroundColor)

passwordInput = Entry(loginScreen)
passwordInput.pack()
passwordInput.place(x=46, y=433, width=294, height=34)
passwordInput.configure(bg=Colors().entryColor)

noAccount = Label(loginScreen, text="Ainda não possui uma conta?", font=("IBM Plex Sans Devanagari", 10))
noAccount.pack()
noAccount.place(x=35,y=475, width=208)
noAccount.configure(bg=Colors().backgroundColor)

registerText = Label(loginScreen, text="Registre-se", font=("IBM Plex Sans Devanagari", 10, "bold"))
registerText.pack()
registerText.place(x=240,y=475, width=103)
registerText.configure(bg=Colors().backgroundColor)

firebaseDb=FirebaseDb(emailInput.get(),passwordInput.get())
loginButton = Button(loginScreen,
                     text="Login",
                     font=("IBM Plex Sans Devanagari", 16),
                     command=firebaseDb.login()
                     )
loginButton.pack()
loginButton.place(x=29, y=549, width=328, height=40)
loginButton.configure(bg=Colors().entryColor)

loginScreen.mainloop()
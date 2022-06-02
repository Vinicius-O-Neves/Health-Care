from tkinter import *
from PIL import ImageTk, Image
from healthcare.data.firebase.model.PersonImcModel import PersonImcModel
from datetime import datetime
from healthcare.ui.imccalculator.controller.classifier.ImcCalculatorRepository import ImcCalculatorRepository
from healthcare.data.firebase.repository.FirebaseRepositoryImp import FirebaseRepositoryImp


class BMICalculatorScreen:
    def __init__(self):
        self.w = Tk()
        self.w.title('HEALTH CARE')
        """self.w.iconbitmap(
            'C:/Users/user/Health-Care/healthcare/resources/images/healthcareicon.ico')  # Icone do programa"""
        self.w['bg'] = '#F2CCCC'
        self.app_width = 386
        self.app_height = 680
        self.screen_width = self.w.winfo_screenwidth()
        self.screen_height = self.w.winfo_screenheight()
        self.x = (self.screen_width / 2) - (self.app_width / 2)
        self.y = (self.screen_height / 2) - (self.app_height / 2) - 30
        self.w.geometry(f'{self.app_width}x{self.app_height}+{int(self.x)}+{int(self.y)}')
        self.w.maxsize(self.app_width, self.app_height)
        self.w.minsize(self.app_width, self.app_height)

        txt1 = Label(self.w,
                     text='Health Care',
                     font=('IBM Plex Sans Devanagari ', 20),
                     bg='#F2CCCC',
                     fg='#FF2113',
                     width=20
                     )
        txt2 = Label(self.w,
                     text='Sexo',
                     font=('IBM Plex Sans Devanagari', 14),
                     bg='#F2CCCC'
                     )
        txt3 = Label(self.w,
                     text='Idade',
                     font=('IBM Plex Sans Devanagari', 14),
                     bg='#F2CCCC'
                     )

        txt4 = Label(self.w,
                     text='Altura',
                     font=('IBM Plex Sans Devanagari', 14),
                     bg='#F2CCCC'
                     )

        txt5 = Label(self.w,
                     text='Peso',
                     font=('IBM Plex Sans Devanagari', 14),
                     bg='#F2CCCC'
                     )

        self.BMIgender = Entry(bg='#CACACA', font=('IBM Plex Sans Devanagari', 14))
        self.BMIage = Entry(bg='#CACACA', font=('IBM Plex Sans Devanagari', 14))
        self.BMIheight = Entry(bg='#CACACA', font=('IBM Plex Sans Devanagari', 14))
        self.BMIweight = Entry(bg='#CACACA', font=('IBM Plex Sans Devanagari', 14))
        self.btnBMI = Button(self.w, text='Calcular',
                             command=self.calcular,
                             font=('IBM Plex Sans Devanagari', 20),
                             bg='#B72CA9')

        #                LAYOUT:

        txt1.place(x=82, y=5, width=222, height=43)
        txt2.place(x=46, y=80)
        self.BMIgender.place(x=46, y=110, width=294, height=34)
        txt3.place(x=46, y=190)
        self.BMIage.place(x=46, y=220, width=294, height=34)
        txt4.place(x=46, y=304)
        self.BMIheight.place(x=46, y=334, width=294, height=34)
        txt5.place(x=46, y=418)
        self.BMIweight.place(x=46, y=448, width=294, height=34)
        self.btnBMI.place(x=31, y=582, width=328, height=40)

        self.w.mainloop()

    def calcular(self):
        self.imcCalculator = ImcCalculatorRepository(
            float(self.BMIweight.get()),
            float(self.BMIheight.get()),
            int(self.BMIage.get()),
            self.BMIgender.get())

        '''resultado_label = Label(self.w, text=str(imcCalculator.calculate()), font=('IBM Plex Sans Devanagari', 14),
                                bg='#F2CCCC',
                                width=20)
        resultado_label.place(x=82, y=680)'''

        # global imgBalance
        self.result_screen = Toplevel()
        self.result_screen.geometry("386x787")
        self.result_screen.maxsize(386, 787)
        self.result_screen.minsize(386, 787)
        """self.result_screen.iconbitmap(
            'C:/Users/user/Health-Care/healthcare/resources/images/healthcareicon.ico')  # Icone do programa"""
        self.result_screen['bg'] = '#F2CCCC'
        self.BMIResult = Label(self.result_screen, text='Seu IMC é de', font=('Oswald', 36),
                               bg='#F2CCCC')
        self.BMIResult.place(x=49, y=57)
        """imgBalance = ImageTk.PhotoImage(
            Image.open('C:/Users/user/Health-Care/healthcare/resources/images/balançaResultado.png'))"""
        # self.img = Label(self.result_screen, image=imgBalance, bg='#F2CCCC')
        # self.img.place(x=49, y=139)
        self.resultado_label = Label(self.result_screen,
                                     text=str(self.imcCalculator.calculate()),
                                     font=('Oswald', 36),
                                     bg='#F2CCCC', fg='#E37526'
                                     )
        self.resultado_label.pack()
        self.resultado_label.place(x=133, y=109)
        self.clas_label = Label(self.result_screen,
                                text='De acordo com a Organização '
                                     'Mundial da\n Saúde (OMS), '
                                     'você está classificado em\n',
                                font=('Oswald', 14),
                                bg='#F2CCCC')

        self.clas_label.place(x=8, y=414)

        self.classificacao = Label(self.result_screen,
                                   text=str(self.imcCalculator.analyze()),
                                   font=('Oswald', 26),
                                   bg='#F2CCCC',
                                   fg='#E37526'
                                   )
        self.classificacao.place(x=89, y=509)
        self.btnSave = Button(self.result_screen,
                              text='Salvar resultado',
                              font=('IBM Plex Sans Devanagari', 20),
                              bg='#B72CA9',
                              command=self.saveResult
                              )
        self.btnSave.place(x=31, y=582, width=328, height=40)

    def saveResult(self):
        FirebaseRepositoryImp.sendImcToFirebase(
            PersonImcModel("4cd5c7c0-7918-40a8-a551-aed42b817524",
                           datetime.today().strftime("%Y-%m-%d").replace('-', ''),
                           {'IMC': self.imcCalculator.calculate(),
                            'classification': self.imcCalculator.analyze()}))


BMICalculatorScreen()

import asyncio
from datetime import datetime
from tkinter import *

from PIL import ImageTk, Image
from healthcare.data.firebase.model.PersonImcModel import PersonImcModel
from healthcare.data.firebase.repository.FirebaseRepositoryImp import FirebaseRepositoryImp
from healthcare.ui.imccalculator.controller.classifier.ImcCalculatorRepository import ImcCalculatorRepository


#     -----   TELA DE INPUTS PARA O CALCULO DO IMC ----- '''

class BMICalculatorScreen:

    def __init__(self, notebook):
        self.w = Frame(notebook, background="#F2CCCC")
        self.w.pack(fill="both", expand=1)

        """self.w.iconbitmap(
            'C:/Users/user/Health-Care/healthcare/resources/images/healthcareicon.ico')  # Icone do programa"""
        self.resp = Label(self.w,
                          text='',
                          font=('IBM Plex Sans Devanagari', 14),
                          bg='#F2CCCC',
                          fg='#FF2113')
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
                             command=self.Validar,
                             font=('IBM Plex Sans Devanagari', 20),
                             bg='#B72CA9')

        #     -----   LAYOUT DA TELA DE CALCULAR IMC  ----- '''

        txt1.pack(padx=82, pady=5)
        txt2.place(x=30, y=58)
        self.BMIgender.place(x=46, y=110, width=294, height=34)
        txt3.place(x=30, y=145)
        self.BMIage.place(x=46, y=200, width=294, height=34)
        txt4.place(x=30, y=240)
        self.BMIheight.place(x=46, y=304, width=294, height=34)
        txt5.place(x=30, y=340)
        self.BMIweight.place(x=46, y=410, width=294, height=34)
        self.resp.place(x=82, y=470, width=222, height=43)
        self.btnBMI.place(x=31, y=582, width=328, height=40)

    #     -----   VALIDAÇÃO DAS ENTRADAS  ----- '''
    def Validar(self):
        try:
            i = int(self.BMIage.get())
            a = float(self.BMIheight.get())
            p = float(self.BMIweight.get())
            s = str(self.BMIgender.get()).lower()

            if s != 'masculino' and s != 'feminino':
                self.resp.config(text='SEXO INVÁLIDO')
            elif p <= 0 or p > 595:
                self.resp.config(text='PESO INVÁLIDO')
            elif a <= 0 or a > 2.51:
                self.resp.config(text='ALTURA INVÁLIDA ')
            elif i <= 0:
                self.resp.config(text='IDADE INVÁLIDA ')
            else:
                self.resp.config(text='')
                self.btnBMI.config(command=self.calcular)

        except ValueError:
            self.resp.config(text='DADO INVÁLIDO,\nUSE "." AO INVÉS DE ",".')

    #     -----   BOTÃO DE CALCUALR O IMC ----- '''

    def calcular(self):
        i = int(self.BMIage.get())
        a = float(self.BMIheight.get())
        p = float(self.BMIweight.get())
        s = str(self.BMIgender.get()).lower()
        self.imcCalculator = ImcCalculatorRepository(p, a, i, s)
        global result_screen

        try:
            result_screen.destroy()
        except (AttributeError, NameError):
            pass

        #     -----   TELA DE RESULTADO DO CALCULO DO IMC ----- '''

        result_screen = Toplevel()
        self.app_width = 386
        self.app_height = 680
        self.screen_width = self.w.winfo_screenwidth()
        self.screen_height = self.w.winfo_screenheight()
        self.x = (self.screen_width / 2) - (self.app_width / 2) - 300
        self.y = (self.screen_height / 2) - (self.app_height / 2) - 30
        result_screen.geometry(f'{self.app_width}x{self.app_height}+{int(self.x)}+{int(self.y)}')
        result_screen.maxsize(self.app_width, self.app_height)
        result_screen.minsize(self.app_width, self.app_height)
        """self.result_screen.iconbitmap(
            'C:/Users/user/Health-Care/healthcare/resources/images/healthcareicon.ico')  # Icone do programa"""
        result_screen['bg'] = '#F2CCCC'
        #   Texto introdutorio "Seu IMC"
        self.BMIResult = Label(result_screen, text='Seu IMC é de', font=('Oswald', 36),
                               bg='#F2CCCC')

        #     -----   VALOR DO IMC ----- '''

        self.resultado_label = Label(result_screen,
                                     text=str(self.imcCalculator.calculate()),
                                     font=('Oswald', 36),
                                     bg='#F2CCCC', fg='#E37526'
                                     )
        #self.imgBalance = ImageTk.PhotoImage(
            #Image.open('healthcare/ui/imccalculator/balance.png'))
        #self.img = Label(result_screen, image=self.imgBalance, bg='#F2CCCC')

        #     -----   TEXTO DE CLASSIFICAÇÃO DO IMC ----- '''

        self.clas_label = Label(result_screen,
                                text='De acordo com a Organização '
                                     'Mundial da\n Saúde (OMS), '
                                     'você está classificado em:\n',
                                font=('Oswald', 14),
                                bg='#F2CCCC')
        self.classificacao = Label(result_screen,
                                   text=str(self.imcCalculator.analyze()),
                                   font=('Oswald', 26),
                                   bg='#F2CCCC',
                                   fg='#E37526'
                                   )
        #     -----   BOTÃO PARA SALVAR O RESULTADO DO CALCULO DO IMC ----- '''

        self.btnSave = Button(result_screen,
                              text='Salvar resultado',
                              font=('IBM Plex Sans Devanagari', 20),
                              bg='#B72CA9',
                              command=self.saveResult
                              )

        #     -----   LAYOUT DA PAGINA DE RESULTADO -----

        self.BMIResult.pack(pady=50)
        self.resultado_label.pack()
        # self.img.pack(pady=5)
        self.clas_label.pack()
        self.classificacao.pack(pady=20)
        self.btnSave.pack(pady=10)

    #     -----   COMANDO DE SALVAR O RESULTADO  -----

    def saveResult(self):
        asyncio.run(
            FirebaseRepositoryImp.sendImcToFirebase(
                PersonImcModel("4cd5c7c0-7918-40a8-a551-aed42b817524",
                               datetime.today().strftime("%Y-%m-%d").replace('-', ''),
                               {'IMC': self.imcCalculator.calculate(),
                                'classification': self.imcCalculator.analyze()}))
        )

#Decida por mim
#faça uma pergunta para o progama e ele terá que te dar uma resposta
import random
import PySimpleGUI as sg

class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Com certeza, você deve fazer isso!',
            'Não sei, você sabe',
            'Não faz isso não!',
            'Acho que tá na hora certa!'
        ]

    def Iniciar(self):
        
        layout = [
            [sg.Text('Faça sua pergunta')],
            [sg.Input()],
            [sg.Output(size=(35,10))],
            [sg.Button('Decida por mim')]
        ]

        self.janela = sg.Window('Decida por mim!',layout=layout)
        while True:
            self.eventos, self.valores = self.janela.read()

            if self.eventos == 'Decida por mim':
                print(random.choice(self.respostas))
                self.janela.close()
decida = DecidaPorMim()
decida.Iniciar()
#jogo de Aventura
#um jogo de decisões onde eu terei que criar varios finais diferentes baseados nas respostas que forem dadas
import PySimpleGUI as sg

class JogoDeAventura:
    def __init__(self):
        self.pergunta1 = 'Você nasceu no norte ou sul (n/s)'
        self.pergunta2 = 'Você prefere a espada ou escudo? (espada/escudo)'
        self.pergunta3 = 'Qual é sua especialidade? (linha de frente/tatico)' 
        self.finalhistoria1 = 'Você sera um heroi na linha de frente!'
        self.finalhistoria2 = 'Você será um heroi protegendo todas as nossas tropas!'
        self.finalhistoria3 = 'Você ira se sacrificar na batalha'
        self.finalhistoria4 = 'Você não é capaz de lutar nessa batalha!'

    def Iniciar(self):

        layout = [
            [sg.Output(size=(50,2))],
            [sg.Input(size=(25,0),key='escolha')],
            [sg.Button('Iniciar'),sg.Button('Responder')]
        ]

        self.janela = sg.Window('Jogo de Aventura!',layout=layout)
        while True:

            self.LerValores()

            if self.eventos == 'Iniciar':
                print(self.pergunta1)
                self.LerValores()
                if self.valores['escolha'] == 'n':
                    print(self.pergunta2)
                    self.LerValores()
                    if self.valores['escolha'] == 'espada':
                        print(self.finalhistoria1)
                    if self.valores['escolha'] == 'escudo':
                        print(self.finalhistoria2)
                if self.valores['escolha'] == 's':
                    print(self.pergunta3)
                    self.LerValores()
                    if self.valores['escolha'] == 'linha de frente':
                        print(self.finalhistoria3)
                    if self.valores['escolha'] == 'tatico':
                        print(self.finalhistoria4)


    def LerValores(self):
        self.eventos, self.valores = self.janela.read()

jogo = JogoDeAventura()
jogo.Iniciar()
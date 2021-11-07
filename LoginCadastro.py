import PySimpleGUI as sg
import easygui as eg

#DEFINIR PROPRIEDADES DA JANELA 1 - LOGAR NO SISTEMA
def Entrar():
    sg.theme('GreenTan')
    Layout = [
        [sg.Text('Usuario', size=(7, 0)), sg.Input(size=(30, 5), key='user')],
        [sg.Text('senha',size=(7, 0)), sg.Input(size=(30, 5), key='pass')],
        [sg.Button('Entrar'), sg.Button('Sair')]
    ]
    return sg.Window('Sistema de Cadastro', layout=Layout, finalize=True)

#DEFINIR PROPRIEDADES DA JANELA 2 - CADASTRAR USUÁRIO
def Cadastrar():
    sg.theme('GreenTan')
    Layout = [
        [sg.Text('Nome', size=(10, 0)), sg.Input(size=(50, 0), key='nome')],
        [sg.Text('CPF', size=(10, 0)), sg.Input(size=(50, 0), key='cpf')],
        [sg.Text('Arquivo', size=(10, 0)), sg.Input(size=(50, 0), key='arquivo'), sg.Button('...')],
        [sg.Checkbox('Fumante?', key='fuma')],
        [sg.Checkbox('Trabalhador?', key='trabalha')],
        [sg.Output(size=(70, 10))],
        [sg.Button('Cadastrar'), sg.Button('Fechar')]
    ]
    return sg.Window('Sistema de Cadastro', layout=Layout, finalize=True)

#DEFINIR VARIAVEIS PARA ABRIR JANELAS
janela1, janela2 = Entrar(), None

#LOOP PARA EFETUAR PROCESSOS DAS JANELAS
while True:
    #VARIAVEIS COM DEFINIÇÃO DE PROPRIEDADES DAS JANELAS
    window, event, values = sg.read_all_windows()

    #JANELA 1 ABERTA / LOGAR NO SISTEMA
    if window == janela1:
        if event == 'Entrar':
            usuario = values['user']
            senha = values['pass']

            if int(len(usuario)) < 7 and int(len(senha)) < 7:
                sg.popup('Usuario e senha incorretos')
            elif int(len(usuario)) < 7:
                sg.popup('Usuario incorreta')
            elif int(len(senha)) < 7:
                sg.popup('Senha incorreta')
            else:
                janela2 = Cadastrar()
                janela1.hide()
        #AO FECHAR JANELA 1 DE LOGIN
        if event == 'Sair':
            sg.popup('Obrigado por testar nosso sistema! Até a próxima..\nThank you!')
            break
        elif event == sg.WIN_CLOSED:
            sg.popup('Obrigado por testar nosso sistema! Até a próxima..\nThank you!')
            break

    #JANELA 2 DE CADASTRO ABERTA / CADASTRAR USUÁRIO
    if window == janela2:
        if event == 'Cadastrar':
            nome = values['nome']
            cpf = values['cpf']

            if int(len(nome)) < 1:
                sg.popup('Favor inserir o Nome...')
            elif int(len(cpf)) < 1:
                sg.popup('Favor inserir o CPF...')
            else:
                if values['fuma'] == True:
                    fuma = 'Sim'
                else:
                    fuma = 'Nao'
                if values['trabalha'] == True:
                    trabalha = 'Sim'
                else:
                    trabalha = 'Nao'

                print('O usuário ' + str(nome) + ' foi cadastrado com sucesso!\n')
                print('Nome: ' + str(nome))
                print('CPF: ' + str(cpf))
                print('Fumante: ' + str(fuma))
                print('Trabalhador: ' + str(trabalha))

                sg.popup('Usuário cadastrado com sucesso!')

        #SELECIONANDO ARUQIVO
        if event == '...':
            path = eg.fileopenbox()
            janela2.Element('arquivo').Update(path, disabled=True)
            print('OK')

        #AO FECHAR JANELA 2 DE CADASTRO
        if event == 'Fechar':
            janela2.hide()
            janela1.un_hide()

        if event == sg.WIN_CLOSED:
            sg.popup('Obrigado por testar nosso sistema! Até a próxima..\nThank you!')
            break
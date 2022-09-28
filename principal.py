import uteis as ut
import PySimpleGUI as sg
layout = [[sg.Text('SEJA BEM VINDO AO SISTEMA DE LOGIN DO CAUÃ')],
          [sg.Text('Usuário')],
          [sg.Input(key='usuario')],
          [sg.Text('Senha')],
          [sg.Input(key='senha')],
          [sg.Text('',key='mensagem')],
          [sg.Button('Cadastrar', size = (20, 2)),sg.Button('Entrar', size = (20, 2))]]
layout_cadastro = [[sg.Text('Cadastrar nova conta')],
          [sg.Text('Usuário')],
          [sg.Input(key='usuario')],
          [sg.Text('Senha')],
          [sg.Input(key='senha')],
          [sg.Text('Digite sua senha novamente')],
          [sg.Input(key='senha2')],
          [sg.Text('',key='mensagem')],
          [sg.Button('Cadastrar', size = (40, 2))]]
window = sg.Window('Login', layout=layout)
arquivo = 'Cadastros_sistema_de_login_caua'
if not ut.arquivoExiste(arquivo):
    ut.criaArquivo(arquivo)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Cadastrar':
        while True:
            window = sg.Window('Cadastro', layout=layout_cadastro)
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == 'Cadastrar':
                break

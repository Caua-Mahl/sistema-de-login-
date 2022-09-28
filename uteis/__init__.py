import PySimpleGUI as sg
# função verifica se existe o arquivo txt.
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


# função cria arquivo txt.
def criaArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print(f'erro ao criar arquivo {nome}')

# fu



#função de cadastro no arquivo txt
def cadastra_arquivo(arq, usuario, senha):
    try:
        a = open(arq, 'at')
    except:
        print('erro ao cadastrar arquivo')
    else:
        a.write(f'{usuario} {senha}')
        a.close()


def janela_login():
    layout = [[sg.Text('SEJA BEM VINDO AO SISTEMA DE LOGIN DO CAUÃ')],
              [sg.Text('Usuário:')],
              [sg.Input(key='usuario')],
              [sg.Text('Senha:')],
              [sg.Input(key='senha', password_char = "*")],
              [sg.Text('', key='mensagem')],
              [sg.Button('Cadastrar', size=(20, 2)), sg.Button('Entrar', size=(20, 2))]]
    return sg.Window('Login', layout=layout, finalize = True)
def janela_cadastro():
    layout_cadastro = [[sg.Button('Voltar', size =(40,1))],
                       [sg.Text('Usuário:')],
                       [sg.Input(key='usuario')],
                       [sg.Text('Senha:')],
                       [sg.Input(key='senha', password_char = "*")],
                       [sg.Text('Digite sua senha novamente:')],
                       [sg.Input(key='senha2')],
                       [sg.Text('', key='mensagem', password_char = "*")],
                       [sg.Button('Cadastrar', size=(40, 2))]]
    return sg.Window('Cadastro', layout=layout_cadastro, finalize = True)

def ler_arquivo(arq):
    return arq.read()
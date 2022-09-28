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

# função de leitura de arquivo txt .
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('erro ao ler arquivo')
    else:
        print(a.read())
    finally:
        a.close()



#função de cadastro no arquivo txt
def cadastraArquivo(arq, nome):
    try:
        a = open(arq, 'at')
    except:
        print('erro ao cadastrar no arquivo')
    else:
        a.write(f'{nome} \n')
        #a.write(f"{nome['nome']} {nome['idade']} {nome['id']} {nome['sexo']} {nome['peso']} {nome['altura']} {nome['idade']} {nome['plano']} {nome['imc']} {nome['bf']}")
        a.close()

# função valida usuario.
def valida_usuario(nome):
    while True:
        v = (nome.isalnum())
        return v

def janela_login():
    layout = [[sg.Text('SEJA BEM VINDO AO SISTEMA DE LOGIN DO CAUÃ')],
              [sg.Text('Usuário:')],
              [sg.Input(key='usuario')],
              [sg.Text('Senha:')],
              [sg.Input(key='senha')],
              [sg.Text('', key='mensagem')],
              [sg.Button('Cadastrar', size=(20, 2)), sg.Button('Entrar', size=(20, 2))]]
    return sg.Window('Login', layout=layout, finalize = True)
def janela_cadastro():
    layout_cadastro = [[sg.Button('Voltar', size =(40,1))],
                       [sg.Text('Usuário:')],
                       [sg.Input(key='usuario')],
                       [sg.Text('Senha:')],
                       [sg.Input(key='senha')],
                       [sg.Text('Digite sua senha novamente:')],
                       [sg.Input(key='senha2')],
                       [sg.Text('', key='mensagem')],
                       [sg.Button('Cadastrar', size=(40, 2))]]
    return sg.Window('Cadastro', layout=layout_cadastro, finalize = True)
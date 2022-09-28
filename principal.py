import uteis as ut
import PySimpleGUI as sg
arquivo = 'Cadastros_sistema_de_login_caua'
if not ut.arquivoExiste(arquivo):
    ut.criaArquivo(arquivo)
janela1, janela2 = ut.janela_login(), None
while True:
    window, event, values = sg.read_all_windows()
    #leitura = str(ut.ler_arquivo(arquivo))
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    if window == janela1 and event == 'Cadastrar':
        janela2 = ut.janela_cadastro()
        janela1.hide()
    if window == janela2 and event == sg.WIN_CLOSED:
        break
    if window == janela2 and event == 'Voltar':
        janela1 = ut.janela_login()
        janela2.hide()
    if window == janela2 and event == 'Cadastrar':
        if values['usuario'].isalnum() and 5 <len(values['usuario'])<12:
            if 5<len(values['senha'])<12:
                if values['senha'] == values['senha2']:
                    sg.popup('Você se cadastrou com sucesso!', title='Cadastrado')
                    janela1 = ut.janela_login()
                    janela2.hide()
                    ut.cadastra_arquivo(arquivo,values['usuario'], values['senha'] )
                else:
                   window['mensagem'].update('As senhas precisam ser iguais!')
            else:
                window['mensagem'].update('Senha inválida, ela deve possuir:\nno mínimo 6 e no máximo 11 caracteres\n')
        else:
           window['mensagem'].update('Usuário inválido, ele deve possuir:\no mínimo 6 e no máximo 11 caracteres.\nApenas letras e números.\nNão estar sendo utilizado')
    if window == janela1 and event == 'Entrar':
        if values['usuario'].isalnum() and 5 <len(values['usuario'])<12:
            if 5<len(values['senha'])<12:
                sg.popup('Você logou com sucesso!', title='Logado')
                janela1.hide()
            else:
                window['mensagem'].update('Usuário ou senha inválida')
        else:
           window['mensagem'].update('Usuário ou senha inválida')
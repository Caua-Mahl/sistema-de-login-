import uteis as ut
import PySimpleGUI as sg
arquivo = 'Cadastros_sistema_de_login_caua'
if not ut.arquivoExiste(arquivo):
    ut.criaArquivo(arquivo)
janela1, janela2 = ut.janela_login(), None
while True:
    window, event, values = sg.read_all_windows()
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
        if values['usuario'].isalnum() and 5 <len(values['usuario'])<15:
            sg.popup('Você se cadastrou com sucesso!', title= 'Cadastrado')
            janela1 = ut.janela_login()
            janela2.hide()
        else:
            window
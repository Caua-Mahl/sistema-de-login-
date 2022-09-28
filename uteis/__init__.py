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
        linhas(f'erro ao criar arquivo {nome}')

# função de leitura de arquivo txt .
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        linhas('erro ao ler arquivo')
    else:
        print(a.read())
    finally:
        a.close()

def cadastraArquivo(arq, nome):
    try:
        a = open(arq, 'at')
    except:
        linhas('erro ao cadastrar no arquivo')
    else:
        a.write(f'{nome} \n')
        #a.write(f"{nome['nome']} {nome['idade']} {nome['id']} {nome['sexo']} {nome['peso']} {nome['altura']} {nome['idade']} {nome['plano']} {nome['imc']} {nome['bf']}")
        a.close()
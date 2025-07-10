import os

### @Author: Matheus Falcão
 
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "storage"))
 
def save(nome_arquivo, dados) -> None:
    """
    Registra um novo conjunto de dados no arquivo.
    Se o arquivo não existir, ele será criado.
    Cada linha será registrada no formato: identificador:[["Chave", "Valor"], ...]
    
    Args:
        nome_arquivo (str): Nome do arquivo.
        dados (list): Dados a serem registrados.
    
    """
    caminho = os.path.join(BASE_DIR, nome_arquivo + ".txt")
    identificador = "1"

    arquivo = open(caminho, "r")
    linhas = arquivo.readlines()
    arquivo.close()

    if linhas:
        ultimos_ids = [int(linha.split(":")[0]) for linha in linhas]
        identificador = str(max(ultimos_ids) + 1)

    linha = identificador + ":" + str(dados) + "\n"
    arquivo = open(caminho, "a")
    arquivo.write(linha)
    arquivo.close()
    
    print("Registro salvo com sucesso.")

def list_all(nome_arquivo) -> list:
    """
    Leitura de dados armazenados em um arquivo.
    
    Args:
        nome_arquivo (str): Nome do arquivo.
    
    Returns: 
        list: Dados lidos do arquivo
    """
    
    caminho = os.path.join(BASE_DIR, nome_arquivo + ".txt")
    linhas = []

    arquivo = open(caminho, "r")
    linhas = arquivo.readlines()
    arquivo.close()
    
    return linhas

def get_by_id(nome_arquivo, identificador) -> str:
    """
    Busca um conjunto de dados pelo identificador.
    
    Args:
        nome_arquivo (str): Nome do arquivo.
        identificador (str): Identificador do conjunto de dados.
    
    Returns: 
        str: Dados lidos do arquivo
    """
    
    linhas = list_all(nome_arquivo)
    
    for linha in linhas:
        if linha.startswith(identificador + ":"):
            return linha.strip()
    
    return "Registro não encontrado."

def update(nome_arquivo, identificador, chave, novo_valor) -> None:
    """
    Atualiza um conjunto de dados pelo identificador.
    
    Args:
        nome_arquivo (str): Nome do arquivo.
        identificador (str): Identificador do conjunto de dados.
        chave (str): Chave do par a ser atualizado.
        novo_valor (str): Novo valor do par.
    """
    
    caminho = os.path.join(BASE_DIR, nome_arquivo + ".txt")
    linhas = list_all(nome_arquivo)
    nova_lista = []

    for linha in linhas:
        if linha.startswith(identificador + ":"):
            partes = linha.strip().split(":", 1)
            lista = eval(partes[1])
            for par in lista:
                if par[0] == chave:
                    par[1] = novo_valor
            nova_linha = identificador + ":" + str(lista) + "\n"
            nova_lista.append(nova_linha)
        else:
            nova_lista.append(linha)

    arquivo = open(caminho, "w")
    arquivo.writelines(nova_lista)
    arquivo.close()
    
    print("Registro atualizado com sucesso.")
    
def remove(nome_arquivo, identificador):
    caminho = os.path.join(BASE_DIR, nome_arquivo + ".txt")
    linhas = list_all(nome_arquivo)
    nova_lista = []

    for linha in linhas:
        if not linha.startswith(identificador + ":"):
            nova_lista.append(linha)

    arquivo = open(caminho, "w")
    arquivo.writelines(nova_lista)
    arquivo.close()
    
    print("Registro removido com sucesso.")
import requests
import json
from bancodedados import BancoDeDados

def main():
    url = "http://dadosabertos.ibama.gov.br/dados/SICAFI/AC/Quantidade/multasDistribuidasBensTutelados.json"
    response = requests.get(url)
    if response.status_code == 200:
        print("Acessando dados abertos do IBAMA...")
        lista_processos = response.json()
        processo_fauna = []
        processo_flora = []
        processo_pesca = []
        processo_outras = []
        print("Agrupando os processos...")
        for processo in lista_processos['data']:
            if processo["tipoInfracao"] == "Fauna":
                processo_fauna.append(processo)
            elif processo["tipoInfracao"] == "Flora":
                processo_flora.append(processo)
            elif processo["tipoInfracao"] == "Pesca":
                processo_pesca.append(processo)
            elif processo["tipoInfracao"] == "Outras":
                processo_outras.append(processo)
        print("Salvando os processos no firebase...")
        BancoDeDados.salvar_firebase(processo_fauna, "Fauna")
        BancoDeDados.salvar_firebase(processo_flora, "Flora")
        BancoDeDados.salvar_firebase(processo_pesca, "Pesca")
        BancoDeDados.salvar_firebase(processo_outras, "Outras")
        print("Salvo no Firebase!")
    else:
        print("Não foi possível acessar a base de dados")


  
if __name__ == "__main__":
    main()
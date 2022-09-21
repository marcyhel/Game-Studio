import os

diretorio="newPlayer/Player/TakeGrenade/"
cont=0
for nome in os.listdir(diretorio):
    # alterar conforme sua necessidade de geração de nomes e layout de arquivos    
    dados = str(nome).split(".")
    numero = dados[0].split("_")[1]
    subnumero = dados[1]
    novo_nome = str(cont)+".png"
    cont+=1
    print(nome)
    os.rename(diretorio+nome, diretorio+novo_nome)
    print("arquivo " + nome + " alterado para " + novo_nome)
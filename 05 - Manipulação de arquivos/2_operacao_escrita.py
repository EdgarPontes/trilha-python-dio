arquivo = open(
    "/home/edgar/workspacepython/trilha-python-dio/05 - Manipulação de arquivos/teste.txt", "w"
)
arquivo.write("Escrevendo dados em um novo arquivo.")
arquivo.writelines(["\n", "escrevendo", "\n", "um", "\n", "novo", "\n", "texto"])

arquivo.close()

arquivo = open(
    "/home/edgar/workspacepython/trilha-python-dio/05 - Manipulação de arquivos/teste.txt", "r"
)
print(arquivo.read())
arquivo.close()
#Descrição
#O desafio consiste em adicionar à função contar_caracteres um dicionário vazio chamado contador para armazenar as contagens de caracteres. Vamos iterar através de cada caractere na string. Para cada caractere, verifique se ele já está presente no dicionário contador. Se estiver, incremente o valor associado a essa chave. Caso contrário, adicione a chave ao dicionário com valor inicial 1. Neste dicionário, as chaves são os caracteres presentes na string e os valores correspondem à contagem de vezes que cada caractere aparece.
#
#Documentação Oficial:
#https://docs.python.org/pt-br/3/tutorial/datastructures.html#dictionaries
#
#Entrada
#A função espera receber uma única string como entrada. Neste desafio, consideramos como casos de teste apenas strings textuais.
#
#Saída
#A função retorna um dicionário onde cada chave é um caractere presente na string de entrada e o valor associado a cada chave é a quantidade de vezes que o caractere ocorre na string.

def contar_caracteres(string):
#TODO: Inicialize um dicionário vazio 'contador' para armazenar as contagens de caracteres.:
    contador = {}
#TODO: Itere através de cada caractere na string.
#TODO: Para cada caractere, verifique se ele já está presente no dicionário contador:
    contem = 0
    for caracter in string:

        if caracter in contador:
            contem = contador[caracter] + 1
            contador.update({caracter: contem})
        else:
            contador[caracter] = 1
            contem = 1

    return contador

# Solicita entrada do usuário
entrada = input()
resultado = contar_caracteres(entrada)
print(resultado)


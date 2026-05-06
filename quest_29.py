# 29) Escreva um programa que substitua todas as ocorrências de uma determinada palavra em uma frase por outra palavra fornecida pelo usuário.

frase = input("Digite uma frase: ")
palavra_antiga = input("Digite a palavra que deseja substituir: ")
nova_palavra = input("Digite a nova palavra: ")

frase_modificada = frase.replace(palavra_antiga, nova_palavra)

print("Frase modificada:", frase_modificada)

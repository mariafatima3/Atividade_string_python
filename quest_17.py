# 17) Escreva um programa que solicite ao usuário para digitar uma frase e conte quantas palavras existem na frase.

frase = input("Digite uma frase: ")
palavras = frase.split()

quantidade = len(palavras)

print("A frase contém", quantidade, "palavras.")
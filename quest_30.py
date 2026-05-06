# 30) Escreva um programa que peça ao usuário para digitar seu nome completo e, em seguida, imprima apenas o sobrenome.
nome = input("Digite seu nome completo: ")
palavras = nome.split()
sobrenome = palavras[-1]
print("Seu sobrenome é:", sobrenome)
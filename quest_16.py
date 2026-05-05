# 16) Escreva um programa que peça ao usuário para digitar seu nome completo e imprima apenas o primeiro nome.

nome_completo = input("Digite seu nome completo: ")
partes = nome_completo.split()

primeiro_nome = partes[0]

print("Seu primeiro nome é:", primeiro_nome)
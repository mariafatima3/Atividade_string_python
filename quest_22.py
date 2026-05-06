# 22) Escreva um programa que solicite ao usuário para digitar uma frase e conte quantas vezes uma determinada letra aparece na frase.

frase = input("Digite uma frase: ")
letra = input("Digite a letra que deseja contar: ")
quantidade = frase.count(letra)

print("A letra aparece", quantidade, "vezes na frase.")
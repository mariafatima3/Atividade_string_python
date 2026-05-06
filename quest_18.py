# 18) Escreva um programa que solicite ao usuário para digitar uma frase e verifique se ela termina com um ponto final.

frase = input("Digite uma frase: ")

if frase.endswith("."):
    print("A frase termina com ponto final.")
else:
    print("A frase NÃO termina com ponto final.")
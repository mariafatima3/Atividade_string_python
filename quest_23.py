# 23) Escreva um programa que solicite ao usuário para digitar uma frase e verifique se todas as palavras estão em letras maiúsculas.

frase = input("Digite uma frase: ")
palavras = frase.split()

todas_maiusculas = all(palavra.isupper() for palavra in palavras)

if todas_maiusculas:
    print("Todas as palavras estão em letras maiúsculas.")
else:
    print("Nem todas as palavras estão em letras maiúsculas.")
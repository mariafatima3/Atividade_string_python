# 19) Escreva um programa que solicite ao usuário para digitar uma frase e verifique se ela contém a palavra "Python".

frase = input("Digite uma frase: ")
palavra = "python"

if palavra in frase.lower():
    print("A frase contém a palavra Python.")
else:
    print("A frase NÃO contém a palavra Python.")
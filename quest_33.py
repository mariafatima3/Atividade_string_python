# 33) Escreva um programa que solicite ao usuário para digitar seu nome e, em seguida, imprima as iniciais do nome em letras maiúsculas.

nome = input("Digite seu nome completo: ")
palavras = nome.split()

iniciais = ""
for palavra in palavras:
    if palavra:  
        iniciais += palavra[0].upper()
        
print("Suas iniciais são:", iniciais)

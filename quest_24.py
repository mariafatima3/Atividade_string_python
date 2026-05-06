# 24) Escreva um programa que solicite ao usuário para digitar seu endereço de e-mail e extraia o nome de usuário (parte antes do "@") e o domínio (parte depois do "@").

email = input("Digite seu endereço de e-mail: ")

if "@" in email and email.count("@") == 1:
    
    usuario, dominio = email.split("@")
    
    print("Nome de usuário:", usuario)
    print("Domínio:", dominio)
else:
    
    print("E-mail inválido! Certifique-se de digitar um endereço com apenas um '@'.")
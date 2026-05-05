# 10) Escreva um programa que solicite ao usuário seu nome completo e imprima as iniciais de cada palavra em letras maiúsculas. 
# Por exemplo, se o nome for "Fulano de Tal", o programa deve imprimir "F.D.T."

nome = input("Digite seu nome completo: ")
palavras = nome.split()

iniciais = [palavra[0].upper() for palavra in palavras if palavra]

resultado = ".".join(iniciais) + "."

print(resultado)
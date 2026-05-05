# 12) Escreva um programa que solicite ao usuário uma frase e imprima uma mensagem formatada mostrando a quantidade de caracteres, 
# palavras e linhas na frase.

frase = input("Digite uma frase: ")

quant_caracteres = len(frase)
quant_palavras = len(frase.split())
quant_linhas = len(frase.splitlines())

print(f"Caracteres: {quant_caracteres}")
print(f"Palavras: {quant_palavras}")
print(f"Linhas: {quant_linhas}")
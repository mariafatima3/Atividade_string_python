# 32) Escreva um programa para ler uma frase, imprima esta frase com as palavras ordenadas em ordem crescente de comprimento das strings.

frase = input("Digite uma frase: ")

palavras = frase.split()
palavras_ordenadas = sorted(palavras, key=len)
frase_ordenada = " ".join(palavras_ordenadas)

print("Frase com palavras ordenadas pelo tamanho:")
print(frase_ordenada)
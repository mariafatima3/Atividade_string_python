# 5) Escreva um programa que verifique se uma palavra é um palíndromo (lê-se igual de trás para frente). Exemplo: "radar".

palavra_1 = "radar"
palavra_2 = "Natan"
palavra_3 = "João"

print(palavra_1.lower() == palavra_1[::-1].lower())
print(palavra_2.lower() == palavra_2[::-1].lower())
print(palavra_3.lower() == palavra_3[::-1].lower())


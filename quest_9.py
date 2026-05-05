# 9) Escreva um programa que solicite ao usuário uma frase e substitua todas as vogais por asteriscos (*). 
# Em seguida, imprima a frase formatada.

frase = input("Digite uma frase: ")

vogais = "aeiouAEIOU"

for v in vogais:
    frase = frase.replace(v, "*")

print(f"Frase formatada: {frase}")
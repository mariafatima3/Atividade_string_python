# 8) Escreva um programa que solicite ao usuário dois números e imprima uma mensagem formatada mostrando a soma, subtração,
# multiplicação e divisão dos números. Por exemplo: "A soma de {num1} e {num2} é {soma}."

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2

print(f"A soma de {num1} e {num2} é {soma}.")
print(f"A subtração de {num1} e {num2} é {subtracao}.")
print(f"A multiplicação de {num1} e {num2} é {multiplicacao}.")

if num2 != 0:
    divisao = num1 / num2
    print(f"A divisão de {num1} e {num2} é {divisao}.")
else:
    print("Não é possível realizar divisão por zero.")

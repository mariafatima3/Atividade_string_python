# 31) Escreva um código que capitalize a primeira letra de cada palavra em uma frase. Exemplo: "python é incrível" deve se tornar "Python É Incrível".

frase = "python é incrível"
frase_capitalizada = " ".join(palavra.capitalize() for palavra in frase.split())

print(frase_capitalizada)  
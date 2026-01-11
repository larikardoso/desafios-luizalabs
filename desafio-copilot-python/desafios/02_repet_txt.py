#Solicitar uma string e um numero inteiro como entrada do usuário. Depois, repetir a string o número de vezes especificado pelo inteiro e exibir o resultado.

texto = input("Digite uma string: ")
numero = int(input("Digite um número inteiro: "))

#Adiciona espaços entre as repetições

resultado = (texto + " ") * numero
print("Resultado:", resultado)
#Vamos solicitar dois números inteiros ao usuário e realizar operações matemáticas básicas com eles.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

operacao = input("Digite a operação (+, -, *, /): ")
if operacao == "+":
    resultado = num1 + num2
    print(f"O resultado de {num1} + {num2} é: {resultado}")
elif operacao == "-":
    resultado = (abs(num1 - num2))
    print(f"O resultado de {num1} - {num2} é: {resultado}")
elif operacao == "*":
    resultado = num1 * num2
    print(f"O resultado de {num1} * {num2} é: {resultado}")
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"O resultado de {num1} / {num2} é: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida. Por favor, escolha entre +, -, * ou /.")
#Calcular a média de três notas fornecidas pelo usuário e informar se o aluno foi aprovado (média >= 7) ou reprovado (média < 7).

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3
print(f"A média das notas é: {media:.2f}")

if media >= 70:
    print("O aluno foi aprovado.")
else:
    print("O aluno foi reprovado.")
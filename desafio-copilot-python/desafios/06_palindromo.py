#Verifica se uma palavra ou frase é um palíndromo (lê-se da mesma forma de trás para frente).
palavra = input("Digite uma palavra ou frase: ")
palavra = palavra.replace(" ", "").lower()
if palavra == palavra[::-1]:
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")
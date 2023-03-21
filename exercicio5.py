string = input("Digite uma string: ")
caracteres = []

for caracter in string:
    caracteres.insert(0, caracter)

print(f"String invertida:  {''.join(caracteres)}")

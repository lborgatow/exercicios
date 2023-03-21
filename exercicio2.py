while True:
    try:
        numero = int(input("Digite um número: "))
        break
    except:
        print("Digite um número válido!\n")
        continue

a = 0
b = 1

while a < numero:
    a, b = b, a + b

if a == numero:
    print(f"O número {numero} pertence a sequência de Fibonacci!")
else:
    print(f"O número {numero} não pertence a sequência de Fibonacci!")

sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

total = sp + rj + mg + es + outros
print(total)
estados = {"SP": sp, 
           "RJ": rj, 
           "MG": mg, 
           "ES": es, 
           "OUTROS": outros}

print("O percentual de cada estado em relação ao total foi:\n")
for estado, valor in estados.items():
    print(f"{estado} = {round((valor / total) * 100, 2)}%")

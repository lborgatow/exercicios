import json


with open("dados.json") as file_object:
    dados = json.load(file_object)

dias_faturamento_0 = 0
for dado in dados:
    if dado['valor'] == 0:
        dias_faturamento_0 += 1

menor_faturamento = dados[0]
maior_faturamento = dados[0]
media_faturamento = sum([dado['valor'] for dado in dados]) / (len(dados) - dias_faturamento_0)
dias_superior_media = 0

for dado in dados:
    if dado['valor'] == 0:
        continue
    else:
        if dado['valor'] < menor_faturamento['valor']:
            menor_faturamento = dado
        
        if dado['valor'] > maior_faturamento['valor']:
            maior_faturamento = dado

        if dado['valor'] > media_faturamento:
            dias_superior_media += 1

print(f"Dia com menor faturamento: dia {menor_faturamento['dia']} --> R${round(menor_faturamento['valor'], 2)}")
print(f"Dia com maior faturamento: dia {maior_faturamento['dia']} --> R${round(maior_faturamento['valor'], 2)}")
print(f"Dias no mês em que o valor de faturamento diário foi superior à média mensal: {dias_superior_media} dias")

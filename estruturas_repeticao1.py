entrada_idade = ""
while entrada_idade != "0":
    entrada_idade = str(input("Digite um número qualquer ou 0 para sair: \n"))
    if entrada_idade == "0":
        continue
    else:
        print(f'Número digitado: {entrada_idade}')
print('Saiu do While')
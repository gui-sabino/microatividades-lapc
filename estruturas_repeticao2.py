texto = 'Olá, laço for'
for item in texto[0:]:
    # Condição para pular os espaços em branco
    if item == " ": 
        continue
    else: # Concatenando a string com o valor
        print('Caractere: ' + item)
print('Saiu do primeiro laço.')

for i in range(1, 11):
    print('Número do intervalo: ' + str(i))
print('Saiu do segundo laço.')
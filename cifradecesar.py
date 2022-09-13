import string
a = list(string.ascii_lowercase)
numero_codificacao = -1

while(numero_codificacao < 0 or numero_codificacao > 25):
    numero_codificacao = int(input('Insira quantas casas deseja deslocar as casas entre 0 e 25: '))

palavra_codificada = list(input('Insira a palavra a ser decifrada: '))
palavra_decodificada = ''

for i in range (len(palavra_codificada)):
    for j in range(26):
        if((palavra_codificada[i] == a[j]) and (j + numero_codificacao > 26)):
            palavra_decodificada += a[(j + numero_codificacao - 26)]
        elif((palavra_codificada[i] == a[j]) and (j + numero_codificacao <= 26)):
            palavra_decodificada += a[j+numero_codificacao]
        elif((palavra_codificada[i] == ' ')):
            palavra_decodificada += ''

print(palavra_decodificada)
#cria o alfabeto
import string
a = list(string.ascii_uppercase)
no_teste = int(input())

for x in range(no_teste):
    palavra_codificada = list(input())
    casas_codificacao = int(input())
    palavra_decodificada = ''
    for i in range (len(palavra_codificada)):
        for j in range(26):
            if((palavra_codificada[i] == a[j]) and (j - casas_codificacao < 0)):
                palavra_decodificada += a[26 - abs(j - casas_codificacao)]
            elif((palavra_codificada[i] == a[j]) and (j - casas_codificacao >= 0)):
                palavra_decodificada += a[j - casas_codificacao]
    print(palavra_decodificada)

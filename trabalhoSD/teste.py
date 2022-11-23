# operacoes = []
# mensagem = {'codOperacao' : 123, 'nome' : 'joao', 'idLoja' : '1', 'dataVenda' : '05/01/2022', 'valorVenda' : '750'}
# mensagem2 = {'codOperacao' : 123, 'nome' : 'pedro', 'idLoja' : '1', 'dataVenda' : '05/01/2022', 'valorVenda' : '1500'}
# mensagem3 = {'codOperacao' : 123, 'nome' : 'joao', 'idLoja' : '1', 'dataVenda' : '05/01/2022', 'valorVenda' : '750'}
# operacoes.append(mensagem)
# operacoes.append(mensagem2)
# operacoes.append(mensagem3)


# try:
#     vendas = {}
#     for operacao in operacoes:
#         vendas[operacao['nome']] = vendas.get(operacao['nome'], 0) + float(operacao['valorVenda'])
#     print(vendas)
#     print(max(vendas, key=vendas.get))

# except ValueError:
#     print("ERRO")

# testando ajuste url git

{
    'codOperacao': '1',
    'nome': 'Alberto',
    'idLoja': 'ALoja',
    'dataVenda': '10/11/2022',
    'valorVenda': '1000'
}
{
    'codOperacao': '1',
    'nome': 'Alberto',
    'idLoja': 'BLoja',
    'dataVenda': '22/03/2022',
    'valorVenda': '1500'
}
{
    'codOperacao': '1',
    'nome': 'Alberto',
    'idLoja': 'CLoja',
    'dataVenda': '30/12/2021',
    'valorVenda': '300'
}
{
    'codOperacao': '1',
    'nome': 'Marcelo',
    'idLoja': 'ALoja',
    'dataVenda': '13/05/2021',
    'valorVenda': '700'
}
{
    'codOperacao': '1',
    'nome': 'Marcelo',
    'idLoja': 'BLoja',
    'dataVenda': '07/12/2021',
    'valorVenda': '400'
}
{
    'codOperacao': '1',
    'nome': 'Marcelo',
    'idLoja': 'CLoja',
    'dataVenda': '21/02/2022',
    'valorVenda': '1000'
}
{
    'codOperacao': '1',
    'nome': 'Danilo',
    'idLoja': 'ALoja',
    'dataVenda': '09/08/2022',
    'valorVenda': '2000'
}
{
    'codOperacao': '1',
    'nome': 'Danilo',
    'idLoja': 'BLoja',
    'dataVenda': '14/11/2022',
    'valorVenda': '500'
}
{
    'codOperacao': '1',
    'nome': 'Danilo',
    'idLoja': 'CLoja',
    'dataVenda': '19/03/2022',
    'valorVenda': '300'
}

Melhor Loja esperado = "LojaA"
Melhor Vendedor esperado = "Alberto"
Total Vendas Alberto esperado = 2800.0
Total Vendas Marcelo esperado = 2100.0
Total Vendas Danilo esperado = 2700.0
Total Vendas ALoja esperado = 3700.0
Total Vendas ALoja esperado = 2400.0
Total Vendas ALoja esperado = 1600.0
Total de Vendas de uma rede de loja no periodo de 01/01/2021 ate 31/12/2021 esperado = 1400.0
Total de Vendas de uma rede de loja no periodo de 01/01/2022 ate 31/12/2022 esperado = 6300.0
Total de Vendas de uma rede de loja no periodo de 01/07/2022 ate 31/12/2022 esperado = 3500.0
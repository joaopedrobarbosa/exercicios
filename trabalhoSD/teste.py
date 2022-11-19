operacoes = []
mensagem = {'codOperacao' : 123, 'nome' : 'joao', 'idLoja' : '1', 'dataVenda' : '05/01/2022', 'valorVenda' : '750'}
mensagem2 = {'codOperacao' : 123, 'nome' : 'pedro', 'idLoja' : '1', 'dataVenda' : '05/01/2022', 'valorVenda' : '1500'}
mensagem3 = {'codOperacao' : 123, 'nome' : 'joao', 'idLoja' : '1', 'dataVenda' : '05/01/2022', 'valorVenda' : '750'}
operacoes.append(mensagem)
operacoes.append(mensagem2)
operacoes.append(mensagem3)


try:
    vendas = {}
    for operacao in operacoes:
        vendas[operacao['nome']] = vendas.get(operacao['nome'], 0) + float(operacao['valorVenda'])
    print(vendas)
    print(max(vendas, key=vendas.get))

except ValueError:
    print("ERRO")

#testando ajuste url git
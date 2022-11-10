# Aqui começa a conversa
tipoAcesso = input('''
    Escolha:
    1. Vendedor
    2. Gerente
    ''')

if(tipoAcesso == '1'):
    nome = input('Insira o nome do Vendedor: ')
    codOperacao = input('Insira o código da operação: ')
    idLoja = input('Insira a identificação da loja: ')
    dataVenda = input('insira a data da venda (dd/mm/yyyy): ')
    valorVenda = input('Insira o valor da venda: ')

    mensagem = {
        'tipoAcesso' : tipoAcesso,
        'nome' : nome,
        'codOperacao' : codOperacao,
        'idLoja' : idLoja,
        'dataVenda' : dataVenda,
        'valorVenda' : valorVenda 
    }
else:
    tipoConsulta = input('''
    Escolha:
    1. Total de vendas de um vendedor 
    2. Total de vendas de uma loja
    3. Total de vendas da rede de lojas em um período 
    4. Melhor vendedor
    5. Melhor loja 
    ''')

    if tipoConsulta == '1':
        consulta = input('Insira o nome do vendedor')
    elif tipoConsulta == '2':
        consulta = input('Insira o nome da loja')
    elif tipoConsulta == '3':
        consulta = input('Insira o periodo da vendas (dd/mm/yyyy até dd/mm/yyyy)')
    elif tipoConsulta == '4':
        consulta = 4
    elif tipoConsulta == '5':
        consulta = 5

    mensagem = {
        'tipoAcesso' : tipoAcesso,
        'tipoConsulta' : tipoConsulta,
        'consulta' : consulta
    }

print(str(mensagem))
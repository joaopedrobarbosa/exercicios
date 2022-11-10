# ------------------
# Cliente Socket UDP
# ------------------

print("Eu sou um CLIENTE UDP!")

# Importando a biblioteca
import socket

# Definindo ip e porta
HOST = '192.168.15.187'  # Endereco IP do Servidor
PORT = 9000              # Porta que o Servidor estará escutando

# Criando o socket
cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define o endereco do servidor (Ip e porta)
enderecoServidor = (HOST, PORT)

print("Vou começar a mandar mensagens para o servidor.")

while (True):
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

	# Enviando mensagem ao servidor
	print("... Mandando para o servidor")
	cliente.sendto(str(mensagem).encode("utf-8"), enderecoServidor)

	# Recebendo resposta do servidor
	msg, endereco = cliente.recvfrom(9000)
	resposta = msg.decode("utf-8")
	print("... O servidor me respondeu:", resposta)

print("... Encerrando o cliente")
cliente.close()
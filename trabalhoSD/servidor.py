# -------------------
# Servidor Socket UDP
# -------------------

import socket
import datetime

# APAGAR ESSA MENSAGEM DEPOIS DE PRONTO
# Preparar um retorno em string para resposta para o cliente
def totalVendasVendedor():
	pass

def totalVendasLoja():
	pass

def totalVendasPeriodo(operacoes, periodoEmString):
	valor = 0
	try:
		data1 = datetime.date(int(periodoEmString[6:10]), int(periodoEmString[3:5]), int(periodoEmString[0:2]))
		data2 = datetime.date(int(periodoEmString[21:25]), int(periodoEmString[18:20]), int(periodoEmString[15:17]))
	except ValueError:
		return "ERRO"
	if data1 > data2:
		data1, data2 = data2, data1
	for i in operacoes:
		dataNova = datetime.date(int(i.get("dataVenda")[6:10]), int(i.get("dataVenda")[3:5]), int(i.get("dataVenda")[0:2]))
		if dataNova >= data1 and dataNova <= data2:
			valor += float(i.get("valorVenda"))
	return str(valor)

def melhorVendedor():
	pass

def melhorLoja():
	pass



# APAGAR ESSE COMENTARIO AQUI DEPOIS
# Aqui como cada um tem um ip, vamos deixar nossos ips aqui
# fins de testes e praticidade na hora de entregar nós tiramos
# IP Rafael = 192.168.0.10

# definindo ip e porta
HOST = '192.168.0.10'    # Substituir pelo endereco IP do Servidor
PORT = 9000

# criando o socket e associando ao endereço e porta
servidor = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
servidor.bind((HOST,PORT))

# servidor escutando (aguardando cliente)
print("Servidor aguardando clientes...")

operacoes = []
# conversando com o cliente
while (True):
	# recebendo dados uma tupla com mensagem e endereço
	msg, enderecoCliente = servidor.recvfrom(9000)
	print("Mensagem do cliente " + str(enderecoCliente))
	# transformando mensagem em dict
	mensagem = eval(msg.decode("utf-8"))
	print(mensagem)

	# Se for mensagem de Vendedor
	if mensagem.get("codOperacao") == "1":
		operacoes.append(mensagem)
		resposta = "OK"
	# Se for mensagem de Gerente
	elif mensagem.get("codOperacao") == "2":
		# APAGAR ESSE COMENTARIO DEPOIS QUE TODO MUNDO JÁ TIVER FEITO
		# Aqui entrarão os métodos para processamento de pedidos do gerente
		if (mensagem.get("tipoConsulta") == "1"):
			resposta = totalVendasVendedor()
		elif (mensagem.get("tipoConsulta") == "2"):
			resposta = totalVendasLoja()
		elif (mensagem.get("tipoConsulta") == "3"):
			resposta = totalVendasPeriodo(operacoes, mensagem.get("consulta"))
		elif (mensagem.get("tipoConsulta") == "4"):
			resposta = melhorVendedor()
		elif (mensagem.get("tipoConsulta") == "5"):
			resposta = melhorLoja()
		else:
			resposta = "ERRO"
	else:
		resposta = "ERRO"
	servidor.sendto(resposta.encode("utf-8"), enderecoCliente)
	
# mensagem de encerramento
print("Servidor encerrado.")
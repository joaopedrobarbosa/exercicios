# -------------------
# Servidor Socket TCP
# -------------------

# importando a biblioteca
import socket

# definindo ip e porta
HOST = '127.0.0.1'       # Substituir pelo endereco IP do Servidor
PORT = 9000              # Porta que o Servidor ficará escutando

# criando o socket e associando ao endereço e porta
servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
servidor.bind((HOST,PORT))

# servidor escutando (aguardando cliente)
servidor.listen()

# cliente conectou - recuperando informações do cliente
conexaoCliente, enderecoCliente = servidor.accept()
lista=()
# conversando com o cliente
while (True):
	# recebendo dados
	dados = conexaoCliente.recv(1024)
	# respondendo ao cliente
	mensagem = eval(dados.decode("utf-8"))

	if (mensagem.get("tipoAcesso") == "1"):
		lista.add(mensagem)
	else:
		print('irei complementar o codigo aqui')

	#codigo com erro, terminar implementaçao variavel resposta
	# conexaoCliente.sendall(resposta.encode("utf-8"))
	conexaoCliente.sendall(mensagem.encode("utf-8"))

# mensagem de encerramento
print("Servidor encerrado.")
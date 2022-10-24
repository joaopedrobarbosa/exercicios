# -------------------
# Servidor Socket TCP
# -------------------

# importando a biblioteca
import socket

print("Eu sou o SERVIDOR TCP!")

# definindo ip e porta
HOST = '127.0.0.1'       # Substituir pelo endereco IP do Servidor
PORT = 9000              # Porta que o Servidor ficará escutando

# criando o socket e associando ao endereço e porta
servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
servidor.bind((HOST,PORT))

# servidor escutando (aguardando cliente)
servidor.listen()
print("Aguardando cliente...")

# cliente conectou - recuperando informações do cliente
conexaoCliente, enderecoCliente = servidor.accept()
print(f"Cliente {enderecoCliente} conectou.")

login = {'joao':'gerente', 'rafael':'vendedor'}

# conversando com o cliente
while (True):
	# recebendo dados
	dados = conexaoCliente.recv(1024)
	# testando dados enviados
	if (not dados):
		# encerrando conexão e saindo do loop
		print ("Encerrando a conexão...")
		conexaoCliente.close()
		break
	# respondendo ao cliente
	mensagem = str(dados.decode("utf-8"))
	print("-----")
	print(f"Mensagem enviada pelo cliente: {mensagem}")
	print(f"Este servidor vai devolver a mensagem ao cliente {enderecoCliente}")
	resposta = "Resposta do servidor: " + mensagem
	conexaoCliente.sendall(resposta.encode("utf-8"))

# mensagem de encerramento
print("Servidor encerrado.")
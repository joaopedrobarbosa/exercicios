# ------------------
# Cliente Socket TCP
# ------------------

print("Eu sou um CLIENTE TCP!")

# importando a biblioteca
import socket

# definindo ip e porta
HOST = '127.0.0.1'       # Substituir pelo endereco IP do Servidor
PORT = 9000              # Porta que o Servidor ficará escutando

# criando o socket
cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# cliente se conectando ao servidor
cliente.connect((HOST,PORT))

print("Vou começar a mandar mensagens para o servidor.")

# Aqui começa a conversa
print("Entrando com mensagem de texto para enviar")
print("(Para sair digite 'fim')")
mensagem = input("Digite seu login > ")



while (mensagem != "fim"):
	# Enviando mensagem ao servidor
	print("... Vou manda uma mensagem para o servidor")
	cliente.sendall(mensagem.encode("utf-8"))

	# Recebendo resposta do servidor
	resposta = cliente.recv(1024)

	# exibindo resposta
	print("... >>> O servidor me respondeu:", resposta.decode("utf-8"))

	# Obtendo nova mensagem do usuário
	print("... Entrando com nova mensagem de texto para enviar")
	mensagem = input("Mensagem > ")

print("Encerrando o cliente")
cliente.close()
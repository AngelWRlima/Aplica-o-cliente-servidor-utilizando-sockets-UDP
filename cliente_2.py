from socket import *

HOST = 'localhost'
PORT = 11304
udp = socket(AF_INET, SOCK_DGRAM)

while True:
    print ('para sair, escreva "sair"')
    msg = input()
    if msg == 'sair': break
    udp.sendto (msg.encode(), (HOST, PORT))
    data, endereco = udp.recvfrom(2048)
    reply = data.decode()
    print (f'Resposta recebida: {reply}')

udp.close()
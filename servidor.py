from socket import *
from threading import Thread

def HandleRequest(ClientSocket, ClientAddr):
    while True:
        data = ClientSocket
        print (f'Mensagem recebida de: {ClientAddr}')
        req = data.decode()
        print (f'Mensagem: {req}')
        volta = 'Mensagem recebida com sucesso!'
        udp.sendto(volta.encode(), ClientAddr)
        break
#class myThread (threading.Thread):
#    def __init__(self, message, Address):
#        threading.Thread.__init__(self)
#        self.message = message
#        self.serverAddress = Address
#    def run(self):
#        print("Starting " + self.name)
#        print(self)
#        messaging(self.message, self.serverAddress)

#def messaging(message, clientAddress):
#    print(message.decode())
#    modifiedMessage = message.decode().upper()
#    udp.sendto(modifiedMessage.encode(), clientAddress)

#endereço de envio e recebimento

PORT = 11304

udp = socket(AF_INET, SOCK_DGRAM)
udp.bind(('', PORT))

print ('Aguardado conexão com o cliente...')
while True:
    msg, cliente = udp.recvfrom(2048)
    Thread(target=HandleRequest, args=(msg, cliente)).start()

#    print ("Recebi =", msg.decode(), "do cliente," ,cliente)
#    print (f'conectado em {cliente}')
#    print (f'{cliente}, {msg.decode()}')

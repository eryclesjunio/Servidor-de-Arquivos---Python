#serv_sock.py

import socket
import threading
import pickle

class TrataCliente:
  @classmethod
  def run(cls):
    while True:
      ans = pickle.loads(conn.recv(1024))
      if(ans[0] == 'POST'):
        cls.writer(ans[1])
        
      if(ans[0] == 'GET'):
        cls.reader(ans[1])
      
  @classmethod    
  def writer(cls, local): 
    print("Armazenando arquivo")
    arq = open(local, 'wb')
    dados = conn.recv(1024)
    #if not dados:
     # break
    arq.write(dados)
    #msg = pickle.dumps("deu certo")
    #conn.send(msg)
    #arq.close()
    #conn.close()
    
  @classmethod
  def reader(cls, local):
    print("Enviando arquivo")
    arq = open(local, 'rb')
    for i in arq.readlines():
        conn.send(i)


HOST = ''
PORT = 57000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

while True:
  conn, addr = s.accept() #Aguardando clientes
  print (addr)
  t = threading.Thread(target=TrataCliente.run,args=[])
  t.start()



  '''
  #TrataCliente
  if(ans[0] == 'POST'):
    t = threading.Thread(target=writer,args=[ans[1]])
    t.start()
  if(ans[0] == 'GET'):
    t = threading.Thread(target=reader,args=[ans[1]])
    t.start()
  '''


#client_sock.py
import socket
import pickle
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
import os

def load_file():

    fname = askopenfilename(filetypes=(("Template files", "*.tplate"),
                                           ("HTML files", "*.html;*.htm"),
                                           ("All files", "*.*") ))
    return fname



if __name__ == "__main__":

    
    HOST = 'localhost' #coloca o host do servidor
    PORT = 57000

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    s.connect((HOST,PORT))
    ans = input('GET ou POST')
    
    while ans != "Fim":
        path = input('Digite o diretorio: ')
        
        if ans == 'POST':
            caminho = load_file()
            #caminho = os.listdir('files/')
            print(caminho)
            '''
            for x in caminho:
                print (x)
            '''    
            arq = open(caminho, 'rb')

            for i in arq.readlines():
                dic = pickle.dumps((ans, path))
                s.send(dic)
                s.send(i)
                
        if ans == 'GET':
            #while True:
            dic = pickle.dumps((ans, path))
            s.send(dic)
            print(s.recv(1024))
                
        ans = input('GET ou POST')
        
    arq.close()
    s.close()



'''
root = Tkinter.Tk()
root.withdraw()
dirname = tkFileDialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
'''



import socket
sockvar= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockvar.connect(('data.pr4e.org', 80))
cmd= 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
sockvar.send(cmd)

while True:
    data= sockvar.recv(512)
    if (len(data)<1):
        break
    print(data.decode())
sockvar.close()

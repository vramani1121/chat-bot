import socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 5090))
server_socket.listen(10)
print("[+] listeinng for connection on 127.0.0.1 : 5090..")

while True:
    conn , addr = server_socket.accept()
    print("[+] got a connection from  {}".format(addr))
    while True:

        data = conn.recv(1024)
        if (data ==''): break
        print("[+] client sent :" , data.decode())
        conn.send(b'this is server.')


    conn.close()
    print("[+] client disconnected ")

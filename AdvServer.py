import socket, select
ID=1

#function to broadcast chat message to all connected clients
def broadcast_data (socket, message):
    #dont send message to master and client who sent
    for socket  in CONNECTION_LIST:
        if socket != server_socket and socket != sock:
            try :
                socket.send(message.encode('utf-8'))
            except :
                #broken socket connection
                socket.close()
                CONNECTION_LIST.remove(socket)
if __name__ == "__main__":
    #list to keep track of sockets
    CONNECTION_LIST = []
    RECV_BUFFER = 4096
    PORT = 5000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("0.0.0.0", PORT))
    server_socket.setblocking(0)
    server_socket.listen(10)

    #add server socket to the list of readable connections
    CONNECTION_LIST.append(server_socket)
    print ("Chat server started on port " + str(PORT))

    while 1:
        #get the list of sockets which are ready to be read through select
        read_sockets.write_sockets,error_sockets = select.select(CONNECTION_LIST, [], [])
        for sock in read_sockets:
            if sock == server_socket:
                #handle the case in which there is new connection
                sockfd, addr = server_socket.accept()

                CONNECTION_LIST.append(sockfd)
                print ("Clinet (%s, %s) is online" %addr)
                print (ID)
                turn= str(ID)
                ID = ID +1
                sockfd.send(turn.encode('utf-8'))
            #   broadcast_data(sockfd, "the other play is turn " + turn)
            else:
                try:
                    data = sock.recv(RECV_BUFFER).decode('utf-8')

                    if data:
                        broadcast_data(sock, data)

                except:
                    broadcast_data(sock, "client (%s, %s) is offline" % addr)
                    print ("Client (%s, %s) is offline" % addr)
                    ID = ID - 1
                    sock.close()
                    CONNECTION_LIST.remove(sock)
                    continue

    server_socket.close()

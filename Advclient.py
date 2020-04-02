import socket
def Main():
    turn = None
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host, port))
    go = s.recv(1024).decode('utf-8')
    print(go)
    if go in ["1"]:
        turn = True
        them = "2"
    elif go in ["2"]:
        turn = False
        them = "1"

    print ("you are connected to the server, and you are player" + go)

    while True:
        if turn == Turn:
            message = input("\n Please Enter a Message -> ")
            if message in ["quit", "Q","q"]:
                s.close()
                break
            s.send(message.encode('utf-8'))
            turn = False
        elif turn == False:
            print("\n Waiting for the other player \n ")
            data = s.recv(1024).decode('utf-8')
            print (" person " + them + " says ----> " + data)
            turn = True
if __name__ == "__main__":
    Main()
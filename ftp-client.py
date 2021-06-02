import socket

HOST = 'localhost'
PORT = 9090
while True:
    sock = socket.socket()
    sock.connect((HOST, PORT))

    request = input('Введите команду: ')

    sock.send(request.encode())

    if request == "exit":
        break

    response = sock.recv(8192).decode()


    if not response:
        print("No data was received")
    else:
        print(response)

    sock.close()
import socket
import os
import glob


def process(req):
    if req == 'pwd':
        return os.getcwd()
    elif req == 'ls':
        files = []
        for filename in glob.iglob('**', recursive=True):
            files = files + [filename]
        return '; '.join(files)
    else:
        reqs = req.split(" ")
        if len(reqs) != 2:
            if len(reqs) < 2:
                return 'bad request'
            elif reqs[0] == 'rename':
                os.rename(reqs[1].replace('..', ''), reqs[2].replace('..', ''))
                return 'Изменения файла успешно сохранены'
            else:
                return 'bad request'
        elif reqs[0] == 'mkdir':
            os.mkdir(reqs[1].replace('..', ''))
            return 'Директория создана'
        elif reqs[0] == 'rmdir':
            os.rmdir(reqs[1].replace('..', ''))
            return 'Директория удалена'
        elif reqs[0] == 'rmfile':
            os.remove(reqs[1].replace('..' , ''))
            return 'Файл удален'
        elif reqs[0] == 'cut':
            ref = req.split(" ")[1].replace('..', '')
            myfile = open(ref, "r")
            data = myfile.read()
            myfile.close()

            datasize = len(data)
            request = str(datasize) + " " + data
            return request
        else:
            return 'bad request'


PORT = 9090

os.chdir("DATA")

while True:
    print("Новый сокет")
    sock = socket.socket()
    sock.bind(('' , PORT))
    sock.listen()

    while True:
        print('Порт' , PORT)
        conn , addr = sock.accept()
        print(addr)
        request = conn.recv(8192).decode()
        print(request)

        if request == "exit":
            break

        response = process(request)
        conn.send(response.encode())

    sock.close()
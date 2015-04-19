import socket
import parallel_processing


def main():
    server = ''
    port = 6699
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #sock = socket.socket()
    #try:
    sock.bind((server, port))
    #except socket.error as e:
        #print (str(e))

    sock.listen(10)
    c, addr = sock.accept()
    print "recive data" + str(addr)
    while True:
        data = c.recv(1024)
        if not data:
            break
        card1, card2 = str(data).split(' ')
        p_data = parallel_processing.main(card1,card2)
    sock.close()



if __name__ == '__main__':
    main()
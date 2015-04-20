import socket
import parallel_processing


def main():
    host = '127.0.0.1'
    port = 6699
    #sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock = socket.socket()
    try:
        sock.connect((host, port))
    except socket.error as e:
        print (str(e))
    s_data = raw_input("=>")
    while s_data != "q":
        sock.send(s_data)
        print "sending data to server"
        data_rec = sock.recv(1024)
        print "data recived :  " + str(data_rec)
    sock.close()



if __name__ == '__main__':
    main()
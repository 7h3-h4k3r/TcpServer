import socket
class Tcpconn:
    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.sock = None
        self.sockc = None
    def _sockinit(self):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
    def _sockclient(self):
        self.sockc = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
    def server_sock_setup(self):
        if(self.sock==None):
            try:
                self._sockinit()
                self.sock.bind((self.host,self.port))
                self.sock.listen()
                print("[*] server host {}\t[*] server port {}\ntcp_socket_server Version:v0.1 \tctrl + c to stop the server".format(self.host,self.port))
                self.__connecntion_server()
            except Exception as e:
                print(" Error : [server socket failed] & {}".format(e))
        else:
            print("Error : socket init failed")
    def __connecntion_server(self):
        while True:
            try:
                conn , address = self.sock.accept()
                conn.send("tcp_server version:v0.1\n".encode())
                self.server_console(address,conn)
            except Exception as e:
                print("Error : {}".format(e))
                pass
    def server_console(self,add,conn):
        while True:
            try:
                data = conn.recv(1024).decode().strip()
                if not data : break
                print("client => Internet_protocol [{}] , _port [{}] Message_ [{}]".format(add[0],add[1],data))
            except KeyboardInterrupt:
                print("server shutdown")
                conn.close()
                exit()
    def client_connect(self):
        try:
            if(self.sockc==None):
                self._sockclient()
            self.sockc.connect((self.host,self.port))
            print("client side successfully connected to the Sever")
            self.client_msg()
        except Exception as e:
            print(f"Error : {e}")
    def client_msg(self):
        print(self.sockc.recv(1024).decode().strip())
        while True:
            data = input(">>")
            if(data == "quit"):
                print("Cliend successfully disconnected")
                self.sockc.close()
                break
            self.sockc.send(data.encode())
            


        


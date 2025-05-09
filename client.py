from Server.__init__ import Tcpconn

client = Tcpconn("127.0.0.1",7444).client_connect()
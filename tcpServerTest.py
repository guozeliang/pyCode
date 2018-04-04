import errno
import socket

def connection_ready(sock,fd,events):
    while True:
        try:
            connection,address = sock.accept()
        except socket.error as e:
            if e.args[0] not in (errno.EWOULDBLOCK,errno.EAGAIN):
                raise
            return
        connection.setblocking(0)
        handle_connection(connection,address)

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sock.setblocking(0)
sock.bind('',9000)



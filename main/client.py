from re import X
import select, socket, sys, banner, pickle
from util import Room, Hall, User
import util
from banner import Ascii_Banner as ab

READ_BUFFER = 4096

if len(sys.argv) < 2:
    print("Usage: Python3 client.py [hostname]", file = sys.stderr)
    sys.exit(1)
else:
    server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_connection.connect((sys.argv[1], util.PORT))
    # print(f'System Argv: {sys.argv}\n')

def prompt():
    print('>', end=' ', flush = True)


print("Connected to server\n") #prints to client terminal.
msg_prefix = ''

socket_list = [sys.stdin, server_connection]

while True:
    read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])
    # print(f'Read_sockets: {read_sockets}\n') 
    # print(f'Write_sockets: {write_sockets}\n')
    # print(f'Error_sockets: {error_sockets}\n')
    for s in read_sockets:
        if s is server_connection: # incoming message from client(s)
            msg = s.recv(READ_BUFFER)
            if not msg:
                print("Server down!")
                sys.exit(2)
            else:
                if msg == util.QUIT_STRING.encode():
                    sys.stdout.write('Bye\n')
                    sys.exit(2)
                else:
                    sys.stdout.write(msg.decode())
                    if 'Please tell us your name' in msg.decode():
                        msg_prefix = 'name: ' # identifier for name
                    else:
                        # new_func("Welcome")
                        msg_prefix = ' '
                    prompt()
                    # new_func("Welcome")
                    

        else:
            msg = msg_prefix + sys.stdin.readline()
            server_connection.sendall(msg.encode())

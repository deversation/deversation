from re import X
<<<<<<< HEAD
import select, socket, sys
from subprocess import run
# from assistant import run_assistant
# banner, pickle
# from main.util import Room, Hall, User
=======
import select, socket, sys, pickle
>>>>>>> dev
import util
from banner import Ascii_Banner

READ_BUFFER = 4096

if len(sys.argv) < 2:
    print("Usage: Python3 client.py [hostname]", file = sys.stderr)
    sys.exit(1)
else:
    server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_connection.connect((sys.argv[1], util.PORT))
<<<<<<< HEAD
    # run_assistant()
    # print(f'System Argv: {sys.argv}\n')
=======
>>>>>>> dev

def prompt():
    
    print('>', end=' ', flush = True)
    # run_assistant()

print("\n🟢 Connected to the server\n")
msg_prefix = ''

socket_list = [sys.stdin, server_connection]

while True:
    read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])

    for s in read_sockets:
        if s is server_connection:
            msg = s.recv(READ_BUFFER)
            if not msg:
                print("Server down!")
                sys.exit(2)
            else:
                if msg == util.QUIT_STRING.encode():
                    bye = Ascii_Banner.colored_banner('Bye!\n', 'red')
                    sys.stdout.write(bye.decode())
                    sys.exit(2)
                else:
                    sys.stdout.write(msg.decode())
                    if 'Please enter a user name:' in msg.decode():
<<<<<<< HEAD
                        msg_prefix = 'name: ' # identifier for name
                        # run_assistant()
=======
                        msg_prefix = 'name: '
>>>>>>> dev
                    else:
                        msg_prefix = ' '
                        # run_assistant()
                    prompt()
<<<<<<< HEAD
                    # run_assistant()
                    # new_func("Welcome")
=======
>>>>>>> dev
                    
        else:
            msg = msg_prefix + sys.stdin.readline()
            server_connection.sendall(msg.encode())
            # run_assistant()

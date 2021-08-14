from os import set_blocking
import select, socket, sys, pdb
from util import Hall, Room, User
import util

READ_BUFFER = 4096

host = sys.argv[1] if len(sys.argv) >= 2 else ''
listen_sock = util.create_socket((host, util.PORT))
# print(f'Host: {host}\n')
# print('List Sock: {listen_sock}\n')

hall = Hall()


connection_list = []
connection_list.append(listen_sock)
# print(f'Hall: {hall}\n')
# print(f'Connection_list: {connection_list}\n')
# print(f'Listen_sock: {listen_sock}\n')


while True:
    # Player.fileno()
    read_players, write_players, error_sockets = select.select(connection_list, [], [])
    # print(f'Read_Players: {read_players}\n') 
    # print(f'Write_players: {write_players}\n')
    # print(f'Error_sockets: {error_sockets}\n')
    
    for user in read_players:
        if user is listen_sock: # new connection, users is a socket
            new_socket, add = user.accept()
            new_user = User(new_socket)
            connection_list.append(new_user)
            hall.welcome_new(new_user)
             
            
            # new_room.append(new_user)
            # new_room('room_name:', 'Dev Talk')
            # new_room()
            # print(f'Connection List: {connection_list}\n')

        else: # new message
            msg = user.socket.recv(READ_BUFFER)
            # print(f'New message: {msg}\n') #prints to server terminal
            if msg:
                msg = msg.decode().lower()
                hall.handle_msg(user, msg)
            else:
                user.socket.close()
                connection_list.remove(user)

    for sock in error_sockets: # close error sockets
        sock.close()
        connection_list.remove(sock)

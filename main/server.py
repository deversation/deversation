import select, socket, sys, pdb
import util
from util import Hall, Room, User 

READ_BUFFER = 4096

host = sys.argv[1] if len(sys.argv) >= 2 else ''
listen_sock = util.create_socket((host, util.PORT))

hall = Hall()
connection_list = []
connection_list.append(listen_sock)

while True: 
    # Player.fileno()
    read_users, write_users, error_sockets = select.select(connection_list, [], [])
    for user in read_users:
        if user is listen_sock: # new connection, user is a socket
            new_socket, add = user.accept()
            new_user = User(new_socket)
            connection_list.append(new_user)
            hall.welcome_new(new_user)

        else: # new message
            msg = user.socket.recv(READ_BUFFER)
            if msg:
                msg = msg.decode().lower()
                hall.handle_msg(user, msg)
            else:
                user.socket.close()
                connection_list.remove(user)

    for sock in error_sockets: # close error sockets
        sock.close()
        connection_list.remove(sock)



# import select, socket, sys, pdb
# from util import Hall, Room, Player
# import util

# READ_BUFFER = 4096

# host = sys.argv[1] if len(sys.argv) >= 2 else ''
# listen_sock = util.create_socket((host, util.PORT))

# hall = Hall()
# connection_list = []
# connection_list.append(listen_sock)

# while True:
#     # Player.fileno()
#     read_players, write_players, error_sockets = select.select(connection_list, [], [])
#     for player in read_players:
#         if player is listen_sock: # new connection, player is a socket
#             new_socket, add = player.accept()
#             new_player = Player(new_socket)
#             connection_list.append(new_player)
#             hall.welcome_new(new_player)

#         else: # new message
#             msg = player.socket.recv(READ_BUFFER)
#             if msg:
#                 msg = msg.decode().lower()
#                 hall.handle_msg(player, msg)
#             else:
#                 player.socket.close()
#                 connection_list.remove(player)

#     for sock in error_sockets: # close error sockets
#         sock.close()
#         connection_list.remove(sock)

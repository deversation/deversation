import socket, pdb
from pyfiglet import Figlet
from termcolor import colored, cprint 
from banner import Ascii_Banner, Text

MAX_CLIENTS = 30
PORT = 22222
QUIT_STRING = '<$quit$>'



def create_socket(address):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setblocking(0)
    s.bind(address)
    s.listen(MAX_CLIENTS)
    print("Now listening at ", address) #prints to server terminal
    return s


class Hall:
    def __init__(self):
        self.rooms = {} # {room_name: Room}
        self.room_user_map = {} # {playerName: roomName}

    # welcomes new users and prints string(s) in sendall()
    def welcome_new(self, new_user):
        new_user.socket.sendall(b'This chat space was created to encourage learning, communication, and collaboration between developers.\n\nPlease tell us your name:\n')
        # new_user.socket.sendall()
        
    def create_default_room(self, room_name): # create room instances when first users signs on
        
         pass
    
    
    def list_rooms(self, user):
        
        if len(self.rooms) == 0:
            msg = 'Oops, no active rooms currently. Create your own!\n' \
                + 'Use [/join room_name] to create a room.\n'
            user.socket.sendall(msg.encode())
        else:
            msg = 'Listing current rooms...\n'
            for room in self.rooms:
                msg += room + ": " + str(len(self.rooms[room].users)) + " user(s)\n"
            user.socket.sendall(msg.encode())
        
            
    # def list_users(self, user):
    #     users = self.room_user_map
    #     msg = str(users.keys())
    #     msg = bytes(msg, encoding='utf-8')
        
    #     # for msg in self.room_user_map.items():
    #     #         msg = str(self.room_user_map, '\n')
    #     user.socket.sendall(msg.encode())
            
        # msg = self.room_user_map
        # if len(self.room_user_map) == 1:
        #     msg = 'You are the only user in this room :('
        #     user.socket.sendall(msg.encode())
        # else:
        #     print('Listing current users...')
        #     print(f'Room Usre Map: {self.room_user_map}')
        # for x in self.room_user_map:
        #     msg = str(f'Users: {x}\n Room: {x[1]}\n')
        #     msg = str(len(self.msg))
        #     # msg = 'Active Users \n'
            
        #     x + ": " + self.room_user_map[x]
            
            # print(self.rooms.users)
        # user.socket.sendall(x.encode())
        
        
    
    def handle_msg(self, user, msg):
        
        
        def green_banner(msg):
            f = Figlet(font='standard')
            x = colored(f.renderText(msg), 'green')
            x = bytes(x, encoding='utf-8')
            return x
        
            # user.socket.sendall(msg)
            # print(b"hello!")
            
        def instructions(user):
            # create a function to loop and print instructions to users instead of code below?
            pass
        
        # instructions variable that gets printed when needed via sendall(instructions)
        # the b before the string converts the string to bytes, which is what is need when sending data via sockets. 
        instructions = b'Instructions:\n'\
            + b'[/join python] to enter python chat\n'\
            + b'[/join challenges] to enter code challenge chat\n'\
            + b'[/join quiz] to enter quiz chat\n'\
            + b'[/join general] to enter general chat\n'\
            + b'[/join room_name] to join/create/switch to a room\n' \
            + b'[/list] to list all active rooms\n'\
            + b'[/manual] to show instructions\n' \
            + b'[/quit] to quit\n' \
            + b'Please choose a command.' \
            + b'\n'
             
       
        print(user.name + " says: " + msg) #users message that only gets printed to server terminal
        
        #checks for "name:" in msg. This happens when the welcome_new() function gets called for new users.
        if "name:" in msg:
            user.socket.sendall(green_banner('Welcome!\n To\n Deversation\n')) #welcome message to new users
        
            name = msg.split()[1]
            user.name = name
            print("New connection from:", user.name) #prints to server terminal
            user.socket.sendall(instructions) #print instuctions to client terminal


        #checks for "/join" in message
        elif "/join" in msg:
            
            # Checking if user is already in the room when swtiching
            # Creates a new room instance 
            same_room = False
            
            if len(msg.split()) >= 2: # checking if the len of msg is >= 2. split() separates based on white space & creates list of strings/words. 
                
                #room_name = msg.split()[1] #grabbing the string at index 1 and assigning to room_name
                room_name = msg.split()[1:] #splitting after the first index. This removes the /join command
                room_name = '-'.join(room_name).upper() # joins and adds '-' between our new room name if more than 1 word for room_name. 'dev talk' equals 'DEV-TALK' 
                print(f'Room Name: {room_name}') # prints to server terminal
                
                # Switches, creates and checks is users is already in current room.
                if user.name in self.room_user_map: # checks 
                    if self.room_user_map[user.name] == room_name: 
                        user.socket.sendall(b'You are already in room: ' + room_name.encode())
                        same_room = True
                    else: # switches
                        old_room = self.room_user_map[user.name]
                        self.rooms[old_room].remove_player(user)
                if not same_room:
                    if not room_name in self.rooms: # new room:
                        new_room = Room(room_name)
                        self.rooms[room_name] = new_room
                    self.rooms[room_name].users.append(user)
                    self.rooms[room_name].welcome_new(user)
                    self.room_user_map[user.name] = room_name
            else:
                user.socket.sendall(instructions) # prints instructions to client terminal


        elif "python" in msg:
        #     same_room = False
        #     # room_name = msg[2::]
        #     # room_name = room_name.upper() 
            # room_name = 'PYTHON'
            # print(f'Room Name: {room_name}') # prints to server terminal
        #     # link = cprint(b'https://www.python.org/', 'blue')
            # py_room = b"welcome to python\n"
            # user.socket.sendall(py_room)
            
            x = Ascii_Banner.green_banner('python')
            user.socket.sendall(x)
            z = Text.blue_text('https://www.python.org/\n')
            user.socket.sendall(z)
        #     new_room = Room(room_name)
        #     self.rooms[room_name] = new_room
        #     self.rooms[room_name].users.append(user)
        #     self.rooms[room_name].welcome_new(user)
        #     self.room_user_map[user.name] = room_name

        elif "/list" in msg:
            self.list_rooms(user) #calls list room function
            
            
        # elif "/users" in msg:
        #     self.list_users(user) #calls list_users function
                

        elif "/manual" in msg:
            user.socket.sendall(instructions) #prints instructions to client terminal

        
        elif "/quit" in msg:
            user.socket.sendall(QUIT_STRING.encode()) # removes user from server/application
            self.remove_player(user)

        else:
            # check if user is already in a room
            if user.name in self.room_user_map:
                self.rooms[self.room_user_map[user.name]].broadcast(user, msg.encode())
            else:
                msg = 'You are currently not in any room! \n' \
                    + 'Use [<list>] to see available rooms! \n' \
                    + 'Use [<join> room_name] to join a room! \n'
                user.socket.sendall(msg.encode())
    
    def remove_player(self, player): # removes user when they /quit. Prints to server terminal.
        if player.name in self.room_user_map:
            self.rooms[self.room_user_map[player.name]].remove_player(player)
            del self.room_user_map[player.name]
        print("User: " + player.name + " has left\n")
        
        
class Room:
    def __init__(self, room):
        self.users = [] # a list of sockets
        self.room = room

    def welcome_new(self, from_user): # welcomes new users to rooms. Prints to users terminal.
        msg = self.room + " welcomes: " + from_user.name + '\n'
        for user in self.users:
            user.socket.sendall(msg.encode())
    
    def broadcast(self, from_user, msg): # sends out messages from users in chat rooms
        msg = from_user.name.encode() + b":" + msg
        for user in self.users:
            user.socket.sendall(msg)

    def remove_player(self, user): # removes user from room. Calls broadcast() and passes args.
        self.users.remove(user)
        leave_msg = user.name.encode() + b" has left the room\n"
        self.broadcast(user, leave_msg)

class User:
    def __init__(self, socket, name = "new"):
        socket.setblocking(0)
        self.socket = socket
        self.name = name

    def fileno(self):
        return self.socket.fileno()


# class MultiChatServer():
    
#     def __init__(self, maxClients, serverPort):
#         self._maxClients = maxClients
#         self._clients = []
        
#         self.ROOM1 = Room('1', self)
#         self.ROOM2 = Room('2', self)
#         self.ROOM3 = Room('3', self)
#         self.ROOM4 = Room('4', self)
        
#         self._serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self._serverPort = serverPort
    
#     def print_room_clients(self):
#         for r in [self.ROOM1, self.ROOM2, self.ROOM3, self.ROOM4]:
#             print (r.get_name(), r._occupants)
    
        

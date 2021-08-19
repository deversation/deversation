import socket
from challenge import random_questions
from ascii_art import bio 
try:
# test code:
    from main.banner import Ascii_Banner, Text 
except:
# production code:
    from banner import Ascii_Banner, Text 

MAX_CLIENTS = 30
PORT = 22222
QUIT_STRING = '<$quit$>'

def create_socket(address):
    '''
    Create socket, passed in to server utilizing a tuple of host IP address and port number.
    '''

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setblocking(0)
    s.bind(address)
    s.listen(MAX_CLIENTS)
    print("Now listening at ", address) 
    return s

class Hall:
    '''
    Hall class instantiated in server. Holds functionality for client entrance, exit, and navigation
    '''

    def __init__(self):
        self.rooms = {}
        self.room_user_map = {}

    def welcome_new(self, new_user):
            '''
            Greet the user upon client startup
            '''

            intro = Text.colored_text('The Deversation chat space was created to encourage learning, communication, and collaboration between developers!\n\nPlease enter a user name:\n', 'cyan')
            new_user.socket.sendall(intro)

    def list_rooms(self, user):
        if len(self.rooms) == 0:
            msg = '\n❗There are currently no active rooms. Try creating or joining a room:\n\n' \
                + 'Type [/join room_name] to create or join a room.\n'
            user.socket.sendall(msg.encode())
        else:
            msg = '\nListing current rooms...\n'
            for room in self.rooms:
                msg += room + ": " + str(len(self.rooms[room].users)) + " user(s)\n"
            user.socket.sendall(msg.encode())
        
    def python_room(self, user):
        x = Ascii_Banner.colored_banner('PYTHON CHAT', 'green')
        user.socket.sendall(x)
        desc = Text.colored_text('🐍\n\nThis is the room for all things python.\nNew to the language? We\'ve gathered some links to get you started:\n', 'green')
        user.socket.sendall(desc)
        z = Text.colored_text('\nhttps://www.sololearn.com/learning/1073\n' + 'https://careerkarma.com/blog/python-projects-beginners/\n' + 'https://www.python.org/\n\n', 'blue')
        user.socket.sendall(z)

    def general_room(self, user):
        x = Ascii_Banner.colored_banner('GENERAL CHAT', 'yellow')
        user.socket.sendall(x)
        desc = Text.colored_text('🍕\n\nTired of all the code speak? Try some human speak instead.\n\n', 'yellow')
        user.socket.sendall(desc)

    def challenge_room(self, user):
        x = Ascii_Banner.colored_banner('CHALLENGE ACCEPTED!', 'red')
        user.socket.sendall(x)
        z = Text.colored_text('https://miro.com/\n' + 'https://replit.com/\n\n', 'blue')
        user.socket.sendall(z)
        random_questions(user)
    
    def handle_msg(self, user, msg):
        '''
        Listens for keywords entered by user and execute the respective functionality.
        '''       

        instructions = b'\nInstructions:\n'\
            + b'[/join python] to enter python chat\n'\
            + b'[/join challenge] to test your knowledge\n'\
            + b'[/join general] to enter general chat\n'\
            + b'[/join room_name] to join/create/switch to a room\n' \
            + b'[/list] to list all active rooms\n'\
            + b'[/help] to show instructions\n' \
            + b'[/quit] to quit\n' \
            + b'\nPlease enter a command without the brackets:' \
            + b'\n\n'
        
        if "name:" in msg:
            x = Ascii_Banner.colored_banner('Welcome!\n To\n Deversation\n', 'green')
            user.socket.sendall(x)
            name = msg.split()[1]
            user.name = name
            print("New connection from:", user.name) 
            user.socket.sendall(instructions)
        elif "/join" in msg:
            same_room = False
            if len(msg.split()) >= 2: 
                room_name = msg.split()[1:]
                room_name = '-'.join(room_name).upper() 
                if user.name in self.room_user_map: 
                    if self.room_user_map[user.name] == room_name: 
                        user.socket.sendall(b'You are already in room: ' + room_name.encode())
                        same_room = True
                    else:
                        old_room = self.room_user_map[user.name]
                        self.rooms[old_room].remove_user(user)
                if not same_room:
                    if "python" in msg:
                        self.python_room(user)
                    elif "general" in msg:
                        self.general_room(user)
                    elif "challenge" in msg:
                        self.challenge_room(user)
                    else:
                        x = Ascii_Banner.colored_banner(room_name, 'cyan')
                        user.socket.sendall(x)
                    if not room_name in self.rooms:
                        new_room = Room(room_name)
                        self.rooms[room_name] = new_room
                    self.rooms[room_name].users.append(user)
                    self.rooms[room_name].welcome_new(user)
                    self.room_user_map[user.name] = room_name
            else:
                user.socket.sendall(instructions)
       
        elif "/list" in msg:
            self.list_rooms(user)

        elif "/help" in msg:
            user.socket.sendall(instructions)
        
        elif '/bio' in msg:
            bio(user)

        elif "/quit" in msg:
            user.socket.sendall(QUIT_STRING.encode())
            self.remove_user(user)

        else:
            if user.name in self.room_user_map:
                self.rooms[self.room_user_map[user.name]].broadcast(user, msg.encode())    
            else:
                z = Text.colored_text('\n❗You are currently not in any room!\n', 'white')
                user.socket.sendall(z)
                msg = '\nTry a command:\n' \
                    + 'Type [/list] to see available rooms \n' \
                    + 'Type [/join room_name] to join a room\n'
                user.socket.sendall(msg.encode())

    def remove_user(self, user):
        if user.name in self.room_user_map:
            self.rooms[self.room_user_map[user.name]].remove_user(user)
            del self.room_user_map[user.name]
        print("User: " + user.name + " has left\n")
        
class Room:
    def __init__(self, room):
        self.users = []
        self.room = room

    def welcome_new(self, from_user):
        msg = Text.colored_text(from_user.name + " has entered: " + self.room + '!\n', 'green')
        for user in self.users:
            user.socket.sendall(msg)
    
    def broadcast(self, from_user, msg):
        msg = from_user.name.encode() + b":" + msg
        for user in self.users:
            user.socket.sendall(msg)

    def remove_user(self, user):
        self.users.remove(user)
        leave_msg = Text.colored_text(' has left the room\n', 'red')
        self.broadcast(user, leave_msg)

class User:
    '''
    User class instantiated in server. Open new socket per user.
    '''

    def __init__(self, socket, name = "new"):
        # setblocking comment out for testing
        socket.setblocking(0)
        self.socket = socket
        self.name = name

    def fileno(self):
        return self.socket.fileno()

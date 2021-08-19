import pytest
# import main.client
import socket
# from main.client import prompt
# import main.server
from main.util import Hall, Room, User, create_socket
from main.banner import Ascii_Banner, Text

# Possible test cases forthe util.py module

def test_can_successfully_create_to_a_hall():
   hall = Hall()
   assert hall

def test_can_successfully_print_a_message_banner():
    msg = "hello"
    banner = Ascii_Banner(msg)
    assert banner

def test_green_banner():
    msg = 'hello'
    banner= Ascii_Banner.green_banner(msg)
    assert banner

def test_red_banner():
    msg = 'hello'
    banner= Ascii_Banner.red_banner(msg)
    assert banner

def test_yellow_banner():
    msg = 'hello'
    banner= Ascii_Banner.yellow_banner(msg)
    assert banner

def test_cyan_banner():
    msg = 'hello'
    banner= Ascii_Banner.cyan_banner(msg)
    assert banner

def test_can_successfully_print_text():
    msg = "In a good progress"
    text = Text(msg)
    assert text

def test_green_text():
    msg = 'hello'
    text = Text.green_text(msg)
    assert text

def test_white_text():
    msg = 'hello'
    text = Text.white_text(msg)
    assert text

def test_red_text():
    msg = 'hello'
    text = Text.red_text(msg)
    assert text

def test_yellow_text():
    msg = 'hello'
    text = Text.yellow_text(msg)
    assert text

def test_blue_text():
    msg = 'hello'
    text = Text.blue_text(msg)
    assert text

def test_cyan_text():
    msg = 'hello'
    text = Text.cyan_text(msg)
    assert text

def test_can_successfully_connected_to_a_chat_room_server():
   name = "test room"
   room = Room(name)
   assert room.room == "test room"

def test_create_socket():
    address = ('127.0.0.1', 22222)
    s = create_socket(address)
    assert s
    
def test_create_user():
    user = 'new'
    name = User(user)
    assert name.name == 'new'

# def test_fileno():
    # inst = User.fileno(self)
    # file = 4
    # assert inst == file

def test_welcome_new(fix_user):
    out = Hall.welcome_new(fix_user)
    # out, err = capsys.readouterr()
    assert out == 'message'
    # assert err == ''

# def test_prompt():
#     prompt = main.client.prompt()
#     assert prompt =='>'

def test_list_rooms():
    pass

# def test_python_room():
    
#     inst = Hall.python_room(user)
    
# def test_can_successfully_print_welcome_to_chat_room_messge():
#     new_hall = Hall()
#     new_user = b'user'
#     assert new_hall.welcome_new(new_user) == b'message'
    # pass

    # actual = new_hall.welcome_new(new_user)
    # assert actual == b'The Deversation chat space was created to encourage learning, communication, and collaboration between developers!\n\nPlease enter a user name:\n'

# def test_can_successfully_list_default_rooms():
#     new_hall = Hall()
#     new_user = 'user'
#     assert  new_hall.list_rooms(new_user)

# def test_handle_msg():
#     socket = 
#     user = 'new' 
#     msg = 'name:'
#     socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     hall = Hall.handle_msg(user, msg)
#     user.socket.sendall(instructions) 

# def test_fileno():
#     fileno = User.fileno()
#     assert fileno



# @pytest.fixture
# def serve():
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(('0.0.0.0', 8080))
# s.listen(5)
# @pytest.fixture
# def new_user():
#     new_user = User()

# class Test_Hall():
#         def test_welcome_new(self, fix_user, capsys):
#             fix_user.welcome_new('me')
#             out, err = capsys.readouterr()
#             assert out == 'This'
#             assert err == ''

# @pytest.fixture
# def fix_user():
#     user = 'new'
#     name = User(user)
#     return name

# @pytest.fixture
# def fix_user():
#     user = User()
#     user.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     user.name = 'new'
#     return user




import pytest
import socket
# import main.client
# from main.client import prompt
# import main.server
from main.util import Hall, Room, User, create_socket
from main.banner import Ascii_Banner, Text

def test_can_successfully_create_to_a_hall():
   hall = Hall()
   assert hall

def test_Ascii_Banner():
    msg = 'msg'
    banner = Ascii_Banner(msg)
    assert banner

def test_colored_banner():
    msg = 'hello'
    banner= Ascii_Banner.colored_banner(msg, 'red')
    assert banner

def test_can_successfully_print_text():
    msg = "In a good progress"
    text = Text(msg)
    assert text

def test_colored_text():
    msg = 'hello'
    text = Text.colored_text(msg, 'blue')
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

# def test_welcome_new(fix_user):
#     user = fix_user
#     out = Hall()
#     assert out.welcome_new(user) == "Error"

# @pytest.fixture
# def fix_user():
#     user = 'new'
#     name = User(user)
#     return name



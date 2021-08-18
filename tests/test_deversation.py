import pytest
# import main.client
import socket
from main.util import Hall, Room, User
from main.banner import Ascii_Banner, Text

def test_hall():
    hall = Hall()
    assert hall


def test_banner():
    msg = 'hello'
    banner = Ascii_Banner(msg)
    assert banner


# Possible test cases forthe util.py module

def test_can_successfully_create_to_a_hall():
   hall = Hall()
   assert hall

def test_can_successfully_print_a_message_banner():
    msg = "hello"
    banner = Ascii_Banner(msg)
    assert banner

def test_can_successfully_print_text():
    msg = "In a good progress"
    text = Text(msg)
    assert text

def test_can_successfully_connected_to_a_chat_room_server():
   name = "test room"
   room = Room(name)
   assert room.room == "test room"

def test_can_successfully_print_chat_room_instructions():
    pass
    
def test_can_successfully_print_welcome_to_chat_room_messge():
    new_hall = Hall()
    new_user = b'user'
    assert new_hall.welcome_new(new_user) == b'message'
    # pass

    # actual = new_hall.welcome_new(new_user)
    # assert actual == b'The Deversation chat space was created to encourage learning, communication, and collaboration between developers!\n\nPlease enter a user name:\n'

# def test_can_successfully_list_default_rooms():
#     new_hall = Hall()
#     new_user = 'user'
#     assert  new_hall.list_rooms(new_user)

def test_can_successfully_create_a_new_room():
    pass

def test_user_can_successfully_create_a_new_user():
    # user = "new"
    # name = User(user)
    # assert name.name == "new"
    pass

def test_user_can_successfully_join_a_chat_room():
    pass

def test_multiple_user_can_successfully_join_a_chat_room():
    pass

def test_messages_can_successfully_displayed_for_all_users_in_a_chat_room():
    pass

def test_user_can_successfully_left_a_chat_room():
    pass


# Possible test cases forthe server.py module

def test_server_is_successfully_listening_at_specific_port():
    pass

# Possible test cases forthe client.py module

def test_can_successfully_prompt_a_user_to_enter_user_name():
    pass

def test_user_can_successfully_enter_a_user_name():
    pass

def test_can_successfully_concatenate_and_display_welcome_message_with_a_user_name():
    pass

def test_can_successfully_print_a_goodbye_massage_when_user_quits():
    pass

def test_can_successfully_print_an_error_massage_when_server_is_down():
    pass


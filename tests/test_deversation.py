import pytest
from main.banner import Ascii_Banner, Text 
from main.util import Hall

def test_hall():
    hall = Hall()
    assert hall

def test_banner():
    msg = 'hello'
    banner = Ascii_Banner(msg)
    assert banner

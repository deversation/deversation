from termcolor import colored
from pyfiglet import Figlet

class Ascii_Banner:
    '''
    Create a colored banner by passing in the message and color parameters
    '''

    def __init__(self, msg):
        self.msg = msg
     
    def colored_banner(msg, color):
        f = Figlet(font='standard')
        x = colored(f.renderText(msg), color)
        x = bytes(x, encoding='utf-8')
        return x

class Text():
    '''
    Create a colored text by passing in the message and color parameters
    '''
    
    def __init__(self, msg):
        self.msg = msg
        
    def colored_text(msg, color):
        x = colored(msg, color)
        x = bytes(x, encoding='utf-8')
        return x

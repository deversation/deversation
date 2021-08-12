# import pyfiglet
from termcolor import colored
from pyfiglet import Figlet

class Ascii_Banner:
    def __init__(self, msg):
        self.msg = msg
        
    def green_banner(self):
        f = Figlet(font='standard')
        print(colored(f.renderText(self.msg), 'green'))
        
    def red_banner(self):
        f = Figlet(font='standard')
        print(colored(f.renderText(self.msg), 'red'))
    
    def yellow_banner(self):
        f = Figlet(font='standard')
        print(colored(f.renderText(self.msg), 'red'))
        
class Text():
    def __init__(self, msg):
        self.msg = msg
        
    def green_text(self):
        pass
    
    def red_text(self):
        pass
    
    def yellow_text(self):
        pass
    
    def blue_text(self):
        pass
        
    
# x = Ascii_Banner("Hello World!")
# y = Ascii_Banner("Welcome!")
# bye = Ascii_Banner("Bye!")
# bye.ascii_banner()
# x.ascii_banner()
# y.ascii_banner()
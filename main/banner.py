from termcolor import colored
from pyfiglet import Figlet

class Ascii_Banner:
    def __init__(self, msg):
        self.msg = msg
        # self.name = name
        
    # def green_banner(self):
    #     f = Figlet(font='standard')
    #     print(type(colored(f.renderText(self.msg), 'green')))
    #     # print(colored(f.renderText(self.name), 'green'))
     
    def green_banner(msg):
        f = Figlet(font='standard')
        x = colored(f.renderText(msg), 'green')
        x = bytes(x, encoding='utf-8')
        return x
    
    def banner(self):
        f = Figlet(font='standard')
        print(f)
        
    def red_banner(self):
        f = Figlet(font='standard')
        print(colored(f.renderText(self.msg), 'red'))
    
    def yellow_banner(self):
        f = Figlet(font='standard')
        print(colored(f.renderText(self.msg), 'yellow'))
        
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
    
    
# print(type(Ascii_Banner("hi")))
# x = Ascii_Banner("Hello World!")
# y = Ascii_Banner("Welcome!")
# bye = Ascii_Banner("Bye!")
# bye.green_banner()
# x.red_banner()
# x.banner()

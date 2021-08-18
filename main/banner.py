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

    def red_banner(msg):
        f = Figlet(font='standard')
        x = colored(f.renderText(msg), 'red')
        x = bytes(x, encoding='utf-8')
        return x
    
    def yellow_banner(msg):
        f = Figlet(font='standard')
        x = colored(f.renderText(msg), 'yellow')
        x = bytes(x, encoding='utf-8')
        return x

    def cyan_banner(msg):
        f = Figlet(font='standard')
        x = colored(f.renderText(msg), 'cyan')
        x = bytes(x, encoding='utf-8')
        return x

# refactor?
    # def color_banner(msg, color):
    #     f = Figlet(font='standard')
    #     x = colored(f.renderText(msg), color)
    #     x = bytes(x, encoding='utf-8')
    #     return x

class Text():
    def __init__(self, msg):
        self.msg = msg
        
    def green_text(msg):
        x = colored(msg, 'green')
        x = bytes(x, encoding='utf-8')
        return x

    def white_text(msg):
        x = colored(msg, 'white')
        x = bytes(x, encoding='utf-8')
        return x

    def red_text(msg):
        x = colored(msg, 'red')
        x = bytes(x, encoding='utf-8')
        return x
    
    def yellow_text(msg):
        x = colored(msg, 'yellow')
        x = bytes(x, encoding='utf-8')
        return x
    
    def blue_text(msg):
        x = colored(msg, 'blue')
        x = bytes(x, encoding='utf-8')
        return x
    
    def cyan_text(msg):
        x = colored(msg, 'cyan')
        x = bytes(x, encoding='utf-8')
        return x
    
    
# print(type(Ascii_Banner("hi")))
# x = Ascii_Banner("Hello World!")
# y = Ascii_Banner("Welcome!")
# bye = Ascii_Banner("Bye!")
# bye.green_banner()
# x.red_banner()
# x.banner()

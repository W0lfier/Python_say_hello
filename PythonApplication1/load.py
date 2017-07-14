"""向用户问候的简单程序"""

import mod.say_hello_module

if __name__ == '__main__':
    USER = mod.say_hello_module.User()
    USER2 = mod.say_hello_module.User('jack.json')
    USER.say_hello()
    USER2.say_hello()

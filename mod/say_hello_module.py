"""实现用户存档的类"""

from json import dump, load
import os

class User():
    """对用户存档的操作"""
    def __init__(self, file_name='default.json'):
        """初始化创建名字为file_name.json的json空文件"""
        self.file_name = file_name
        if os.path.exists(self.file_name):
            pass
        else:
            with open(self.file_name, 'w') as file_object:
                dump('', file_object)

    def check_exist(self):
        """检查文档与用户存档是否存在"""
        try:
            with open(self.file_name, 'r') as file_object:
                username = load(file_object)
        except FileNotFoundError:
            return False
        if username:
            return True
        return False

    def who(self):
        """输出存档名称"""
        if self.check_exist():
            with open(self.file_name, 'r') as file_object:
                user_name = load(file_object)
            return user_name
        return None

    def add_user(self, user_name):
        """创建用户存档"""
        if self.check_exist():
            print('Here is already existing an user.')
            return False
        with open(self.file_name, 'w') as file_object:
            dump(user_name, file_object)
        print('Welcome ' + user_name + ', I will remember you.')
        return True

    def del_user(self):
        """删除用户存档"""
        if self.check_exist():
            with open(self.file_name, 'w') as file_object:
                dump('', file_object)
            return True
        print("Here is nobody.")
        return False

    def say_hello(self):
        """向用户问候，用户不存在则创建并存档"""
        if self.check_exist():
            with open(self.file_name, 'r') as file_object:
                user_name = load(file_object)
            print('hello, ' + user_name)
        else:
            user_name = input('You are the first time to visit here, input your name')
            self.add_user(user_name)

"""say_hello_module.py的测试用例"""

from json import load, dump
import unittest
import os

from mod.say_hello_module import User

class TestUser(unittest.TestCase):
    """测试User类"""
    def setUp(self):
        """实例化User类"""
        self.user = User('test.json')
   
    def test_add_user(self):
        """测试添加用户存档功能"""
        with open('test.json','w') as file_object:
            dump('',file_object)
        self.assertTrue(self.user.add_user('test'))
        with open('test.json','r') as file_object:
            user_name = load(file_object)
        self.assertEqual('test',user_name)
        self.assertFalse(self.user.add_user('test2'))

    def test_del_user(self):
        """测试删除用户存档功能""" 
        with open('test.json','w') as file_object:
            dump('',file_object)
        self.assertFalse(self.user.del_user())
        self.user.add_user('test')
        self.assertTrue(self.user.del_user())
        
    def test_who(self):
        """测试读取用户存档功能"""
        with open('test.json','w') as file_object:
            dump('',file_object)
        self.assertEqual(None,self.user.who())
        self.user.add_user('test')
        self.assertEqual('test',self.user.who())

if __name__ == '__main__':
    unittest.main()
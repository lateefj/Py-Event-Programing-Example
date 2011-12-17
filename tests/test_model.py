
import unittest
import os

from zrouter import ZVent
import events
from model import set_storage_path, User
set_storage_path('/tmp/test')

class TestUser(unittest.TestCase):

    id = 12324
    name = 'foo'

    def set_up(self):
        u = User()
        path = u.path(self.id)
        os.remove(path)
    
    setUp = set_up # PEP-8


    def test_new_user(self):

        e = ZVent(ztype=events.NEW_USER, data={'id':TestUser.id, 
            'name':TestUser.name})
        ZVent.publish(e)
        u = User()
        u.load(TestUser.id)
        assert u.id == TestUser.id, 'expect id to be %s but it was %s' % (
                TestUser.id, u.id)
        assert u.name == TestUser.name

    def test_change_name(self):
        self.test_new_user()
        new_name = 'bar'
        e = ZVent(ztype=events.CHANGE_USER_NAME, data={'id':TestUser.id, 
            'new_name':new_name})
        ZVent.publish(e)
        u = User()
        u.load(TestUser.id)
        assert u.name == new_name

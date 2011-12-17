
import unittest
import os

from zrouter import ZVent
import events
from model import set_storage_path
set_storage_path('/tmp/test')
from model import User, Message

class TestUser(unittest.TestCase):

    id = 12324
    name = 'foo'

    def set_up(self):
        u = User()
        path = u.path(self.id)
        try:
            os.remove(path)
        except Exception, e:
            pass
    
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


class TestMessage(unittest.TestCase):

    id = 43252
    text = 'foo'
    user_id = TestUser.id

    def set_up(self):
        u = Message()
        path = u.path(self.id)
        try:
            os.remove(path)
        except Exception, e:
            pass
    
    
    setUp = set_up # PEP-8

    def test_new(self):

        e = ZVent(ztype=events.MESG_NEW, data={'id':TestMessage.id, 
            'text':TestMessage.text, 'user':TestMessage.user_id})
        ZVent.publish(e)
        m = Message()
        m.load(TestMessage.id)
        assert m.id == TestMessage.id, 'expect id to be %s but it was %s' % (
                TestMessage.id, u.id)
        assert m.text == TestMessage.text

    def test_update(self):
        self.test_new()
        new_text = 'foo the bar out of here'
        e = ZVent(ztype=events.MESG_NEW, data={'id':TestMessage.id, 
            'text':new_text, 'user':TestMessage.user_id})
        ZVent.publish(e)
        m = Message()
        m.load(TestMessage.id)
        assert m.id == TestMessage.id, 'expect id to be %s but it was %s' % (
                TestMessage.id, u.id)
        assert m.text == new_text

    def test_delete(self):
        self.test_new()
        e = ZVent(ztype=events.MESG_DELETE, data={'id':TestMessage.id,
            'user':TestMessage.user_id})
        ZVent.publish(e)
        m = Message()
        m.load(TestMessage.id)
        assert m.deleted == True

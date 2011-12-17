import unittest

from zrouter import ZVent

class TestZVent(unittest.TestCase):

    def set_up(self): 
        """
        Make sure there is nothing in the even system before running tests.
        """
        ZVent.clear()
    
    setUp = set_up # WTF PEP8 anyone!! (Ok pet peeve)

    def test_register(self):
        def t(e):
            pass
        k = 'test:1'
        ZVent.register(k, t)
        assert ZVent.MAP.has_key(k)
        assert len(ZVent.MAP[k]) == 1
        assert ZVent.MAP[k][0] == t

    def test_publish(self):
        def t(e):
            data['foo'] = 'bar'

        data = {'foo':'foo'}
        k = 'test:2'
        ZVent.register(k, t)
        ze = ZVent(ztype=k, data=data)
        ZVent.publish(ze)
        assert data['foo'] == 'bar'

"""
Example of a very simple event dispatch system. The change in names is mainly
to reduce confusion with concepts and implementation. This is a very simple
implementation for demonstration purposes.
"""

import logging


class ZVent(object):
    """
    It would be easy to subclass this to add some kind of session, filter or
    other feature that would help
    """
    
    MAP = {}
    def __init__(self, ztype=None, data=None):
        self.ztype = ztype
        self.data = data
        
    @classmethod
    def register(clzz, ztype, callback):
        if not ZVent.MAP.has_key(ztype):
            ZVent.MAP[ztype] = []
            
        ZVent.MAP[ztype].append(callback)
    @classmethod 
    def publish(clzz, zvent):
        if ZVent.MAP.has_key(zvent.ztype):
            for callback in ZVent.MAP[zvent.ztype]:
                callback(zvent)

    @classmethod
    def clear(clzz):
        ZVent.MAP.clear()

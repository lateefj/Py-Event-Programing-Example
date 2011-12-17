"""
Example of a very simple event dispatch system. The change in names is mainly
to reduce confusion with concepts and implementation. This is a very simple
implementation for demonstration purposes.
"""

import logging
from json import dumps

log = logging.getLogger(name=__name__)
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
        log.debug('Registering: %s' % ztype)
        if not ZVent.MAP.has_key(ztype):
            ZVent.MAP[ztype] = []
            
        ZVent.MAP[ztype].append(callback)
    @classmethod 
    def publish(clzz, zvent):
        log.debug('Publish for type %s' % zvent.ztype)
        if ZVent.MAP.has_key(zvent.ztype):
            for callback in ZVent.MAP[zvent.ztype]:
                callback(zvent)

    @classmethod
    def clear(clzz):
        ZVent.MAP.clear()

    def jsonify(self):
        d = {'ztype':self.ztype, 'data':self.data}
        return dumps(d)

import os

from uuid import uuid4
from json import dumps, loads


from zrouter import ZVent
import events

STORAGE_PATH = None

def gen_id():
    return uuid4().int

def set_storage_path(path):
    global STORAGE_PATH
    if not os.path.exists(path):
        os.mkdir(path)
    STORAGE_PATH = path

class User:
    namespace = 'user' # Base directory could be bucket or table name

    
    def __init__(self):
        self.store_path = '%s/%s' % (STORAGE_PATH, User.namespace)
        if not os.path.exists(self.store_path):
            os.mkdir(self.store_path)

        """The actual model state variables"""
        self.id = None
        self.deleted = None
        self.name = None
        self.last_online = None
        self.profile = {}
    
    ################# Using file system for simplicity #############
    def path(self, id):
        path = '%s/%s.json' % (self.store_path, id)
        return path
    def get_events(self, id):
        path = self.path(id)
        l = []
        if os.path.exists(path):
            re = loads(open(path).read())
            for e in re:
                
                e = loads(e) # String to dict conversion
                # Create a proper event object from the dictionary
                l.append(ZVent(ztype=e['ztype'], data=e['data']))
        return l

    def apply(self, e):
        """
        The magic here is the mapping we do at the end to associate an
        event with a method on the object. We could have a big stack
        of 'if' statments but this is much cleaner.
        """
        if User.apply_map.has_key(e.ztype):
            User.apply_map[e.ztype](self, e)

    def save(self, e): 
        """
        Way to save the event besides convertin to JSON this is nothing. Using
        a JSON document store like Mongo or Riak would rock here.
        """
        id = e.data['id']
        l = self.get_events(id)
        l.append(e.jsonify())
        f = open(self.path(id), 'w')
        f.write(dumps(l))

    def load(self, id):
        """
        Get the event and just reapply them all!
        """
        l = self.get_events(id)
        for e in l:
            self.apply(e)

    def new_user(self, e):
        """
        Simple to set the current state of new user since all we have
        is the id and the name.
        """
        self.id = e.data['id']
        self.name = e.data['name']

    def change_name(self, e):
        pass
    def change_profile(self, e):
        pass
    def delete_profile_field(self, e):
        pass
    def delete_user(self, e):
        pass
    def user_online(self, e):
        pass

    apply_map = {
            events.NEW_USER:new_user,
            events.CHANGE_USER_NAME:change_name,
            events.UPATE_USER_PROFILE: change_profile,
            events.DELETE_PROFILE_FIELD: delete_profile_field,
            events.DELETE_USER: delete_user,
            events.USER_ONLINE: user_online
            }

def handle_user_event(e):
    """
    The user event handlers are implemented on the class so 
    we don't really need much to see here. Basically we need to 
    do 3 steps:
        * First load the User object so that it is the current state
        * Save the event to the datastore
        * Apply it to update the current state
    """
    u = User()
    u.load(e.data['id'])
    u.save(e)
    u.apply(e)

# Maps the all events that the User class is handling
for k in User.apply_map.keys():
    ZVent.register(k, handle_user_event)


    


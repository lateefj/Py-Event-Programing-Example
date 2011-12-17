"""
This is a list of events with convinent constants every
event will have the event_type and a timestamp so in the example
dictionaries is just the data of the event.
"""


################### USER EVENTS #########################
NEW_USER = 'user:1'
"""New user creation {id:123, name:'foo'}"""

CHANGE_USER_NAME = 'user:2'
"""Change the user name {id:123, new_name:'bar'}"""

UPATE_USER_PROFILE = 'user:3'
"""Set an abitrary number of fields {id:123, display_name:'Teef', badger:'hottness'}"""

DELETE_PROFILE_FIELD = 'user:4'
"""Remove a field from the users profile {id:123, field_name:'badger'}"""

DELETE_USER = 'user:5'
"""Remove a user from the system {id:123}"""

USER_ONLINE = 'user:6'
"""Marker that the user was online at some point {id:123, timestamp:234234}"""

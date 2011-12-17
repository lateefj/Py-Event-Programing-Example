"""
This is a list of events with convinent constants every
event will have the event_type and a timestamp so in the example
dictionaries is just the data of the event.
"""


################### USER EVENTS #########################
NEW_USER = 'user:1'
"""New user creation {name:'foo'}"""

CHANGE_USER_NAME = 'user:2'
"""Change the user name {old_name:'foo', new_name:'bar'}"""

UPATE_USER_PROFILE = 'user:3'
"""Set an abitrary number of fields {display_name:'Teef', badger:'hottness'}"""

DELETE_PROFILE_FIELD = 'user:4'
"""Remove a field from the users profile {field_name:'badger'}"""

DELETE_USER = 'user:5'
"""Remove a user from the system {name:'bar'}"""




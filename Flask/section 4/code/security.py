from werkzeug.security import safe_str_cmp #Python comparison on all versions
from user import User

# users = [
#     {
#         "ID":1,
#         "username":'Aditya Vyas',
#         'password':'asdf'
#     }
# ]

# username_mapping = {
#     'bob': {
#         "ID":1,
#         "username":'Aditya Vyas',
#         'password':'asdf'
#     }
# }

# userid_mapping = {
#     1: {
#         "id":1,
#         "username":'Aditya Vyas',
#         'password':'asdf'
#     }
# }

users = [User(1,'Aditya','asdf')]

username_mapping = {u.username: u for u in users}


userid_mapping = {u.id: u for u in users}


def authenticate(username,password):
    user = username_mapping.get(username,None)
    if user and safe_str_cmp(user.password,password):
        return user

def identity(payload):
     user_id = payload['identity']
     return userid_mapping.get(user_id,None)



from client import Client
from client_friends import ClientFriends

user = Client()
user_friends = ClientFriends(user.execute())
user_friends.print_friends()

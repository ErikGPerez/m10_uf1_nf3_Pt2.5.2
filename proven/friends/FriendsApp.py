from proven.friends.model.FriendModel import FriendModel
from proven.friends.controllers.FriendController import FriendController

class FriendsApp:
    
    def friendMain(self):
            model = FriendModel()
            control = FriendController(model)
            
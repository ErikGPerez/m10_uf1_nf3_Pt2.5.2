from model.FriendModel import FriendModel
from controllers.FriendController import FriendController

class FriendsApp:
    
    def friendMain(self):
            model = FriendModel()
            control = FriendController(model)
            
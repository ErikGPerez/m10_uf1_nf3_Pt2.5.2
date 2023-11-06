from proven.friends.controllers.FriendController import FriendController
from proven.friends.model.FriendModel import *
from proven.friends.model.Friend import *
import FriendMenu

class FriendView:
    def __init__(self, control: FriendController, model: FriendModel):
        self.control = control
        self.model = model
        self.menu = FriendMenu
from proven.friends.controllers.FriendController import FriendController
from proven.friends.model.FriendModel import *
from proven.friends.model.Friend import *
import FriendMenu

class FriendView:
    def __init__(self, control: FriendController, model: FriendModel):
        self.control = control
        self.model = model
        self.menu = FriendMenu()
    
    def showInputDialog(self, message):
        print(message)
        return input()
    
    def showMessage(self, message):
        print(message)
        
    def display(self):
        while True:
            self.menu.show()
            
    def processAction(self, action):
        if action != None:
            if action:
                self.control.processRequest(action)
    
    def showFriendTable(self, data):
        cont = 0
        for Friend in data:
            print(Friend)
            cont = cont + 1
        print(cont + "Elements found. " + data.len())
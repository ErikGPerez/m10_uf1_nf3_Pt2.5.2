from proven.friends.model.FriendModel import FriendModel
from proven.friends.views.FriendView import FriendView
from proven.friends.model.Friend import Friend

class FriendController:
    
    def __init__(self, model: FriendModel):
        self.model = model
        self.view = FriendView(self, self.model)
        self.view.display()
        
    def processRequest(self, action):

        if action == None:
            action = "wrong_action"
        else:
            if action == "exit":
                self.exitApplication()
            if action == "list_all_friends":
                self.listAllFriends()
            if action == "search_friend_by_phone":
                self.searchFriendByPhone()
            if action == "search_friend_by_name":
                self.searchFriendsByName()
            if action == "friend_form_add":
                self.addFriend()
            if action == "friend_form_modify":
                self.modifyFriendForm()
            if action == "friend_form_remove":
                self.removeFriendForm()
            if action == "wrong_action":
                print("Wrong option")
        
    def exitApplication(self):
        quit()
    
    def listAllFriends(self):
        data = self.model.findAll()
        if data != None:
            self.view.showFriendTable(data)
        else:
            self.view.showMessage("Error retrieving data")
                
    def searchFriendByPhone(self):
        phone = self.view.showInputDialog("Input phone: ")
        if phone != None:
            friend = Friend(phone)
            found = self.model.find(friend)
            if found != None:
                self.view.friendForm(found)
            else:
                self.view.showMessage("Friend not found")
        else:
            self.view.showMessage("Error in parameter phone")
        
    def searchFriendsByName(self):
        name = self.view.showInputDialog("Input name: ")
        if name != None:
            data = self.model.findFriendsByName(name)
            if data != None:
                self.view.showFriendTable(data)
            else:
                self.view.showMesssage("Error searching Friends")
        else:
            self.view.showMessage("Error in parameter name")
        
    def addFriend(self):
        friend = self.view.friendForm(None)
        if friend != None:
            result = self.model.add(friend)
            if result > 0:
                self.view.showMessage("Friend succesfully added")
            else:
                self.view.showMessage("Friend has not been added")
        else:
            self.view.showMessage("Error in parameters")
        
    def modifyFriend(self, oldVersion, newVersion):
        result = self.model.modify(oldVersion, newVersion)
        if (result > 0):
            self.view.showMessage("Friend succesfully modified")
        else:
            self.view.showMessage("Friend has not been modified")
    
    def removeFriend(self, friend):
        result = self.model.remove(friend)
        if result > 0:
            self.view.showMessage("Friend succesfully removed")
        else:
            self.view.showMessage("Friend has not been removed")
            
    def modifyFriendForm(self):
        phone = self.view.showInputDialog("Input old friend phone: ")
        if phone != None:
            friend = Friend(phone)
            found = self.model.find(friend)
            if found != None:
                self.view.friendForm(found)
                newFriend = self.view.friendForm(None)
                if newFriend == None:
                    self.view.showMessage("Friend not modified")
                else: 
                    self.modifyFriend(friend, newFriend)
            else:
                self.view.showMessage("Friend not found")
    
    def removeFriendForm(self):
        phone = self.view.showInputDialog("Input phone: ")
        if phone != None:
            friend = Friend(phone)
            found = self.model.find(friend)
            if found != None:
                self.removeFriend(friend)
            else:
                self.view.showMessage("Friend not found")

from model.FriendModel import FriendModel
from views.FriendView import FriendView
from model.Friend import Friend

class FriendController:
    
    def __init__(self, model: FriendModel):
        self.model = model
        self.view = FriendView(model)
        self.view.display()
        
        
    def processRequest(self, action):

        if action == None:
            "wrong_action"
        else:
            if action == "exit":
                exitApplication()
            if action == "list_all_friends":
                listAllFriends()
            if action == "search_friend_by_phone":
                searchFriendByPhone()
            if action == "friend_form_remove":
                removeFriendForm()
            if action == "friend_form_add":
                addFriend()
            if action == "search_friends_by_name":
                searchFriendsByName()
            if action == "friend_form_modify":
                modifyFriendForm()
            if action == "wrong_action":
                print("Wrong option")
        
        def exitApplication(self):
            quit()
    
        def listAllFriends(self):
            """ List all friends in the data source
            """
            data = model.findAll()
            if data != None:
                self.view.showFriendTable(data)
            else:
                self.view.showMessage("Error retrieving data")
                
        def searchFriendByPhone(self):
            phone = self.view.showInputDialog("Input phone: ")
            if phone != None:
                friend = Friend(phone)
                found = model.find(friend)
                if found != None:
                    self.view.friendForm(found)
                else:
                    self.view.showMessage("Friend not found")
            else:
                self.view.showMessage("Error in parameter phone")
        
        def searchFriendsByName(self):
            name = self.view.showInputDialog("Input phone: ")
            if name == None:
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
            phone = self.view.inputDialog("Input phone: ")
            if phone != None:
                friend = Friend(phone)
                found = self.model.find(friend)
                if found != None:
                    newFriend = self.view.friendForm(found)
                    modifyFriend(friend, newFriend)
                else:
                    self.view.showMessage("Friend not found")
        
        def removeFriendForm(self):
            phone = self.view.showInputDialog("Input phone: ")
            if phone != None:
                friend = Friend(phone)
                found = self.model.find(friend)
                if found != None:
                    removeFriend(friend)
                else:
                    self.view.showMessage("Friend not found")

#Test section

#f = FriendController(FriendModel())
#f.exitApplication()


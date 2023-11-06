from model.FriendModel import FriendModel
from views.FriendView import FriendView
from model.Friend import Friend

class FriendController:
    
    def __init__(self, model: FriendModel):
        self.model = model
        self.view = FriendView(model)
        view.display()
        
        
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
                view.showFriendTable(data)
            else:
                view.showMessage("Error retrieving data")
                
        def searchFriendByPhone(self):
            phone = view.showInputDialog("Input phone: ")
            if phone != None:
                friend = Friend(phone)
                found = model.find(friend)
                if found != None:
                    view.friendForm(found)
                else:
                    view.showMessage("Friend not found")
            else:
                view.showMessage("Error in parameter phone")
        
        def searchFriendsByName(self):
            name = view.showInputDialog("Input phone: ")
            if name == None:
                data = model.findFriendsByName(name)
                if data != None:
                    view.showFriendTable(data)
                else:
                    view.showMesssage("Error searching Friends")
            else:
                view.showMessage("Error in parameter name")
        
        def addFriend(self):
            friend = view.friendForm(None)
            if friend != None:
                result = model.add(friend)
                if result > 0:
                    view.showMessage("Friend succesfully added")
                else:
                    view.showMessage("Friend has not been added")
            else:
                view.showMessage("Error in parameters")
        
        def modifyFriend(self, oldVersion, newVersion):
            result = model.modify(oldVersion, newVersion)
            if (result > 0):
                view.showMessage("Friend succesfully modified")
            else:
                view.showMessage("Friend has not been modified")
        
        def removeFriend(self, friend):
            result = model.remove(friend)
            if result > 0:
                view.showMessage("Friend succesfully removed")
            else:
                view.showMessage("Friend has not been removed")
                
        def modifyFriendForm(self):
            phone = view.inputDialog("Input phone: ")
            if phone != None:
                friend = Friend(phone)
                found = model.find(friend)
                if found != None:
                    newFriend = view.friendForm(found)
                    modifyFriend(friend, newFriend)
                else:
                    view.showMessage("Friend not found")
        
        def removeFriendForm(self):
            phone = view.showInputDialog("Input phone: ")
            if phone != None:
                friend = Friend(phone)
                found = model.find(friend)
                if found != None:
                    removeFriend(friend)
                else:
                    view.showMessage("Friend not found")

#Test section

#f = FriendController(FriendModel())
#f.exitApplication()


from controllers.FriendController import *
from model.FriendModel import *
from model.Friend import *
from views.FriendMenu import FriendMenu

class FriendView:
    def __init__(self, control, model):
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
            action = self.menu.getSelectedOptionActionCommand()
            self.processAction(action)
            
            
    def processAction(self, action):
        if action != None:
            if action:
                self.control.processRequest(action)
    
    def showFriendTable(self, data):
        cont = 0
        for Friend in data:
            print(Friend)
            cont = cont + 1
        print(str(cont) + " Elements found. " + str(len(data)))
        
    def friendForm(self, inputF: Friend):
        if inputF != None:
            print(inputF)
        else:
            try:
                print("Input new phone: ")
                phone = input()
                print("Input new name: ")
                name = input()
                print("Input new age: ")
                age = input()
                age = int(age)
                inputF = Friend(phone, name, age)
            except:
                print("Error retriving data")
                inputF = None
        return inputF
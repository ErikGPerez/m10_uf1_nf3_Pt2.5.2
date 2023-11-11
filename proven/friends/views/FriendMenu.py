from proven.friends.views.Option import Option
from proven.friends.views.Menu import Menu


class FriendMenu(Menu):
    
    def __init__(self):
        super().__init__("Friends Manager main menu")
        self.addOption(Option("Exit", "exit"))
        self.addOption(Option("List all friends", "list_all_friends"))
        self.addOption(Option("Find friend by phone", "search_friend_by_phone"))
        self.addOption(Option("Find friends by name", "search_friend_by_name"))
        self.addOption(Option("Add friend", "friend_form_add"))
        self.addOption(Option("Modify friend", "friend_form_modify"))
        self.addOption(Option("Remove friend", "friend_form_remove"))
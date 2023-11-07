import Option
import Menu


class FriendMenu(Menu):
    
    def __init__(self):
        super("Friends Manager main menu")
        Menu.addOption(Option("Exit", "exit"))
        Menu.addOption(Option("List all friends", "list_all_friends"))
        Menu.addOption(Option("Find friend by phone", "search_friend_by_phone"))
        Menu.addOption(Option("Find friends by phone", "search_friend_by_name"))
        Menu.addOption(Option("Modify friend", "friend_form_modify"))
        Menu.addOption(Option("Remove friend", "friend_form_remove"))
        
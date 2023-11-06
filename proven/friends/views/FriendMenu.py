import Option
import Menu


class FriendMenu(Menu):
    
    def __init__(self):
        super("Friends Manager main menu")
        addOption(Option("Exit", "exit"))
        addOption(Option("List all friends", "list_all_friends"))
        addOption(Option("Find friend by phone", "search_friend_by_phone"))
        addOption(Option("Find friends by phone", "search_friend_by_name"))
        addOption(Option("Modify friend", "friend_form_modify"))
        addOption(Option("Remove friend", "friend_form_remove"))
        
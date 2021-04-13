from menu import BaseMenu
from utils import *
from custom_exceptions import *

class FeedMenu(BaseMenu):
    __header = "*****Feed*****"
    __options = "[1] Back"
    __next_menus = {
        '1': lambda *_: raise_exception(ExitFromMenuException)
    }

    def __init__(self, user_controller, profile_controller, post_controller):
        self.__user_controller = user_controller
        self.__profile_controller = profile_controller
        self.__post_controller = post_controller

        
    def show(self):
        print(self.__header)
        feed = self.__post_controller.select_all_posts()
        for i in feed:
            print(f"From {i['username']}\nDate: {i['creation_date']}\nTitle: {i['title']}\nDescription: {i['description']})\n")
        print(self.__options)
        input_func = get_option_input()


        def get_input():
            selected_option = input_func('Enter option: ')
            if selected_option not in self.__next_menus.keys():
                raise UserInputOptionException
            return selected_option

        while True:
            selected_option = self.input_secure_wrap(get_input)

            try:
                self.__next_menus[selected_option]()
            except ExitFromMenuException:
                return



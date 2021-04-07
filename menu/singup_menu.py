from menu.base_menu import BaseMenu
from menu.main_menu import MainMenu
from utils import get_option_input, raise_exception
from custom_exceptions import UserInputOptionException, ExitFromMenuException
from models.context import Context

class SignupMenu(BaseMenu):
    pass
    __header = "******Please SIGN UP******\nLet's create your profile"
    __options = "[1] Retry\n [2] Back"

    def __init__(self, user_controller, profile_controller, post_controller):
        self.__user_controller = user_controller
        self.__profile_controller = profile_controller
        self.__post_controller = post_controller
    

        self.__next_menus = {
            '1': lambda *_: None,
            '2': lambda *_: raise_exception(ExitFromMenuException)
        }
        
    def show(self):
        print(self.header)
        input_func = get_option_input()


        def get_input():
            selected_option = input_func('Enter option: ')
            if selected_option not in self.__next_menus.keys():
                raise UserInputOptionException
            return selected_option

        while True:
            pass
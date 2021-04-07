from menu.base_menu import BaseMenu
from models import Context
from menu.myprofile_menu import ProfileMenu
from menu.mypage_menu import MyPageMenu
from menu.feed_menu import FeedMenu
from utils import get_option_input
from custom_exceptions import ExitFromMenuException

class MainMenu(BaseMenu):
    __header = "*****Main Menu*****"
    __options = "[1] My Profile\n [2] My posts\n [3] Feed"
    __next_menus = {
        '1': ProfileMenu,
        '2': MyPageMenu,
        '3': FeedMenu
    }

    def __init__(self, user_controller, profile_controller, post_controller):
        self.__user_controller = user_controller
        self.__profile_controller = profile_controller
        self.__post_controller = post_controller
        self.__context = Context()    

        
    def show(self):
        print(self.header)
        print("Welcome to your page", self.__context.user.)
        print(self.__context)
        input_func = get_option_input()


        def get_input():
            selected_option = input_func('Enter option: ')
            if selected_option not in self.__next_menus.keys():
                raise UserInputOptionException
            return selected_option

        while True:
            selected_option = self.input_secure_wrap(get_input)

            try:
                self.__next_menus[selected_option](
                    self.__user_controller,
                    self.__profile_controller,
                    self.__post_controller
                )
            except ExitFromMenuException:
                return

    
            





from menu.base_menu import BaseMenu
from menu import *
from models import Context
from utils import get_option_input, get_confirm_input, raise_exception
from custom_exceptions import ExitFromMenuException

class DeleteUserMenu(BaseMenu):
    __header = "*****Main Menu*****"
    __options = "[1] Delete User\n[2] Back"


    def __init__(self, user_controller, profile_controller, post_controller):
        self.__user_controller = user_controller
        self.__profile_controller = profile_controller
        self.__post_controller = post_controller
        self.__context = Context()    

        self.__next_menus = {
            '1': self.delete_all_data,
            '2': lambda *_: raise_exception(ExitFromMenuException)
        }

    def delete_all_data(self):        
        confirm_input_func = get_confirm_input()

        def confirm():
            return confirm_input_func("Are you sure? ('y' or 'n'): ")

        user_confirm = self.input_secure_wrap(confirm)

        if user_confirm == 'y':
            print(self.__context.user.id)
            if self.__post_controller.delete_all_user_post(self.__context.user.id):
                if self.__user_controller.delete_user(self.__context.user.id):
                    print(self.__context.profile.id)
                    if self.__profile_controller.delete_profile(self.__context.profile.id):
                       input("Your data deleted! Bye!")
                       start = StartMenu()
                       start.show()       
        else:
            input("Error in data base")


    def show(self):
        input_func = get_option_input()


        def get_input():
            selected_option = input_func('Enter option: ')
            if selected_option not in self.__next_menus.keys():
                raise UserInputOptionException
            return selected_option

        while True:
            print(self.__header)
            print(self.__options)

            selected_option = self.input_secure_wrap(get_input)

            try:
                next_menu = self.__next_menus[selected_option]()
            except ExitFromMenuException:
                return

    
            




from menu.base_menu import BaseMenu
from menu.signin_menu import SinginMenu
from menu.singup_menu import SignupMenu
from utils import get_option_input, raise_exception
from custom_exceptions import UserInputOptionException
from utils import get_option_input, raise_exception

class StartMenu(BaseMenu):
    header = "******BLOG******\nplease SING IN or SIGN UP"
    options = '[1] - SIGN IN\n[2] - SIGN UP\n[3] - Exit'
    next_menus = {
        '1': SinginMenu,
        '2': SignupMenu,
        '3': lambda: raise_exeption(KeyboardInterrupt)
    }


    def __init__(self, user_controller, profile_controller, post_controller):
        self.__user_controller = user_controller
        self.__profile_controller = profile_controller
        self.__post_controller = post_controller


    def show(self):
        input_func = get_option_input()

        def get_input():
            selected_option = input_func('Enter option')
            if selected_option not in self.next_menus.keys():
                raise UserInputOptionException
            return selected_option

        while True:
            print(self.header)
            print(self.options)

            selected_option = self.input_secure_wrap(get_input)

            next_menu = self.next_menus[selected_option](
                self.__user_controller,
                self.__profile_controller,
                self.__post_controller
            )
            
            next_menu.show()
            


     
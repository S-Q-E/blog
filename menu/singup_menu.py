from menu.base_menu import BaseMenu
from menu.main_menu import MainMenu
from utils import *
from custom_exceptions import UserInputOptionException, ExitFromMenuException
from models.context import Context
from models.profile import Profile
from models.blog_user import User

class SignupMenu(BaseMenu):
    pass
    __header = "******Please SIGN UP******"

    def __init__(self, user_controller, profile_controller, post_controller):
        self.__user_controller = user_controller
        self.__profile_controller = profile_controller
        self.__post_controller = post_controller
    

        

    def show(self):
        print(self.__header)
        get_age = get_age_input()
        input_func = get_option_input()
        input_username_func = get_username_input()
        input_password_func = get_password_input()
        
        def get_age_from_user():
            return get_age("Enter your age:_")

        def get_username():
            return input_username_func("Enter username:_ ")

        def get_password():
            return input_password_func("Enter password:_ ")

        while True:

            username = self.input_secure_wrap(get_username)
            password = self.input_secure_wrap(get_password)
            
            if self.__user_controller.is_user_exist(username):
                print(f"User {username} already exist!")
                continue

            profile_id = self.__profile_controller.create_empty_profile()
            
            if profile_id:
                user = User(username, password, profile_id)
                self.__user_controller.create_user(user)
                input(f"User {username} created!\nPress Enter to continue")
                return
            else:
                input('Registration failed! Try again!')
            
            
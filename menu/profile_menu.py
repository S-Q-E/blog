from menu import BaseMenu
from utils import get_option_input
from custom_exceptions import ExitFromMenuException
from models import Context
from utils import *

class ProfileMenu(BaseMenu):
    __header = "*****My profile*****"
    __options = "[1] Edit first name\n[2] Edit second name\n[3] Edit last name\n[4] Edit age\n[5] Back"
    
    def __init__(self, user_controller, profile_controller, post_controller):
        self.__user_controller = user_controller
        self.__profile_controller = profile_controller
        self.__post_controller = post_controller  
        self.__context = Context()

        self.__next_menus = {
            '1': self.edit_fname,
            '2': self.edit_sname,
            '3': self.edit_lname,
            '4': self.edit_age,
            '5': lambda *_: raise_exception(ExitFromMenuException)
        }

    def edit_fname(self):
        input_name_func = get_name_input()

        def curr_name_input():
            return input_name_func("Enter new first name: ")
        
        new_first_name = self.input_secure_wrap(curr_name_input)

        self.__context.profile.first_name = new_first_name
        
        #спросить почему тут выходить что ошибка а на самом деле нет!
        if self.__profile_controller.update_profile(self.__context.profile):
            input("First name changed!\nPress Enter ==>>")
        else:
            print("Some error in database")

        
    def edit_sname(self):
        input_name_func = get_name_input()

        def curr_name_input():
            return input_name_func("Enter new second name: ")
        
        new_second_name = self.input_secure_wrap(curr_name_input)

        self.__context.profile.second_name = new_second_name

        if not self.__profile_controller.update_profile(self.__context.profile):
            print("Some error in database")
        else:
            input("Second name changed!\nPress Enter ==>>")
        

    def edit_lname(self):
        input_name_func = get_name_input()

        def curr_name_input():
            return input_name_func("Enter new last name: ")
        
        new_last_name = self.input_secure_wrap(curr_name_input)

        self.__context.profile.last_name = new_last_name

        if not self.__profile_controller.update_profile(self.__context.profile):
            print("Some error in database")
        else:
            input("Second name changed!\nPress Enter ==>>")
        

    def edit_age(self):
        input_age_func = get_age_input()

        def curr_age_input():
            return input_age_func("Enter new age")
        
        new_age = self.input_secure_wrap(curr_age_input)

        self.__context.profile.age = new_age

        if not self.__profile_controller.update_profile(self.__context.profile):
            print("Some error in database")
        else:
            input("Second name changed!\nPress Enter ==>>")


    def show(self):
        input_func = get_option_input()

        def get_input():
            selected_option = input_func('Enter option: ')
            if selected_option not in self.__next_menus.keys():
                raise UserInputOptionException
            return selected_option

        while True:
            print(self.__header)
            print("First name:", self.__context.profile.first_name)
            print("Second name:", self.__context.profile.second_name)
            print("Last name:", self.__context.profile.last_name)
            print("Age:", self.__context.profile.age)
            print(self.__options)
            selected_option = self.input_secure_wrap(get_input)
            
            try:
                self.__next_menus[selected_option]()     
            except ExitFromMenuException:
                return


    
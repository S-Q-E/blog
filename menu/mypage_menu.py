from menu import BaseMenu
from utils import *
from custom_exceptions import *
from models import Context, Post

class MyPageMenu(BaseMenu):
    __header = "*****Your posts*****"
    __options = "[1] Create post \n[2] Edit post\n[3] Delete post\n[4] All my post\n[5] Back"

    def __init__(self, user_controller, profile_controller, post_controller):
        self.__user_controller = user_controller
        self.__profile_controller = profile_controller
        self.__post_controller = post_controller
        self.__context = Context()

        self.__next_menus = {
            '1': self.create_post,
            '2': self.edit_post,
            '3': self.delete_post,
            '4': self.show_all_my_posts,
            '5': lambda *_: raise_exception(ExitFromMenuError)
        }

    def create_post(self):
        title = input("Enter title of post: ")
        description = input("Enter description: ")
        user_id = self.__user_controller.select_userid_by_username(self.__context.user.username)

        new_post = Post(user_id = user_id, title= title, description = description)
        
        
        if self.__post_controller.create_post(new_post):
            print("Post created!")

    
    def delete_post(self):
        posts = self.__post_controller.select_all_my_posts()
        for i in posts:
            print(f"ID: ({i['id']})\nTitle: {i['title']}")
            id_input = get_post_id_fucn()
            if id_input not in i['id']:
                print("Incorrect ID")
            else:
                self.__post_controller.delete_post(id_input)
        

    def show_all_my_posts(self):
        posts = self.__post_controller.select_all_my_posts()
        for i in posts:
            print(f"Date: ({i['creation_date']})\nTitle: {i['title']}\nDescription: {i['description']}")

        input("Press Enter for back to ")


    def edit_post(self):
        pass

                
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
                self.__next_menus[selected_option]()
            except ExitFromMenuException:
                return



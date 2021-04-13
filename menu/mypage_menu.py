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
            '5': lambda *_: raise_exception(ExitFromMenuException)
        }

    def create_post(self):
        title = input("Enter title of post: ")
        description = input("Enter description: ")
        user_id = self.__user_controller.select_userid_by_username(self.__context.user.username)

        new_post = Post(user_id = user_id, title= title, description = description)
        
        
        if self.__post_controller.create_post(new_post):
            print("Post created!")

    
    def delete_post(self):
        posts = self.__post_controller.select_all_my_posts(self.__context.user.id)
        ids = []
        for i in posts:
            ids.append(i['id'])
            print(f"ID: ({i['id']})\nTitle: {i['title']}")
            id_input = get_post_id_fucn()
            def get_id():
                return id_input("Enter post id: ")

            selected_id = self.input_secure_wrap(get_id)

            if int(selected_id) not in ids:
                print("Incorrect ID")
                continue
            else:
                if self.__post_controller.delete_post(selected_id):
                    input("Post deleted")
                else:
                    input("Some error in data base")
        


    def show_all_my_posts(self):
        posts = self.__post_controller.select_all_my_posts(self.__context.user.id)
        for i in posts:
            print(f"Date: ({i['creation_date']})\nTitle: {i['title']}\nDescription: {i['description']}\n")
        
        

        input("Press Enter for back to ")


    def edit_post(self):
        posts = self.__post_controller.select_all_my_posts(self.__context.user.id)
        ids = []
        for i in posts:
            print(f"ID: ({i['id']})\nTitle: {i['title']}\nDescription: {i['description']}\n")
            ids.append(i['id'])

        user_input = id_input("Please choose post's id")
        if int(user_input) not in ids:
            input("Can't found such id")
            raise_exception(ExitFromMenuException)
        else:
            title = input("Enter new title")
            description = input("Enter new description")

        user_id = self.__user_controller.select_userid_by_username(self.__context.user.username)
        new_post = Post(id = int(user_input), user_id = user_id, title= title, description = description)

        if not self.__post_controller.update_post(new_post):
            input("Some error in DB")
        else:
            input("Post edited! Press Enter to continue..")

                
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



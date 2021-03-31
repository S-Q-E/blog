from models.repositories import UserRepository

class UserController:
    __user_repo = None

    def __init__(self, user_repo: UserRepository):
        self.__user_repo = user_repo

    def create_user(self, user):
        return self.__user_repo.create_user(user)

    def delete_user(self, user):
        return self.__user_repo.delete_user(user)

    def update_user(self, user):
        return self.__user_repo.update_user(user)

    def show_user(self, user):
        return self.__user_repo.update_user(user)

    
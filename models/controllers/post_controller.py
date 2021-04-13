# from models.repositories import PostRepository

class PostController:
    __post_repo = None

    def __init__(self, post_repo):
        self.__post_repo = post_repo

    def create_post(self, post):
        return self.__post_repo.create_post(post)

    def delete_post(self, id):
        return self.__post_repo.delete_post(id)

    def select_post(self, id):
        return self.__post_repo.select_post(id)

    def update_post(self, post):
        return self.__post_repo.update_post(post)

    def select_all_posts(self):
        return self.__post_repo.select_all_post()

    def select_all_my_posts(self, user_id):
        return self.__post_repo.select_all_my_posts(user_id)
    
    def delete_all_user_post(self, user_id):
        return self.__post_repo.delete_all_user_post(user_id)
from models.repositories import PostRepository

class PostController:
    __post_repo = None

    def __init__(self, post_repo: PostRepository):
        self.__post_repo = post_repo

    def create_post(self, post: Post):
        return self.__post_repo.create_post(post)

    def delete_post(self, post: Post):
        return self.__post_repo.delete_post(post)

    def show_post(self, post: Post):
        return self.__post_repo.show_post(user)

    def update_post(self, post: Post):
        return self.__post_repo.update_post(user)

    
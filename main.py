from db import DBService
from models import User, Profile, Post
from models.repositories import UserRepository, ProfileRepository, PostRepository
from models.controllers import UserController, ProfileController, PostController

def main():
    db = DBService()
    profile_repo = ProfileRepository(db)
    prof_control = ProfileController(profile_repo)
    profile = Profile(id= 2, first_name = "Rikardo", second_name="Izecson", last_name="Silva", age = 35)
    
    if prof_control.show_profile(profile):
        print('Profile created!')
    

    
    # user_repo = UserRepository(db)
    # user_controller = UserController(user_repo)

    # user = User('ricardo', 'password12', 2)
    # if user_controller.create_user(user):
    #     print('User created!')

    # post_repo = PostRepository(db)
    # post_control = PostController(post_repo)

    # post = Post(user_id=6, title='My first post', description='Hello everyone! Glad to be here! nice social platform! I will be send post here everyday!')
    # if post_control.create_post(post):
    #     print('Well done!')


if __name__ == '__main__':
    main()
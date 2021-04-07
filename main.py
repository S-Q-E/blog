from db import DBService
from models import User, Profile, Post
from models.repositories import UserRepository, ProfileRepository, PostRepository
from models.controllers import UserController, ProfileController, PostController
from menu.start_menu import StartMenu

def main():
    db = DBService()

    user_repo = UserRepository(db)
    profile_repo = ProfileRepository(db)
    post_repo = PostRepository(db)

    user_controller = UserController(user_repo)
    profile_controller = ProfileController(profile_repo)
    post_controller = PostController(post_repo)
    
    app = StartMenu(user_controller, profile_controller, post_controller)
    app.show()
    

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Disconnecting from DB...')
        db = DBService()
        db.close()
        print('Bye!')
    
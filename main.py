from db import DBService
from models import User
from models.repositories import UserRepository
from models.controllers import UserController

def main():
    db = DBService()
    user_repo = UserRepository(db)
    user_controller = UserController(user_repo)
    
    user = User('Artem', 'Gromov', 1)

    if user_controller.delete_user(user):
        print('успех')

if __name__ == '__main__':
    main()
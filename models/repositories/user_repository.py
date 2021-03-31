from db import DBService
from models import User

class UserRepository:
    __db = None
    
    def __init__(self, db: DBService):
        self.__db = db
        
    def create_user(self, user: User):
        """
        Выполняет добавление пользователя в бд. 
        :param user: - User
        :return bool: - False - ошибка, True - успех
        """

        try:
            with self.__db.connection.cursor() as cursor:
                query = "INSERT INTO blog_user (username, password, profile_id) VALUES ('{username}', '{password}', {profile_id})"
                query = query.format(
                    username = user.username, 
                    password = user.password,
                    profile_id = user.profile_id
                )

                self.__db.execute(query)

            return True
        except Exception as ex:
            print(ex)
            return False

    
    def show_user(self, user: User):
        """
        Показывает данные пользователя в бд
        :param user: - User
        :return bool: - False - ошибка, True - успех
        """
        try:
            with self.__db.connection.cursor() as cursor:
                query = "SELECT * FROM blog_user where id = {id};"
                query = query.format(
                    id = user.id
                )
                self.__db.execute(query)

            return True
        except Exception as ex:
            print(ex)
            return False    

        
    def delete_user(self, user: User):
        """
        Удаляет пользователя из бд.
        :param user: - User
        :return bool: - False - ошибка, True - успех
        """
        try:
            with self.__db.connection.cursor() as cursor:
                query = "DELETE FROM blog_user where id = {id};"
                query = query.format(
                    id = user.id
                )
                self.__db.execute(query)
                connect.commit()
            return True
        except Exception as ex:
            print(ex)
            return False


    def update_profile(self, user):
        """
        Обовляет данные профиля в бд.
        :param user: - User
        :return bool: - False - ошибка, True - успех
        """
        try:
            with self.__db.connection.cursor() as cursor:
                query = "UPDATE blog_user SET username = {username}, `password` = {password};"
                query = query.format(
                    username = user.username,
                    password = user.password
                )
                self.__db.execute(query)
                cursor.commit()
            return True
        except Exception as ex:
            print(ex)
            return False
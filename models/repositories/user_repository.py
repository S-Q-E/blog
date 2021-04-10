from db import DBService
from models.blog_user import User
from custom_exceptions import RepositoryError
from models.controllers import ProfileController
import models.repositories

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


    def login_user(self,username, password):
        """
        Возвращает объект класса User, если есть запись в бд
        :param username: - str
        :param password: - str
        :return (User, Profile): - успех
        :return None - неправильные данные
        :raise RepositoryError: - ошибка в бд
        """
        try:
            query = "SELECT * FROM blog_user WHERE username = '{username}' AND password = '{password}'"
            query = query.format(username= username, password= password)
            self.__db.execute(query)

            if self.__db.cursor.rowcount == 1:
                user = User.from_dict(self.__db.cursor.fetchone())
                
                if user:
                    profile_repo = models.repositories.ProfileRepository(self.__db)
                    profile_controller = ProfileController(profile_repo)
                    profile = profile_controller.select_profile(user.profile_id)

                    if profile:
                        return (user, profile)
            elif self.__db.cursor.rowcount > 1:
                raise RepositoryError
            return (None, None)
        except Exception as ex:
            print("user_repsitory exepcion", ex)
    

    def select_user_by_username(self, username):
        try:
            query = "SELECT * FROM blog_user where username = '%s'" % username
            self.__db.execute(query)

            if self.__db.cursor.rowcount > 0:
                return User.from_dict(self.__db.cursor.fetchone())
            else:
                return None
        except Exception as ex:
            print(ex)
            raise 
        
    
    def select_userid_by_username(self, username):
        try:
            query = "SELECT id FROM blog_user where username = '%s'" % username
            self.__db.execute(query)

            if self.__db.cursor.rowcount == 1:
                return self.__db.cursor.fetchone()['id']
            else:
                return None
        except Exception as ex:
            print(ex)
            raise 
        




    def select_user(self, id):
        """
        Возвращает объект класса User с бд с нужным нам id
        :param id: - int
        :return User: - успешный select (такая запись есть)
        :return None: - такой записи нету
        :raise RepositoryError: - ошибка в бд
        """

        try:
            query = "SELECT * FROM blog_user WHERE id = %d" % id
            self.__db.execute(query)
            

            if self.__db.cursor.rowcount == 1:
                return User.from_dict(self.__db.cursor.fetchone())
            else:
                return None
        except Exception as ex:
            print(ex)
             


    def delete_user(self, id):
        """
        Удаляет пользователя из бд.
        :param user: - User
        :return bool: - False - ошибка, True - успех
        """
        try:
            query = "DELETE FROM blog_user where id = %d" % id 
            self.__db.execute(query)
        except Exception as ex:
            print(ex)
            raise RepositoryError


    def update_user(self, user:User):
        """
        Обовляет данные профиля в бд.
        :param user: - User
        :raise RepositoryError: - Ошибка в базе данных 
        """
        try:
            query = "UPDATE blog_user SET username = '{username}', password = '{password}', profile_id = {profile_id} where id = {id}"
            query = query.format(
                username = user.username,
                password = user.password,
                profile_id = user.profile_id,
                id = user.id
            )
            self.__db.execute(query)
        except Exception as ex:
            print(ex)
            raise RepositoryError
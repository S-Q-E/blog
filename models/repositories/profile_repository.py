from db import DBService
from models import Profile

class ProfileRepository:
    __db = None
    
    def __init__(self, db: DBService):
        self.__db = db

    def show_profile(self, profile: Profile):
        """
        Показывает данные профиля в бд
        :param profile: - Profile
        :return bool: - False - ошибка, True - успех
        """
        try:
            with self.__db.connection.cursor() as cursor:
                query = "SELECT * FROM profile where id = {id}"
                query = query.format(
                    id = profile.id
                )
                self.__db.execute(query)
                data = cursor.fetchall()
                print(data)

            return True
        except Exception as ex:
            print(ex)
            return False
        
    
    def create_profile(self, profile: Profile):
        """
        Добавляет профиль в бд.
        :param profile: - Profile
        :return bool: - False - ошибка, True - успех
        """
        try:
            with self.__db.connection.cursor() as cursor:
                query = "INSERT INTO profile (first_name, second_name, last_name, age) VALUES ('{firstname}', '{secondname}', '{lastname}', {age})"
                query = query.format(
                    firstname = profile.first_name,
                    secondname = profile.second_name,
                    lastname = profile.last_name,
                    age = profile.age 
                )

                self.__db.execute(query)
                self.__db.connection.commit()

            return True
        except Exception as ex:
            print("Error in profile repo", ex)
            return False
 

        
    def delete_profile(self, profile: Profile):
        """
        Удаляет профиль из бд.
        :param profile: - Profile
        :return bool: - False - ошибка, True - успех
        """
        try:
            with self.__db.connection.cursor() as cursor:
                query = "DELETE FROM profile where id = {id};"
                query = query.format(
                    id = profile.id
                )
                self.__db.execute(query)
                connect.commit()
            return True
        except Exception as ex:
            print(ex)
            return False


    def update_profile(self, profile: Profile):
        """
        Обовляет данные профиля в бд.
        :param profile: - Profile
        :return bool: - False - ошибка, True - успех
        """
        try:
            with self.__db.connection.cursor() as cursor:
                query = "UPDATE profile SET first_name = {firstname}, second_name = {secondname}, last_name = {lastname}, age = {age};"
                query = query.format(
                    firstname = profile.first_name,
                    secondname = profile.second_name,
                    lastname = profile.last_name,
                    age = profile.age
                )
                self.__db.execute(query)
                cursor.commit()
            return True
        except Exception as ex:
            print(ex)
            return False
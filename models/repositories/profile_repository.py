from db import DBService
from models import Profile
from custom_exceptions import RepositoryError

class ProfileRepository:
    __db = None
    
    def __init__(self, db: DBService):
        self.__db = db



    def select_profile(self, id):
        """
        Возвращает объект класса Profile c бд с н ужжным id
        :param id: - int успешный select (такая запись есть)
        :return Profile: - False - ошибка, True - успех
        :return None: - нету такой записи
        :raise Repository Error: - ошибка в бд
        """
        try:
            query = "SELECT * FROM profile where id = %d" % id
            self.__db.execute(query)

            if self.__db.cursor.rowcount == 1:
                return Profile.from_dict(self.__db.cursor.fetchone())
            else:
                return None

        except Exception as ex:
            print(ex)
            raise RepositoryError
        
    
    def create_profile(self, profile: Profile):
        """
        Добавляет профиль в бд.
        :param profile: - Profile
        :return bool: - False - ошибка, True - успех
        """
        try:
            query = "INSERT INTO profile (first_name, second_name, last_name, age) VALUES ('{firstname}', '{secondname}', '{lastname}', {age})"
            query = query.format(
                firstname = profile.first_name,
                secondname = profile.second_name,
                lastname = profile.last_name,
                age = profile.age 
            )
            
            self.__db.execute(query)
            return True
        except Exception as ex:
            print(ex)
            return False
 

        
    def delete_profile(self, id):
        """
        Удаляет профиль из бд.
        :param profile: - Profile
        :return bool: - False - ошибка, True - успех
        """
        try:
            query = "DELETE FROM profile where id = %d" % id
            self.__db.execute(query)
            return True
        except Exception as ex:
            print(ex)
            raise RepositoryError



    def update_profile(self, profile: Profile):
        """
        Обовляет данные профиля в бд.
        :param profile: - Profile
        :raise RepositoryError: ошибка в базе данных
        """
        try:
            query = "UPDATE profile SET first_name = '{firstname}', second_name = '{secondname}', last_name = '{lastname}', age = {age} WHERE id = {id}"
            query = query.format(
                firstname = profile.first_name,
                secondname = profile.second_name,
                lastname = profile.last_name,
                age = profile.age,
                id = profile.id
            )
        
            self.__db.execute(query)
        except Exception as ex:
            print(ex)
            return False
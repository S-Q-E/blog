from db import DBService
from models import Post

class PostRepository:
    __db = None
    
    def __init__(self, db: DBService):
        self.__db = db

    def show_post(self, post: Post):
        """
        Показывает посты в бд. 
        :param post: - Post
        :return bool: - False - ошибка, True - успех
        """
        try:
            with self.__db.connection.cursor() as cursor:
                query = "SELECT * FROM post where id = {id};"
                query = query.format(
                    id = post.id
                )
                self.__db.execute(query)
                data = cursor.fetchall()
                print(data)
            return True
        except Exception as ex:
            print(ex)
            return False

        
    def create_post(self, post: Post):
        """
        Добавляет посты в бд. 
        :param post: - Post
        :return bool: - False - ошибка, True - успех
        """
        try:
            with self.__db.connection.cursor() as cursor:
                query = "INSERT INTO post (user_id, title, description) VALUES ({userid}, '{title}', '{description}')"
                query = query.format(
                    userid = post.user_id,
                    title = post.title,
                    description = post.description
                )
                self.__db.execute(query)
                self.__db.connection.commit()

            return True
        except Exception as ex:
            print(ex)
            return False
        
    def delete_profile(self, post: Post):
        """
        Удаляет посты из бд. 
        :param post: - Post
        :return bool: - False - ошибка, True - успех
        """
        try:
            with self.__db.connection.cursor() as cursor:
                query = "DELETE FROM post where id = {id};"
                query = query.format(
                    id = post.id
                )
                self.__db.execute(query)
                self.__db.connection.commit()

            return True
        except Exception as ex:
            print(ex)
            return False


    def update_post(self, post):
        """
        Обновляет данные поста в бд. 
        :param post: - Post
        :return bool: - False - ошибка, True - успех
        """
        try:
            with self.__db.connection.cursor() as cursor:
                query = "UPDATE post SET `user_id` = {userid}, `title` = '{title}', `description` = '{decrip}';"
                query = query.format(
                    userid = post.user_id,
                    title = post.title,
                    desrip = post.desription
                )
                self.__db.execute(query)
                self.__db.connection.commit()
            return True
        except Exception as ex:
            print(ex)
            return False

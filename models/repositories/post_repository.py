from db import DBService
from models import Post
from custom_exceptions import RepositoryError

class PostRepository:
    __db = None
    
    def __init__(self, db: DBService):
        self.__db = db


    def select_post(self, id):
        """
        Возвращает объект класса Profile c бд с н ужжным id
        :param id: - int успешный select (такая запись есть)
        :return Profile: - False - ошибка, True - успех
        :return None: - нету такой записи
        :raise Repository Error: - ошибка в бд
        """
        try:
            query = "SELECT * FROM post where id = %d" % id
            self.__db.execute(query)
            if self.__db.cursor.rowcount == 1:
                return Post.from_dict(self.__db.cursor.fetchone())
            else:
                return None
        except Exception as ex:
            print(ex)
            # raise RepositoryError

        
    def create_post(self, post: Post):
        """
        Добавляет посты в бд. 
        :param post: - Post
        :return bool: - False - ошибка, True - успех
        """
        try:
            query = "INSERT INTO post (user_id, title, description) VALUES ({userid}, '{title}', '{description}')"
            query = query.format(
                userid = post.user_id,
                title = post.title,
                description = post.description
            )
            self.__db.execute(query)
            return True
        except Exception as ex:
            print(ex)
            return False
        
    def delete_post(self, id):
        """
        Удаляет посты из бд. 
        :param post: - Post
        :return bool: - False - ошибка, True - успех
        """
        try:
            query = "DELETE FROM post where id = %d" % id
            self.__db.execute(query)
        except Exception as ex:
            print(ex)
            raise RepositoryError


    def update_post(self, post: Post):
        """
        Обновляет данные поста в бд. 
        :param post: - Post
        :return bool: - False - ошибка, True - успех
        """
        try:
            query = "UPDATE post SET user_id = {userid}, title = '{title}', description = '{descrip}'"
            query = query.format(
                userid = post.user_id,
                title = post.title,
                descrip = post.description
            )
            self.__db.execute(query)
        except Exception as ex:
            print(ex)
            
    def select_all_post(self):
        try:
            query = " select blog_user.username, post.creation_date,  post.title, post.description  from post inner join blog_user on post.user_id = blog_user.id order by post.creation_date ASC"
            self.__db.execute(query)

            return self.__db.cursor.fetchall()
        except Exception as ex:
            print(ex)
            raise RepositoryError

    def select_all_my_posts(self):
        try:
            query = " select * from post where True"
            self.__db.execute(query)

            return self.__db.cursor.fetchall()
        except Exception as ex:
            print(ex)
            raise RepositoryError

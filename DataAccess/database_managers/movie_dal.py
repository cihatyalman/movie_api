from Core.data_access.sqlite_base import SqliteBase
from Entities.movie import Movie
from Business.constants.constant import Constant

class MovieDal(SqliteBase):

    __table_name = "movies"

    def __init__(self):
        super().__init__(Constant.DB_FILE)
        self.__create_table()

    def __create_table(self):
        sql_code = """CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY, name TEXT, link TEXT, imdb REAL, image TEXT, 
        language_index INTEGER, subject TEXT, year INTEGER, category_indexes TEXT)""".format(self.__table_name)
        return super()._create_table(sql_code)
    
    def add(self, movie:Movie):
        sql_code = """INSERT INTO {} (name,link,imdb,image,language_index,subject,
        year,category_indexes) VALUES (?,?,?,?,?,?,?,?)""".format(self.__table_name)
        return super()._add(sql_code, movie.name, movie.link, movie.imdb, movie.image, 
        movie.language_index, movie.subject, movie.year, movie.category_indexes)

    def add_list(self,movie_list):
        "value: list_item_model -> name, link, imdb, image, language_index, subject, year, category_indexes"
        print("Saving {} movie detail...".format(str(len(movie_list))))
        for movie in movie_list:
            self.add(movie)
        print("Saved {} movie detail.".format(str(len(movie_list))))

    def get_end_id(self):
        sql_code = """SELECT id FROM (SELECT * FROM {} ORDER BY id DESC) LIMIT 1""".format(self.__table_name,)
        return super()._get(sql_code)[0][0]

    def get(self, sql_where_code="",reverse_data=False):
        sql_code = """SELECT * FROM (SELECT * FROM {} ORDER BY id {}) {}""".format(self.__table_name,("DESC" if reverse_data else "ASC"),sql_where_code)
        result = super()._get(sql_code)
        return self.convert_object_list(result)

    def convert_object_list(self,tuple_list):
        movie_object_list = []
        for res in tuple_list:
            movie_object_list.append(Movie(res[1],res[2],res[3],res[4],res[5],res[6],res[7],res[8],res[0]).toMap())
        return movie_object_list

    def get_custom_code(self,sql_code):
        result = super()._get(sql_code)
        return self.convert_object_list(result)
        
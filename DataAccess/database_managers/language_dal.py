from Core.data_access.sqlite_base import SqliteBase
from Business.constants.constant import Constant

class LanguageDal(SqliteBase):
    languages = ["Yerli Film","Multi Dil","Türkçe Dublaj","Türkçe Altyazı"]

    __table_name = "languages"
    def __init__(self):
        super().__init__(Constant.DB_FILE)

    def __create_table(self):
        sql_code = """CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY, name TEXT)""".format(self.__table_name)
        super()._create_table(sql_code)
        self.__add()
    
    def __add(self):
        sql_code = """INSERT INTO {} (name) VALUES (?)""".format(self.__table_name)
        for language in self.languages:
            super()._add(sql_code, language)

    def configure(self):
        "Run once !"
        self.__create_table()

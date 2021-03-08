from Core.data_access.sqlite_base import SqliteBase
from Business.constants.constant import Constant

class CategoryDal(SqliteBase):
    categories = ["Aile","Aksiyon","Animasyon","Belgesel","Bilim Kurgu","Biyografi","Dini","Dövüş","Dram","Efsane","Fantastik","Gençlik","Gerilim",
    "Gizem","Hint","Karate","Komedi","Korku","Macera","Müzikal","Netflix","Polisiye","Politik","Romantik","Savaş","Spor","Suç","Tarih","Vahşi Batı"]

    __table_name = "categories"
    
    def __init__(self):
        super().__init__(Constant.DB_FILE)

    def __create_table(self):
        sql_code = """CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY, name TEXT)""".format(self.__table_name)
        super()._create_table(sql_code)
        self.__add()
    
    def __add(self):
        sql_code = """INSERT INTO {} (name) VALUES (?)""".format(self.__table_name)
        for category in self.categories:
            super()._add(sql_code, category)

    def configure(self):
        "Run once !"
        self.__create_table()

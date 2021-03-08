from Core.data_access.sqlite_base import SqliteBase
from Entities.link import Link
from Business.constants.constant import Constant

class LinkDal(SqliteBase):

    __table_name = "links"

    def __init__(self):
        super().__init__(Constant.DB_FILE)
        self.__create_table()
        
    def __create_table(self):
        sql_code = """CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY, name TEXT, link TEXT)""".format(self.__table_name)
        return super()._create_table(sql_code)

    def add(self, link:Link):
        sql_code = """INSERT INTO {} (name,link) VALUES (?,?)""".format(self.__table_name)
        return super()._add(sql_code, link.name, link.link)
        
    def add_list(self,link_datas):
        "value: list_item_model -> name, link"
        print("Saving {} movie links...".format(str(len(link_datas))))
        for link_data in link_datas:
            self.add(link_data)
        print("Saved {} movie links.".format(str(len(link_datas))))
        
    
    def get(self, sql_where_code="",reverse_data=False):
        sql_code = """SELECT * FROM (SELECT * FROM {} ORDER BY id {}) {}""".format(self.__table_name,("DESC" if reverse_data else "ASC"),sql_where_code)
        result = super()._get(sql_code)
        return self.convert_object_list(result)

    def convert_object_list(self,tuple_list):
        link_object_list = []
        for res in tuple_list:
            link_object_list.append(Link(res[1],res[2],res[0]))
        return link_object_list
        
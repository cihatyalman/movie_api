import sqlite3 as sql

class SqliteBase:
    def __init__(self,db_name):
        self.__db_name = db_name
    
    def _create_table(self,sql_code):
        with sql.connect(self.__db_name) as con:
            cur = con.cursor()
            cur.execute(sql_code)

    def _get(self,sql_code):
        with sql.connect(self.__db_name) as con:
            cur = con.cursor()
            cur.execute(sql_code)
            data = cur.fetchall()
        return data

    def _add(self,sql_code,*args):
        with sql.connect(self.__db_name) as con:
            cur = con.cursor()
            cur.execute(sql_code,args)
            con.commit()

    def _update(self,sql_code):
        with sql.connect(self.__db_name) as con:
            cur = con.cursor()
            cur.execute(sql_code)
            con.commit()

    def _delete(self,sql_code):
        with sql.connect(self.__db_name) as con:
            cur = con.cursor()
            cur.execute(sql_code)
            con.commit()


#region Sample Queries 
create_table_code = """CREATE TABLE IF NOT EXISTS demo (id INTEGER PRIMARY KEY,text_value TEXT, decimal_value REAL)"""
add_code = """INSERT INTO demo (text_value,decimal_value) VALUES (?,?)"""
update_code = """UPDATE demo SET text_value = "new_text_value" WHERE id=1"""
delete_code = """DELETE FROM demo WHERE id=1"""
get_code = "SELECT * FROM demo WHERE id=1"
#endregion
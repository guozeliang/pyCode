
import cx_Oracle as oracle

class oracleCon(object):
    def __init__(self,pdbcUrl='phpatient/phpatient@172.16.10.55:1521/oracle11'):
        # connect oracle database
        self.db = oracle.connect(pdbcUrl)

    def queryData(self,sql):
        # create cursor
        cursor = self.db.cursor()
        # execute sql
        cursor.execute(sql)
        data = cursor.fetchall()
        return data

    def __del__(self):
        # close cursor and oracle
        cursor = self.db.cursor()
        cursor.close()
        self.db.close()


if __name__ == '__main__':
    orclConn = oracleCon()
    data = orclConn.queryData("select * from t_member t where t.username = '17737166928'")
    print(data)

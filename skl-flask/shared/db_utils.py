import pymysql
from shared.utils import objectview

class DButils:
    _db = None

    @staticmethod
    def connect():
        # 打开数据库连接
        connect = pymysql.connect("localhost", "root", "xYz_1235813", "sakila", charset='utf8', cursorclass=pymysql.cursors.DictCursor, autocommit=True)
        DButils._db = connect
        # 使用cursor()方法获取操作游标
        cursor = DButils._db.cursor()
        return {
          'connect': connect,
          'cursor': cursor
        }

    @staticmethod
    def closeCon():
        if (DButils._db.open):
            DButils._db.close()

    @staticmethod
    def execute(query, args=None, isDML = False):
      conn = DButils.connect()
      connect, cursor = (lambda connect, cursor: (connect, cursor))(**conn)
      if args is not None:
        cursor.execute(query, args)
      else:
        cursor.execute(query)
      return DButils.returnResult(connect, cursor, False, isDML)


    @staticmethod
    def executemany(query, args=None, isDML = False):
      conn = DButils.connect()
      connect, cursor = (lambda connect, cursor: (connect, cursor))(**conn)
      if args is not None:
        cursor.execute(query, args)
      else:
        cursor.execute(query)
      return DButils.returnResult(connect, cursor, True, isDML)


    @staticmethod
    def executeSqls(sqls):
      conn = DButils.connect()
      connect, cursor = (lambda connect, cursor: (connect, cursor))(**conn)
      try:
          for sql in map(lambda s: objectview(s), sqls):
            if sql.args is not None:
                cursor.execute(sql.query, sql.args)
            else:
                cursor.execute(sql.query)
          connect.commit()
          connect.close()
          return True
      except Exception as e:
          connect.rollback()
          connect.close()
          raise Exception(e)


    def returnResult(connect, cursor, isMany = False, isDML = False):
        result = None
        if isDML:
          connect.commit()
          result = 'OK'
        elif isMany:
          result = cursor.fetchall()
        else:
          result = cursor.fetchone()
        DButils.closeCon()
        return result




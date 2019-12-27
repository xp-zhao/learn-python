import pymysql


def get_db_con():
    host = '47.98.49.140'
    port = 3306
    user = 'root'
    password = '123456'
    database = 'mp'
    conn = pymysql.connect(host, user, password, database, charset='utf8',
                           port=port)
    return conn


if __name__ == '__main__':
    con = get_db_con()
    sql = 'select * from tbl_user_info'
    cursor = con.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print(len(result))
    print(result)

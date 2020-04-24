import pymysql


def get_con():
    host = "47.98.49.140"
    port = 3306
    user = "root"
    password = "123456"
    database = "mp"
    charset = "utf8"
    return pymysql.connect(host=host, port=port,
                           user=user, password=password,
                           database=database, charset=charset)


conn = get_con()
cursor = conn.cursor()
cursor.execute("select * from tbl_role")
role_list = cursor.fetchone()
print(type(role_list))

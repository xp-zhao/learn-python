import data.db as db
from data.user import User

con = db.get_db_con()
sql = 'select * from tbl_user_info'
# result = pd.read_sql(sql, con)
cursor = con.cursor()
cursor.execute(sql)
print(cursor.description)
result = cursor.fetchall()
for i in filter(lambda x: x[1] == 'xp', result):
    print(i)


def f(x):
    return User(x[0], x[1], x[2], x[3])


r = map(f, result)
print(list(r))

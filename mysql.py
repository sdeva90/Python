import pymysql
# import config
connection=pymysql.connect(
    host='localhost',user='sdeva',passwd='sandy90-',db='py_work')
cursor=connection.cursor()

sql=('select * from country')
cursor.execute(sql)
data=cursor.fetchall()
print(data)

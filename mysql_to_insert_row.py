import pymysql
# import config
connection=pymysql.connect(
    host='localhost',user='sdeva',passwd='sandy90-',db='py_work')
cursor=connection.cursor()

sql=("insert INTO country (id, state, country, population) VALUES ('%d', '%s', '%s', '%d')" % (5, 'syn', 'aus', 1324))

cursor.execute(sql)
connection.commit()
data=cursor.fetchall()
print(data)
print(sql)

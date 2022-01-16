import pymysql as MYSQL
def connectionPooling():
    db=MYSQL.connect(host='localhost',port=3306,user='root',passwd='Pratik@123',db='learning')
    cmd=db.cursor()
    return db,cmd
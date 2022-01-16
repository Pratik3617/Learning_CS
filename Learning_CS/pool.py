import pymysql as MYSQL
def connectionPooling():
    db=MYSQL.connect(host='ec2-34-230-198-12.compute-1.amazonaws.com',port=5432,user='dhaiducohaslbx',passwd='9942775b2b7ed53767e511bf6fb8eedfb3b75f0f888ee1fac5f8f9fe3a7ed4dc',db='d20lptt31kgtp1')
    cmd=db.cursor()
    return db,cmd

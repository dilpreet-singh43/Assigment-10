#1.
 import pymysql as py

db=py.connect("localhost","root","456","book")
cursor=db.cursor()
qr='create table book(book_id int,title_id int,location char(20),genre char(20))'
cursor.execute(qr)
qr='create table Titles(title_id int,title char(10),ISBN int,publisher char(20),publisher_id int)'
cursor.execute(qr)
qr='create table Publishers(publisher_id int, name char(20),streetadd varchar(20),suite_num int,zipcode_id int)'
cursor.execute(qr)
qr='create table Zipcodes(zipcode_id int,city char(20),state char(20),zipcode int)'
cursor.execute(qr)
qr='create table Authertitle(auther_title_id int,auther_id int,title_id int)'
cursor.execute(qr)
qr='create table Authers(auther_id int,first_name char(20),middle_name char(20),last_name char(20))'
cursor.execute(qr)






#2.
import pymysql as py

db=py.connect("localhost","root","123","book")
cursor=db.cursor()
qr= 'insert into book values(1,23,"dfg","fee")'
try:
    cursor.execute(qr)
    db.commit()
except:
    db.rollback()

qr= 'insert into Titles values(1,"dfg",23,"fee",456)'
try:
    cursor.execute(qr)
    db.commit()
except:
    db.rollback()
qr= 'insert into Publishers values(1,"dfg","fee23",456,678)'
try:
    cursor.execute(qr)
    db.commit()
except:
    db.rollback()


qr= 'insert into Zipcodes values(1,"dfg","fee23",456)'
try:
    cursor.execute(qr)
    db.commit()
except:
    db.rollback()

qr= 'insert into Authertitle values(1,23,456)'
try:
    cursor.execute(qr)
    db.commit()
except:
    db.rollback()

qr= 'insert into Authers values(1,"abc","dfg","ser")'
try:
    cursor.execute(qr)
    db.commit()
except:
    db.rollback()

db.close







#3.
import pymysql as py

db=py.connect("localhost","root","123","book")
cursor=db.cursor()

qr= 'update book set book_id=4 where title_id= 23'
try:
    cursor.execute(qr)
    db.commit()
except:
    db.rollback()

qr='select * from book'
cursor.execute(qr)
result=cursor.fetchall()
for r in result:
    print(r)
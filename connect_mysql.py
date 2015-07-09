# -*- coding: utf-8 -*-
import MySQLdb #Á¬½Ó   


if __name__ == '__main__':
    try:
        conn = MySQLdb.connect(host="localhost",user="root",passwd="root",db="zmh",charset="utf8")
        cursor = conn.cursor()
        sql = "insert into studentin(student_id,student_name) values(%s,%s)"   
        param = ("10000","zmh")    
        n = cursor.execute(sql,param)
        print(n)	   
    except:
        print("Could not connect to MySQL server.")
        exit( 0 )
	   
	   
	   
	   
	   

"""
exercise: The local time is written to the file every two seconds and the serial number is displayed, and the next time the program runs,
it continues to write from the last serial number.
"""
# import time
# with open('localTime.txt', 'a+') as file:  # 'a+': Append and readable mode
#     while True:
#         file.seek(0, 0)  # Move File Offset Location
#         flag = len(file.readlines()) + 1
#         localTime = time.ctime()
#         file.write(f'{flag}.{localTime}\n')
#         time.sleep(2)


import pymysql
args = {
    'host': '192.168.93.128',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'database': 'stu',
    'charset': 'utf8'
}

# first. connect database
db = pymysql.connect(**args)
# second. bjects that manipulate database data to get results
cur = db.cursor()
# third. use cursor to manipulate database
try:
    # sql = "insert into class (cid, caption) values (4, 'IMBA');"
    # sql = "update teacher set tname = '%s' where tid = 1;" %name  # '' must be written, if there is no '' then there is no '' in the SQL statement
    # cur.execute(sql)
    # data = [
    #     ('Dave', 'male', 4),
    #     ('Elk', 'female', 2)
    # ]
    # sql = "insert into student (sname, gender, class_id) values (%s, %s, %s);"
    """
        The list contains tuples, each tuple is used to pass parameters to the sql statement, and several tuples are written as many times as there are
    """
    # cur.executemany(sql, data)  # Batch Write

except Exception as e:
    print(e)
    db.rollback()  # Rollback if there is an exception to modify the data table
"""
    the engin of class table is InnoDB, InnoDB support transactions, pymysql perform write operations will automatically open the transaction,
    the last must commit to modify the data table, otherwise it will automatically rollback(No data update, Abandonment of modifications).
"""
db.commit()
# fourth. close cursor and database
cur.close()
db.close()
import pymysql


def get_connection():
    conne = pymysql.connect(
        user='root',
        password='Akshay@123',
        host='localhost',

        port=3360,
    )


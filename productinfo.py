
#PRODUCTSERVICE --> DATABASE MADHE --*
#COMMIT --> RQEUIRES --> DELETE/INSERT/UPDATE --> DATABASE MADHE CHANGES
#GET / GETALL --> NO COMMIT REQUIRED


#CONNECTION --> ACK
#CURSOR --> COMMUNICATION CHANNEL --. SQL QURIES RUN --. SQL - DATABASE LANG -->


#MYSQL --> 3306  ---> ORACLE -- 1521 ---> POSTGRES -- 5432 --->

CREATE_TABLE ='''
            create table prod_info(
            pro_id int,
            proud_name varchar(30),
            prod_prise float,
            prod_qty int,
            prod_ven varchar(30),
            primary key(prod_id)
            )
'''
INSERT_QUERY="insert into prof_info values({},{},{},{},{},{})"
UPDATE_QUERY="update prod_info set prod_name='{}',prod_qty={}, prod_price{},prod_ven'{}' where prod_id={}"
DELETE_QUERY="delete * from prod_info where prod_id={}"
GET_PRODUCT="select * from prod_info where prod_id = {}"
GET_ALL_PRODUCT="select * from prod_info"


class Product:
    def __init__(self, pid, pnm, prc, pqty, pven):
        self.prodQty = pqty
        self.prodVendor = pven
        self.prodId = pid
        self.prodName = pnm
        self.prodPrice = prc


    def __repr__(self):
        return str(self)
    def __str__(self):
        return f'''\n {self.__dict__}'''

def add_product(prod):
    FINAL_QUERY = INSERT_QUERY.format(prod.prodId, prod.prodName, prod.prodQty, prod.prodPrice, prod.prodVendor)
    conn = get_connection()  # ack with db--> mysql db - connection -
    cursor = conn.cursor()  # cursor thru -- #platform --> on which we can execute -- sql -->-- communication channel -sql run
    cursor.execute(FINAL_QUERY)
    conn.commit()  # database final kar -->

def delete_product():
    pass

def update_product():
    pass

def get_product(pid):
    conn=get_connection()
    cursor=conn.cursor()
    FINAL_QUERY = GET_PRODUCT.format(pid)
    cursor.execute(FINAL_QUERY)
    print(cursor.fetchone())

def get_all_products():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute(GET_ALL_PRODUCT)
    print(cursor.fetchall())



import pymysql
def get_connection():
    conne=pymysql.connect(
        user='root',
        password='Akshay@123',
        host='localhost',
        database='akshay',
        port=3360,
    )
    return conne

def get_product_input():
    pid= int(input('Enter Product Id:'))
    pqty = int(input('Enter Product Qty : '))
    pnm = input('Enter Product Name : ')
    prc = float(input('Enter Product Price :'))
    pven = input('Enter Product Vendor : ')
    prod = Product (pid,pnm,prc,pqty,pven)
    return prod



if __name__ == '__main__':
    get_product(771)
   # get_all_products()
    # prod  = get_product_input()
    # add_product(prod)












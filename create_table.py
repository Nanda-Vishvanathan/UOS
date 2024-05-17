import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def create_table_customers(cursor):
    logger.info("Create customers Table!")
    cursor.execute("CREATE TABLE IF NOT EXISTS customers (\
        customer_id INT PRIMARY KEY,\
        firstname VARCHAR(255),\
        surname VARCHAR(255),\
        email VARCHAR(255),\
        address VARCHAR(255),\
        zip_code VARCHAR(20),\
        region VARCHAR(255),\
        status VARCHAR(30)\
    )")
    logger.info("Customers Table created successfully!")


def create_table_orders(cursor):
    logger.info("Creating Orders Table!")
    cursor.execute("CREATE TABLE IF NOT EXISTS orders (\
        order_id INT PRIMARY KEY,\
        date VARCHAR(255),\
        customer_id INT,\
        amount FLOAT,\
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id)\
    )")
    logger.info("Orders Table created")
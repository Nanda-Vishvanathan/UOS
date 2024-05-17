import logging
import boto3
import pandas as pd


logger = logging.getLogger()
logger.setLevel(logging.INFO)


def insert_data_customers(connection, cursor, bucket_name, file_key, table):
    s3 = boto3.client('s3', region_name='us-east-1')
    # Fetching the file contents from S3 directly.
    response = s3.get_object(Bucket=bucket_name, Key=file_key)
    # Reading csv file contents from the response
    data = pd.read_csv(response['Body'])
    # Printing the Data
    logger.info("Data details::", data)

    # Iterating over each row in the dataframe and inserting into the table
    for _, row in data.iterrows():
        sql = f"INSERT INTO {table} (customer_id, firstname, surname, email, address, zip_code, region, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (
            row['customer_id'],
            row['firstname'],
            row['surname'],
            row['email'],
            row['address'],
            row['zip_code'],
            row['region'],
            row['status']
        )
        cursor.execute(sql, values)
        connection.commit()
    logger.info("Customer data inserted & committed into the DB!")


def insert_data_orders(connection, cursor, bucket_name, file_key, table_name):
    logger.info("Creating orders data!")
    s3 = boto3.client('s3', region_name='us-east-1')
    # Fetching the file contents from S3 directly.
    response = s3.get_object(Bucket=bucket_name, Key=file_key)
    # Reading csv file contents from the response
    data = pd.read_csv(response['Body'])
    # Iterate over each row in the dataframe and inserting into the table
    for _, row in data.iterrows():
        sql = f"INSERT INTO {table_name} (order_id,date,customer_id, amount) VALUES (%s, %s, %s, %s)"
        values = (
            row['order_id'],
            row['date'],
            row['customer_id'],
            row['amount'],
        )
        cursor.execute(sql, values)
        connection.commit()
    logger.info("Orders data inserted & committed into the DB!")

import json
import mysql.connector
import boto3
import logging
import create_table
import insert_table


logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    try:
        logger.info("Establishing Connection to uos db")
        ssm_client = boto3.client('ssm')
        db_host = ssm_client.get_parameter(
            Name='uos_db_host', WithDecryption=True)['Parameter']['Value']
        db_name = ssm_client.get_parameter(
            Name='uos_db_name', WithDecryption=True)['Parameter']['Value']
        db_password = ssm_client.get_parameter(
            Name='uos_rds_password', WithDecryption=True)['Parameter']['Value']
        db_username = ssm_client.get_parameter(
            Name='uos_rds_username', WithDecryption=True)['Parameter']['Value']
        connection = mysql.connector.connect(
                    host=db_host,
                    user=db_username,
                    password=db_password,
                    database=db_name)
        cursor = connection.cursor()
        logger.info("Connection Established to uos db!")

        # Creating tables:
        create_table.create_table_customers(cursor)
        create_table.create_table_orders(cursor)
        # Inserting records:
        insert_table.insert_data_customers(connection, cursor, "uos-files-d", "customers.csv", "customers")
        insert_table.insert_data_orders(connection, cursor, "uos-files-d", "orders.csv", "orders")

        cursor.close
        connection.close()
        logger.info("DB Connection closed!")
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'DB set up successfully!'})
        }
    except mysql.connector.Error as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Database error.', 'Error': str(e)})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Server error.', 'Error': str(e)})
        }

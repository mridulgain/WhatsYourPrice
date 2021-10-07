import os
import psycopg2
from psycopg2 import Error
import time

DATABASE_URL = os.environ['DATABASE_URL']

def record_price(p):
    try:
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        # Create a cursor to perform database operations
        cursor = conn.cursor()
        # # Print PostgreSQL details
        # print("PostgreSQL server information")
        # print(conn.get_dsn_parameters(), "\n")
        # # Executing a SQL query
        # cursor.execute("SELECT version();")
        # # Fetch result
        # record = cursor.fetchone()
        # print("You are connected to - ", record, "\n")
        # create table
        # query = ''' 
        #     CREATE TABLE price (
        #         id VARCHAR(100) PRIMARY KEY,
        #         price VARCHAR(10)
        #     )
        #     '''
        # cursor.execute(query)
        # print("Table created")
        # insert data
        postgres_insert_query = """ INSERT INTO price (id, price) VALUES (%s,%s)"""
        record_to_insert = p
        cursor.execute(postgres_insert_query, record_to_insert)

        conn.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into roles table")
    finally:
        if (conn):
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")


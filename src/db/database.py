import psycopg2
from dotenv import load_dotenv
from psycopg2 import sql, Error
from datetime import datetime
import os


load_dotenv()

load_dotenv()

class Database:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                database=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT")
            )
            self.conn.autocommit = True
            self.cursor = self.conn.cursor()  
            print("Connected to PostgreSQL:", os.getenv("DB_NAME"))
        except Error as e:
            print("Error while connecting to PostgreSQL:", e)
            self.conn = None
            self.cursor = None  

    def insert_query(self, table_name: str, data: dict):
        if not self.cursor: 
            raise Exception("Database connection not initialized")

        try:
            columns = data.keys()
            values = [data[col] for col in columns]

            query = f"""
            INSERT INTO {table_name} ({", ".join(columns)})
            VALUES ({", ".join(["%s"] * len(values))})
            RETURNING *;
            """

            self.cursor.execute(query, values)
            return self.cursor.fetchone()
        except Error as e:
            print(f"Insert error: {e}")
            return None

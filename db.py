import psycopg2 
import os

def get_connection():
    conn = psycopg2.connect(
        host= os.getenv("DB_HOST"),
        database= "postgres",
        user= os.getenv("DB_USER")
    )
    return conn

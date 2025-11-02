import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os

# load_dotenv(). # Only required when deploying locally and not in cluster

DATABASE_URL = os.getenv("DATABASE_URL")

def get_db_connection():
    if not DATABASE_URL:
        raise ValueError("DATABASE_URL environment variable is not set")
    return psycopg2.connect(DATABASE_URL)
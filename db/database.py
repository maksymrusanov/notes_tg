import os

import psycopg
from dotenv import load_dotenv

load_dotenv()


def create_connection():
    try:
        conn = psycopg.connect(
            host=os.getenv("POSTGRES_HOST"),
            port=os.getenv("POSTGRES_PORT"),
            dbname=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
        )
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        raise e
    return conn


async def change_note_status(note_id: int, new_status: str):
    conn = create_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                UPDATE notes SET status = %s WHERE id = %s;
                """,
                (new_status, note_id),
            )
    conn.close()


async def create_table():
    conn = create_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS notes (
                    id SERIAL PRIMARY KEY,
                    user_id INTEGER,
                    name TEXT,
                    status TEXT,
                    description TEXT);
                """)
    conn.close()


async def add_note(user_id: int, name: str, description: str, status="In progress"):
    conn = create_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO notes (user_id,name,status, description) VALUES (%s,%s,%s,%s);
                """,
                (user_id, name, status, description),
            )
    conn.close()


async def get_notes(status: str):
    conn = create_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT id,name,description,status FROM notes WHERE status = %s ;
                """,
                (status,),
            )
            notes = cur.fetchall()
    conn.close()
    return notes


async def change_note_status(note_id: int, new_status: str):
    conn = create_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                UPDATE notes SET status = %s WHERE id = %s;
                """,
                (new_status, note_id),
            )
    conn.close()


async def get_all_notes():
    conn = create_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT id,name,description,status FROM notes WHERE status not IN ('Deleted');
                """,
            )
            notes = cur.fetchall()
    conn.close()
    return notes


async def delete_note(note_id: int):
    conn = create_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                DELETE FROM notes WHERE id = %s;
                """,
                (note_id,),
            )
    conn.close()

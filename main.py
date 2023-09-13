import psycopg2
import os
from datetime import datetime
from typing import List


def dump_passwords() -> List:
    query = """SELECT * FROM passwords"""
    try:
        conn = psycopg2.connect(
            database="passwords",
            host="localhost",
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            port="5432",
        )

        cursor = conn.cursor()
        cursor.execute(query)

        passwords = cursor.fetchall()

        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return passwords


def add_password(name: str, password: str, username="") -> None:
    query = """INSERT INTO passwords(name, username, password, created_on) VALUES(%s, %s, %s, %s)"""
    try:
        conn = psycopg2.connect(
            database="passwords",
            host="localhost",
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            port="5432",
        )

        cursor = conn.cursor()
        cursor.execute(query, (name, username, password, datetime.now()))

        conn.commit()

        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def main():
    add_password("https://www.youtube.com", "qwerty", "Paul")
    passwords = dump_passwords()

    for password in passwords:
        print(password)


if __name__ == "__main__":
    main()

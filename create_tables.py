import psycopg2
from config import load_config

def create_tables():
    """ Create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE users (
            user_id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            surname VARCHAR(255),
            creation_date DATE NOT NULL DEFAULT CURRENT_DATE,
            birthday DATE,
            email VARCHAR(100),
            phone VARCHAR(20)
        )
        """,
        """ CREATE TABLE members (
                member_id SERIAL PRIMARY KEY,
                creation_date DATE NOT NULL DEFAULT CURRENT_DATE,
                FOREIGN KEY (user_id)
                REFERENCES users (user_id)
                ON UPDATE RESTRICT
                FOREIGN KEY (role_id)
                REFERENCES roles (role_id)
                )
                FOREIGN KEY (store_id)
                REFERENCES stores (store_id)
                ON UPDATE RESTRICT
        """,
        """
        CREATE TABLE roles (
                role_id SERIAL PRIMARY KEY,
                title VARCHAR(255) NOT NULL
        )
        """,
        """
        CREATE TABLE stores (
                store_id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                creation_date DATE NOT NULL DEFAULT CURRENT_DATE
                address VARCAHR(255),
                FOREIGN KEY (subscription_id)
                REFERENCES subscriptions (subscription_id),
        )
        """,
        """
        CREATE TABLE COURSES (
            course_id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            description TEXT NOT NULL,
            creation_date DATE NOT NULL DEFAULT CURRENT_DATE
            FOREIGN_KEY (store_id)
            REFERENCES stores (store_id)
        )
        """)
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_tables()
import psycopg2
from config import load_config

def create_tables():
    """ Create tables in the PostgreSQL database"""

    commands = ("""
        CREATE TABLE if not exists users (
            user_id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            surname VARCHAR(255),
            creation_date DATE NOT NULL DEFAULT CURRENT_DATE,
            birthday DATE,
            email VARCHAR(100),
            phone VARCHAR(20)
        );
        """, 
        """
        CREATE TABLE if not exists roles (
            role_id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL
        );
        """,
        """
        CREATE TABLE if not exists subscriptions(
            subscription_id SERIAL PRIMARY KEY,
            type varchar(40),
            price numeric(10,2),
            start_date DATE NOT NULL DEFAULT CURRENT_DATE,
            recurring boolean,
            next_payment_date date 
        );
        """,
        """
        CREATE TABLE if not exists stores (
            store_id SERIAL PRIMARY KEY,
            subscription_id int,
            name VARCHAR(255) NOT NULL,
            creation_date DATE NOT NULL DEFAULT CURRENT_DATE,
            address VARChaR(255),
            FOREIGN KEY(subscription_id)
            REFERENCES subscriptions(subscription_id)
        );
        """,
        """ 
        CREATE TABLE if not exists members (
            member_id SERIAL PRIMARY KEY,
            creation_date DATE NOT NULL DEFAULT CURRENT_DATE,
            user_id int,
            role_id int,
            store_id int,
            FOREIGN KEY(user_id)
                REFERENCES users(user_id)
                ON UPDATE RESTRICT,
            FOREIGN KEY(role_id)
            REFERENCES roles(role_id),
            FOREIGN KEY(store_id)
                REFERENCES stores(store_id)
                ON UPDATE RESTRICT
        );
        """,
        """
        CREATE TABLE if not exists courses (
            course_id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            description TEXT NOT NULL,
            creation_date DATE NOT NULL DEFAULT CURRENT_DATE,
            store_id int,
            FOREIGN KEY (store_id)
                REFERENCES stores (store_id)
        );
    """
    )
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


def delete_all_tables():
    """ Deletes Table for testing purposes """
    commands = (
    """
        drop table if exists users, roles, subscriptions, stores, members, courses;
    """,
    )
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
    # delete_all_tables()
    create_tables()

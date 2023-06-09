import sqlite3

# First example
instructions = ["""\
    CREATE TABLE if not exists person(
        id integer PRIMARY KEY AUTOINCREMENT,
        name varchar,
        email varchar UNIQUE NOT NULL,
        dept varchar,
        role varchar
    );
    """,
    """\
    CREATE TABLE if not exists balance (
        id integer PRIMARY KEY AUTOINCREMENT,
        person interger UNIQUE NOT NULL,
        value integer NOT NULL,
        FOREIGN KEY(person) REFERENCES person(id)
    );
    """
    ]

con = sqlite3.connect("files/3_sql_e_sqlite.db")
con.execute("PRAGMA foreign_keys = ON;")
for instruction in instructions:
    con.execute(instruction)
con.commit()
con.close()


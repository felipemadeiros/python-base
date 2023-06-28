from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship


Base = declarative_base()

class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255))

class Balance(Base):
    __tablename__ = "balance"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    value = Column(Integer, nullable=False)
    person_id = Column(Integer, ForeignKey(Person.id))
    person = relationship('Person', foreign_keys='Balance.person_id')

engine = create_engine("sqlite:///files/4_sql_alchemy.db")

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

session = SessionLocal()

# person = Person(name="Felipe")
# session.add(person) # INSERT INTO person (NAME) VALUES ('Felipe');

# person = Person(name="Luciane")
# session.add(person) # INSERT INTO person (NAME) VALUES ('Luciane');

# session.commit()

# rows = session.query(Person).filter(Person.name == "Felipe")
# for row in rows:
#     # print(row.id, row.name)
#     balance = Balance(value=40, person_id=row.id)
#     session.add(balance)

# session.commit()

rows = session.query(Balance)
for row in rows:
    print(row.value, row.person.name)

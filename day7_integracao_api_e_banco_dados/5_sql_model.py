from typing import Optional
from sqlmodel import SQLModel, Field, create_engine, Session, select, Relationship


class Person(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    balance: "Balance" = Relationship(back_populates="person")

class Balance(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    value: int
    person_id: int = Field(foreign_key="person.id")

    person: Person = Relationship(back_populates="balance")


engine = create_engine("sqlite:///files/5_sql_model.db", echo=False)
SQLModel.metadata.create_all(bind=engine)

with Session(engine) as session:
    # person = Person(name="Felipe")
    # session.add(person)

    # session.commit()

    # sql = select(Person)
    # # sql = select(Person).where(Person.name == "Felipe")
    # rows = session.exec(sql)
    # # for person in rows:
    # #     balance = Balance(value=60, person=person)
    # #     session.add(balance)
    # # session.commit()

    sql = select(Person)
    rows = session.exec(sql)
    for person in rows:
        print(person.name, person.balance)
        print(person.name, person.balance[0].value)

    sql = select(Balance)
    rows = session.exec(sql)
    for balance in rows:
        print(balance.person, balance.value)
        print(balance.person.name, balance.value)

    sql = select(Person, Balance).where(Balance.person_id == Person.id)
    rows = session.exec(sql)
    for person, balance in rows:
        print(person.name, balance.value)

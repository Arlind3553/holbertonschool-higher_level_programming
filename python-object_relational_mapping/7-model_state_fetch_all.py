#!/usr/bin/python3
"""
List all states from the database hbtn_0e_0_usa
"""


from SQLAlchemy.orm import Session
from sys import argv
from model_state import Base, State
from SQLAlchemy import create_engine

if __name__ == '__main__':
    eng = create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}")
    Base.metadata.create_all(eng)
    session = Session(eng)
    q = session.query(State).all()
    for row in q:
        print(f"{row.id}: {row.state}")
    session.close()

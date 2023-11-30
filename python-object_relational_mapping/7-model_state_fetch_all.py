#!/usr/bin/python3
"""
List all states from the database hbtn_0e_0_usa
"""


from SQLAlchemy.orm import Session
from sys import argv
from model_state import Base, State
from SQLAlchemy import create_engine

if __name__ == '__main__':
    db = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3])
    eng = create_engine(db)
    Base.metadata.create_all(eng)
    session = Session(eng)
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")
    session.close()

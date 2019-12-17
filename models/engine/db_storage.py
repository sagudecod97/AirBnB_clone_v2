#!/usr/bin/python3
""" This is the engine to the DB storage"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from os import environ


class DBStorage:
    """ Class to manage the storage in th DataBase
        Args:
        __engine(str): The engine
        __session(str): The session    
    """
    __engine = None
    __session = None

    def __init___(self):
        user = environ.get('HBNB_MYSQL_USER')
        pwd = environ.get('HBNB_MYSQL_PWD')
        hst = environ.get('HBNB_MYSQL_HOST')
        db = environ.get('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.
            format(user, pwd, hst, db), pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        session = Session()
        hbnb_env = environ.get('HBNB_ENV')
        if hbnb_env == 'test':
            txt = text("DROP ALL tables;")
            


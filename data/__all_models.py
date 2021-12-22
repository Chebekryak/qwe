from sqlalchemy import Column, Integer, Text, String, Boolean, ForeignKey
from.db_session import SqlAlchemyBase


class Question(SqlAlchemyBase):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_class = Column(Integer, ForeignKey('classes.id'))
    text = Column(Text)
    image = Column(String)
    points = Column(Integer)


class Class(SqlAlchemyBase):
    __tablename__ = "classes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(String)


class Answer(SqlAlchemyBase):
    __tablename__ = "answers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_question = Column(Integer, ForeignKey('questions.id'))
    body = Column(String)
    status = Column(Boolean)
from sqlalchemy import (create_engine, Column, Integer, String)
from sqlalchemy.orm import DeclarativeBase,scoped_session, sessionmaker


engine = create_engine('sqlite:///cadastro.db')
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

#Base = DeclarativeBase()
class Base(DeclarativeBase):
    pass

Base.query = db_session.query_property()

class Pessoas(Base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    idade = Column(Integer)

    def __repr__(self):
        return f'<Pessoa {self.nome}>'
  
    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()



def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()

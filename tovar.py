from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# Base = declarative_base()
engine = create_engine ('postgresql+psycopg2://postgres:example@localhost/MAGaz')
print('imported')
Base = declarative_base()
# создаем таблицы



class Tovar(Base):
    __tablename__ = "tovar"
    id = Column(Integer, primary_key=True)
    title = Column(String(30))
    cost = Column(Float)
    # addresses = relationship(
    #     "Address", back_populates="user", cascade="all, delete-orphan"
    # )
    def __repr__(self):
        return f"Tovar(id={self.id!r}, title={self.title!r}, cost={self.cost!r})"
    


Base.metadata.create_all(bind=engine)



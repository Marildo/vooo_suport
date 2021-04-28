from sqlalchemy import Column, String, TIMESTAMP
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Client(Base):
    __tablename__ = 'Client'
    id = Column(INTEGER(unsigned=True), primary_key=True)
    id_address = Column(INTEGER(unsigned=True))
    id_contact = Column(INTEGER(unsigned=True))
    name = Column(String(255), nullable=False)
    trading = Column(String(255), nullable=False)
    brand = Column(String(255), nullable=False)
    status = Column(TINYINT, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)

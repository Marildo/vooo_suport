from sqlalchemy import  Column, String, TIMESTAMP, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, TINYINT,DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

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
    id_document = Column(INTEGER(unsigned=True), ForeignKey('document.id'), nullable=False)
    document = relationship('Document')
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)



class Document(Base):
    __tablename__ = 'document'
    id = Column(INTEGER(unsigned=True), primary_key=True)
    type = Column(String(10), nullable=False)
    number = Column(DECIMAL(20), nullable=False)



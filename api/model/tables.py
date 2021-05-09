from sqlalchemy import Column, String, TIMESTAMP, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, TINYINT, DECIMAL, DATETIME
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
    id_aggregator = Column(INTEGER(unsigned=True), ForeignKey('aggregator.id'))
    aggregator = relationship('Aggregator')
    headquarter_id = Column(INTEGER(unsigned=True))
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)


class Document(Base):
    __tablename__ = 'document'
    id = Column(INTEGER(unsigned=True), primary_key=True)
    type = Column(String(10), nullable=False)
    number = Column(DECIMAL(20), nullable=False)


class Aggregator(Base):
    __tablename__ = 'aggregator'
    id = Column(INTEGER(unsigned=True), primary_key=True)
    name = Column(String(255), nullable=False)


class ClientConnector(Base):
    __tablename__ = 'client_connector'
    client_id = Column(INTEGER(unsigned=True), primary_key=True)
    connector_id = Column(INTEGER(unsigned=True), primary_key=True)
    contract_code = Column(DECIMAL(15), nullable=False)


class Connector(Base):
    __tablename__ = 'connector'
    connector_id = Column(INTEGER(unsigned=True), primary_key=True)
    connector_type_id = Column(INTEGER(unsigned=True),ForeignKey('connector_type.connector_type_id'), nullable=False)
    provider_id = Column(INTEGER(unsigned=True), nullable=False)
    name = Column(String(75), nullable=False)
    description = Column(String(150))
    periodicity = Column(String(1), nullable=False)
    periodicity_last_datetime = Column(DATETIME)
    external_code_id = Column(INTEGER(unsigned=True))
    periodicity_week_day = Column(DECIMAL(1, 0))
    working_days = Column(DECIMAL(1, 0))
    type = relationship('ConnectorType', enable_typechecks=False)


class ConnectorType(Base):
    __tablename__ = 'connector_type'
    connector_type_id = Column(INTEGER(unsigned=True), primary_key=True)
    name = Column(String(75), nullable=False)
    description = Column(String(150))

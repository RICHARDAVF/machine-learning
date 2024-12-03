from sqlalchemy import Column, Integer, String, Float, ForeignKey,UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Model = declarative_base()

class Entity(Model):
    __tablename__ = "table_entity"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    type_entity = Column(Integer, nullable=False)
    datos = relationship("Datos", back_populates="entity_name")
    def __repr__(self):
        return f"Entity(id={self.id},name={self.name},type_entity={self.type_entity})"

class Variable(Model):
    __tablename__ = "table_variable"
    id = Column(Integer, primary_key=True)
    name_header = Column(String(255), nullable=False)
    name_children = Column(String(255), nullable=False)
    datos = relationship("Datos", back_populates="variable")
    def __repr__(self):
        return f"Variable(id={self.id},name_header={self.name_header},name_children={self.name_children})"
class Dates(Model):
    __tablename__ = "table_dates"
    id = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False)
    month = Column(String(20), nullable=False)
    month_prefix = Column(String(2), nullable=False)
    datos = relationship("Datos", back_populates="date")
    def __repr__(self):
        return f"Dates(id={self.id},year={self.year},month={self.month},mont_prefix={self.month_prefix})"
class Datos(Model):
    __tablename__ = "table_datos"
    id = Column(Integer, primary_key=True)
    entity_id = Column(Integer, ForeignKey("table_entity.id"))
    variable_id = Column(Integer, ForeignKey("table_variable.id"))
    date_id = Column(Integer, ForeignKey("table_dates.id"))
    value = Column(Float, nullable=False)
    entity_name = relationship("Entity", back_populates="datos")
    variable = relationship("Variable", back_populates="datos")
    date = relationship("Dates", back_populates="datos")

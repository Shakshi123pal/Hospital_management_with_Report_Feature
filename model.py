from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table, null
from database import Base


class link(Base):
    __tablename__ = "link"
    doctors_id = Column(ForeignKey('doctors.id'), primary_key=True)
    patient_id = Column(ForeignKey('patients.id'), primary_key=True)


class Patients(Base):
    __tablename__ = "patients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    disease = Column(String)
    room_id = Column(Integer)
    doctor = relationship("Doctors", back_populates="patient", secondary="link")


class Doctors(Base):
    __tablename__ = "doctors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    specialization = Column(String)
    patient = relationship("Patients", back_populates="doctor", secondary="link")


class Admin(Base):
    __tablename__ = "admin"
    username = Column(String, primary_key=True, index=True)
    hashed_pass = Column(String, index=True)



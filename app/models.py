from .database import Base 
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, Float, Date,func



class Medicine(Base):
    __tablename__='medicine'
    
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String, nullable=False, index=True)
    brand = Column(String,nullable=True)
    generic_name = Column(String, nullable=True, index=True)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False, default=0)
    expiry_date = Column(Date, nullable=True)
    category = Column(String, nullable=True)
    prescription_required = Column(Boolean, default=False)
    dosage = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True)),
    updated_at = Column(TIMESTAMP(timezone=True),
                        server_default=func.now(),
                        onupdate=func.now())
    
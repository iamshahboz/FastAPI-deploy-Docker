from pydantic import BaseModel
from typing import Optional 
from datetime import datetime, date 


class MedicineBase(BaseModel):
    name: str 
    brand: Optional[str] = None 
    generic_name: Optional[str] = None 
    description: Optional[str] = None 
    price: float 
    stock: int 
    expiry_date: Optional[date] = None 
    category: Optional[str] = None 
    prescription_required: bool = False 
    dosage: Optional[str] = None  

class MedicineCreate(MedicineBase):
    pass 


class MedicineUpdate(BaseModel):
    name: Optional[str] = None
    brand: Optional[str] = None
    generic_name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None
    expiry_date: Optional[date] = None
    category: Optional[str] = None
    prescription_required: Optional[bool] = None
    dosage: Optional[str] = None
    
    
    
class MedicineRead(MedicineBase):
    id: int
    created_at: datetime 
    updated_at: datetime 


    class Config:
        orm_mode = True  
    
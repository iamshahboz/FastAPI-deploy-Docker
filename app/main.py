from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import models
from . import schemas
from .database import get_db, engine
from typing import List 

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# create a medicine 
@app.post('/medicine', response_model=schemas.MedicineRead)
def create_medicine(medicine: schemas.MedicineCreate, db: Session=Depends(get_db)):
    existing_medicine = db.query(models.Medicine).filter(models.Medicine.name == medicine.name).first()
    if existing_medicine:
        raise HTTPException(status_code=400, detail='Medicine with this name already exists')
    
    new_medicine = models.Medicine(**medicine.model_dump())
    db.add(new_medicine)
    db.commit()
    db.refresh()
    return new_medicine 

# get all medicines 
@app.get('medicine', response_model=List[schemas.MedicineRead])
def get_all_medicines(db: Session = Depends(get_db)):
    medicines = db.query(models.Medicine).all()
    return medicines 


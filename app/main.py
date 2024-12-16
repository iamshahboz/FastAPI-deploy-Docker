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
    db.refresh(new_medicine)
    return new_medicine 

# get all medicines 
@app.get('/medicine', response_model=List[schemas.MedicineRead])
def get_all_medicines(db: Session = Depends(get_db)):
    medicines = db.query(models.Medicine).all()
    return medicines


# UPDATE: Update a medicine by ID
@app.put("/medicines/{medicine_id}", response_model=schemas.MedicineRead)
def update_medicine(
    medicine_id: int, medicine_data: schemas.MedicineUpdate, db: Session = Depends(get_db)
):
    medicine = db.query(models.Medicine).filter(models.Medicine.id == medicine_id).first()
    if not medicine:
        raise HTTPException(status_code=404, detail="Medicine not found.")
    
    # Update only the fields provided in the request
    for key, value in medicine_data.dict(exclude_unset=True).items():
        setattr(medicine, key, value)
    
    db.commit()
    db.refresh(medicine)
    return medicine


# DELETE: Remove a medicine by ID
@app.delete("/medicines/{medicine_id}", response_model=dict)
def delete_medicine(medicine_id: int, db: Session = Depends(get_db)):
    medicine = db.query(models.Medicine).filter(models.Medicine.id == medicine_id).first()
    if not medicine:
        raise HTTPException(status_code=404, detail="Medicine not found.")
    
    db.delete(medicine)
    db.commit()
    return {"message": f"Medicine with ID {medicine_id} has been deleted."}


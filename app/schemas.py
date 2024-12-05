from pydantic import BaseModel
import enum 

class TodoBase(BaseModel):
    title : str
    description : str | None = None


class TodoCreate(TodoBase):
    pass


class Todo(TodoBase):
    id : int
    owner_id  : int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str
    name: str


class UserCreate(UserBase):
    pass 


class User(UserBase):
    id : int
    is_active : bool
    todos : list[Todo] = []

    class Config:
        from_attributes = True
        
class TransmissionEnum(enum.Enum):
    MANUAL = 1
    AUTOMATIC = 2 
    CVT = 3 
        
        
class CarBase(BaseModel):
    name: str 
    color: str 
    transmission: TransmissionEnum = Form(...)
    image: UploadFile() = File(...)
        

    

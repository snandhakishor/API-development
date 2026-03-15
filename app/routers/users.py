from .. import model
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import CreateUser, UserOut
from ..utils import hash_password

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post('/', status_code= status.HTTP_201_CREATED, response_model=UserOut)
def create_user(user: CreateUser, db: Session = Depends(get_db)):
    # db.execute(text("INSERT INTO users (email, password) VALUES (:email, :password)"), 
                                # {"email":user.email, "password":user.password})
    # print("request received")                      
    # db.commit()
    # return {"message": "User created successfully"}
    hashed_password = hash_password(user.password)
    user.password = hashed_password
    new_user = model.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/{id}', response_model=UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    the_user = db.query(model.User).filter(model.User.id==id).first()
    if the_user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'id {id} does not exist')
    return the_user

print(type(model.User.password))
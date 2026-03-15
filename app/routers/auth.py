from sqlalchemy.orm import Session
from ..database import get_db
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from ..schemas import Token
from ..model import User
from ..utils import verify_password
from .. import oauth2
router = APIRouter(tags=["Authentication"])

@router.post('/login', response_model=Token)
def login(user_login: OAuth2PasswordRequestForm = Depends(), db:Session=Depends(get_db)):
    the_user = db.query(User).filter(User.email == user_login.username).first()
    if not the_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credentials")
    
    if not verify_password(user_login.password, the_user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
    
    access_token = oauth2.create_access_token({"user_id":the_user.id})
    return {"access_token":access_token, "token_type":"bearer"}
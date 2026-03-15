from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime
from typing import Literal
class Post(BaseModel):
    title: str
    content: str
    

class UpdatePost(Post):
    pass

class UserOut(BaseModel):
    email: EmailStr
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

class PostNext(BaseModel):
    title: str
    content: str
    votes: int

class PostandVote(BaseModel):
    post: PostNext
    owner: UserOut
    model_config = ConfigDict(from_attributes=True)

class User(BaseModel):
    email: EmailStr
    created_at: datetime
    
class PostOut(Post):
    id: int
    owner_id: int
    owner_details: UserOut
    model_config = ConfigDict(from_attributes=True)


class CreateUser(BaseModel):
    email: EmailStr
    password: str

class PostplusVote(BaseModel):
    Post: PostOut
    votes: int
    model_config = ConfigDict(from_attributes=True)

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: int

class VotePost(BaseModel):
    post_id: int
    dir: Literal[0, 1]
from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from sqlalchemy import text, func
from typing import Optional, List
from ..database import get_db
from ..schemas import Post, UpdatePost, PostOut, PostplusVote, PostandVote
from ..import model
from .. import oauth2

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)


@router.get('/')
def get_posts(db: Session = Depends(get_db), limit: int = 10, filters: Optional[str] = ""):
    # cursor.execute("SELECT * FROM posts")
    # posts = cursor.fetchall()
    # print(posts)
    posts = db.execute(text(f"""SELECT p.id, p.title, p.content, COUNT(v.post_id) AS votes 
    FROM posts p LEFT JOIN votes v ON p.id = v.post_id 
    WHERE p.title LIKE '%{filters}%' GROUP BY p.id, p.title, p.content
    ORDER BY votes DESC
    LIMIT {limit}"""))
    return posts.mappings().all()

# the order matters, if we put /posts/{id} before /posts, it will always try to match the first one and never reach the second one. So we need to put the more specific route first.

# post operation

@router.post('/', status_code= status.HTTP_201_CREATED, response_model=PostOut)
def create_posts(post: Post, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    # cursor.execute("INSERT INTO posts (title, content, published) VALUES(%s, %s, %s)",
    #                 (post.title, post.content, post.published))
    # new_post = cursor.fetchone()
    # conn.commit()
    new_post = model.Post(owner_id = user_id.id, **post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

# get posts by id
@router.get('/{id}', response_model=PostplusVote)
def recieve_posts(id: int, db: Session = Depends(get_db), user_id = Depends(oauth2.get_current_user)):
    # cursor.execute("SELECT * FROM posts WHERE id = %s", (str(id),))
    # post_ = cursor.fetchone()
    post = db.query(model.Post).filter(model.Post.id == id).first()
    if post:
        if post.owner_id != user_id.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    post_ = db.query(model.Post, func.count(model.Vote.post_id).label("votes")).join(model.Vote, 
                     model.Post.id == model.Vote.post_id, isouter=True).group_by(model.Post.id).filter(model.Post.id == id).first()
    if not post_:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f'post with id: {id} was not found')
    
    
    return post_

# @app.get('/posts/latest')
# def get_latest_post():
#     latest_post = my_posts[len(my_posts)-1]
#     return {"latest_post":latest_post}
# an error will occur for the above route because it will try to match the /posts/{id} route first and it will not find a post with id 'latest'. To fix this, we need to put the /posts/latest route before the /posts/{id} route.

# deleting post
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db:Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    # cursor.execute("DELETE FROM posts WHERE id = %s", (str(id),))
    # deleted_post = cursor.fetchone()
    # conn.commit()
    deleted_post = db.query(model.Post).filter(model.Post.id == id).first()
    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f'id {id} does not exist')
    if deleted_post.owner_id != user_id.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")
    db.delete(deleted_post)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# updating post
@router.put('/{id}')
def update_post(id: int, post: UpdatePost, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    # cursor.execute("UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s",
    #                (post.title, post.content, post.published, str(id)))

    # conn.commit()
    post_query = db.query(model.Post).filter(model.Post.id == id)
    post_ = post_query.first()
    if post_ == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'id {id} does not exist')
    if post_.owner_id != user_id.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform the action")
    post_query.update(post.model_dump(), synchronize_session=False)
    db.commit()
    return post_query.first()

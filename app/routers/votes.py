from fastapi import APIRouter, Depends, HTTPException, status
from .. import model, schemas, database, oauth2
from sqlalchemy.orm import Session
router = APIRouter(
    prefix="/vote",
    tags=["Vote"]
)

@router.post('/', status_code=status.HTTP_201_CREATED)
def vote(votes: schemas.VotePost, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    vote_user = db.query(model.Vote).filter(model.Vote.user_id == current_user.id, 
                                            model.Vote.post_id == votes.post_id)
    found_vote = vote_user.first()
    current_post = db.query(model.Post).filter(model.Post.id == votes.post_id).first()
    if not current_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    if votes.dir == 1:
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail="already voted")
        else:
            new_vote = model.Vote(post_id = votes.post_id, user_id = current_user.id)
            db.add(new_vote)
            db.commit()
            return "Vote added"
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="You haven't voted")
        else:
            db.delete(found_vote)
            db.commit()
            return "deleted"
        
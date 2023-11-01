from fastapi import APIRouter, HTTPException
from storeapi.models.post import UserPost, UserPostIn, CommentIn, Comment

router = APIRouter()


# Database
post_table = {}
comment_table = {}


def find_post(post_id: int):
    return post_table.get(post_id)


# Creating post endpoint
# Adding endpoint to create new posts
@router.post("/post", response_model=UserPost)
async def create_post(post: UserPostIn, status_code=201):
    data = post.model_dump()
    last_record_id = len(post_table)
    new_post = {**data, "id": last_record_id}
    post_table[last_record_id] = new_post
    return new_post
    # Needs to respond with the body and id = new_post


# To get a list of all the available posts
@router.get("/post", response_model=list[UserPost])
async def get_all_posts():
    return list(post_table.values())


# Adding endpoint to create new comments
@router.post("/comment", response_model=Comment)
async def create_comment(comment: CommentIn, status_code=201):
    # To make sure the post for which this comment is being created actually exist:
    post = find_post(comment.post_id)
    # if not None
    # not None = True
    # if True => the block bellow is executed
    if not post:
        raise HTTPException(status_code=404, detail="Post not found.")

    data = comment.model_dump()
    last_record_id = len(comment_table)
    new_comment = {**data, "id": last_record_id}
    comment_table[last_record_id] = new_comment
    return new_comment
    # Needs to respond with the id, post_id and body = new_comment

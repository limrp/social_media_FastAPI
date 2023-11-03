from fastapi import APIRouter, HTTPException
from storeapi.models.post import (
    UserPost,
    UserPostIn,
    CommentIn,
    Comment,
    UserPostWithComments,
)

router = APIRouter()


# Database
post_table = {}
comment_table = {}


def find_post(post_id: int):
    return post_table.get(post_id)


# Endpoint to create new posts
@router.post("/post", response_model=UserPost, status_code=201)
async def create_post(post: UserPostIn):
    data = post.model_dump()
    last_record_id = len(post_table)
    new_post = {**data, "id": last_record_id}
    post_table[last_record_id] = new_post
    return new_post
    # Needs to respond with the body and id = new_post


# Endpoint to get a list of all the available posts
@router.get("/post", response_model=list[UserPost])
async def get_all_posts():
    return list(post_table.values())


# Endpoint to create new comments
@router.post("/comment", response_model=Comment, status_code=201)
async def create_comment(comment: CommentIn):
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


# Endpoint to get all the comments on a given post
# This endpoint will receive the post's id
# and will respond with a list of comments.
@router.get("/post/{post_id}/comment", response_model=list[Comment])
async def get_comments_on_post(post_id: int):
    return [
        comment for comment in comment_table.values() if comment["post_id"] == post_id
    ]


# Endpoint to get a post with the list of comments
@router.get("/post/{post_id}", response_model=UserPostWithComments)
async def get_post_with_comments(post_id: int):
    post = find_post(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found.")
    return {
        "post": post,
        "comments": await get_comments_on_post(post_id),
    }

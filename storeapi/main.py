from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Models to validate incoming data
class UserPostIn(BaseModel):
    body: str


class UserPost(UserPostIn):
    id: int


# Database
post_table = {}


# Creating post endpoint
@app.post("/post", response_model=UserPost)
async def create_post(post: UserPostIn):
    data = post.model_dump()
    last_record_id = len(post_table)
    new_post = {**data, "id": last_record_id}
    post_table[last_record_id] = new_post
    return new_post
    # Needs to respond with the body and id = new_post


# To get a list of all the available
@app.get("/post", response_model=list[UserPost])
async def get_all_posts():
    return list(post_table.values())


# response_model=list[UserPost] means that
# we are going to respond with a list that is going to content UserPosts
# Pydantic and FastAPI are gonna make sure that
# everything that we return here will get converted to JSON correctly


# to-do
# print post_table in jn

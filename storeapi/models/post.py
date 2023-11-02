from pydantic import BaseModel


# Models to validate incoming data
class UserPostIn(BaseModel):
    body: str


class UserPost(UserPostIn):
    id: int


# Adding comments to the posts:
# The user is going to send us the post's id and the comment's body
# that's how we are going to relate comment to posts!


class CommentIn(BaseModel):
    body: str
    post_id: int


# When we respond, we are going to send them:
# 1. the commend body
# 2. the post's id that it (the comment) is related to.abs
# 3. A unique identifier for each individual comment!


class Comment(CommentIn):
    id: int
    # 3. A unique identifier for each individual comment!


# Adding a class for a UserPost together with its comments
# We are going to respond with this to the user in some endpoint
class UserPostWithComments(BaseModel):
    # 2 keys
    post: UserPost
    comments: list[Comment]


# Data structure defined by this class:
# {
#     "post": {"id": 0, "body": "My post!"},
#     "comments": [
#         {"id": 2, "post_id": 0, "body": "A comment of post 0"},
#         {"id": 3, "post_id": 1, "body": "Another comment of post 0"},
#     ],
# }

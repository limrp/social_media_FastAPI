# Course

## Section 2: Working with FastAPI

### Section 2, p10

* We add the required models
    * `UserPostIn`: That's going to have:
        * The post's body.
    * `UserPost`: That is going to have:
        * The post's **ID**.
        * The post's **body** (inherited from `UserPostIn`).

`response_model=list[UserPost]` means that we are going to respond with a list that is going to content `UserPosts`.

`Pydantic` and `FastAPI` are gonna make sure that everything that we return here will get converted to JSON correctly.

### Section 2, p13

**Topic**: Split the API (`main.py`) into files with `APIRouter`.

**Goal:** How to use an `APIRouter`

After creating `routers/post.py` and moving the **endpoints** there, we:

* imported `from fastapi import APIRouter`
* created a `router = APIRouter()` and 
* modified the decorators from `@app.post()` to `@router.post()`.

In `main.py`, we:

* deleted the **endpoints**
* deleted the `post_table` dictionary / database
* deleted the `from storeapi.models.post import UserPost, UserPostIn` import
* imported `from storeapi.routers.post import router as post_router`
* Used the `.include_router()` method, adding: `app.include_router(router=post_router)`.

With the last action, we are using the `router` that was created in `routers/post.py` and including it in the `app`.

### Section 2, p14

**Topic**: Adding comments to the social media app.

**Goal**: How to add a new feature to an API.

*Thought process* to add a new feature to an API:

1. What data does you API receive and return? 
(i.e. What data does **the user** is going to send **you** and what data are you going to send back?)
2. What data do you need to store?
3. Write the interface with the user = the endpoints.

**Answers**

**1A. What data does the user is going to send you?**

This is refering to the **data coming in send by the user**. The user is going to send us:

* the **post' id**: That's how we are going to **relate comments to posts**!
* The comment's **body**

**1B. What data are you going to send back (return)?**

When we respond, we are going to send them:

    1. the comment's body
    2. the post's id that it (the comment) is related to
    3. A unique identifier for each individual comment!

Let's create those classes!

**First:** 

* The `storeapi/models/post.py` script is where our models are.
* We add the required models to deal with data coming in and out of our API in the `storeapi/models/post.py` script:
    * `CommentIn(BaseModel)`: For the **data coming in send by the user**: 
        * The post' ID.
        * The comment's body.
    * `Comment(CommentIn)`: this is going to add a unique identifier for each individial comment. So each comment will have:
        * The unique identifier for the comment.
        * The post's ID (inherited from `CommentIn`).
        * The comment's body (inherited from `CommentIn`).
    * `UserPostWithComments(BaseModel)`: This will have:
        * The post: `UserPost` that is going to have the post's ID and the inherited post's body.
        * The coments: `list[Comment]` a list of comments.
        * This is an example of how we can nest models within other models.
        * Example of a response of `UserPostWithComments(BaseModel)`:
        ```python
        {"post": {"id": 0, "body": "My post!"}, 
         "comments": [{"id": 2, "post_id": 0, "body": "A comment of post 0"}, 
                      {"id": 3, "post_id": 0, "body": "Other comment of post 0"},
                     ]             
        }
        ```

**Important**

* `UserPostWithComments(BaseModel)` is an example of how we can nest models within other models.
* What is the difference between an endpoint and a route?

## Section 3: Introduction to `pytest`
# Course

## Section 2, p10

`response_model=list[UserPost]` means that we are going to respond with a list that is going to content `UserPosts`.

`Pydantic` and `FastAPI` are gonna make sure that everything that we return here will get converted to JSON correctly.

## Section 2, p13

**Goal**: Split the API (`main.py`) into files with `APIRouter`.

**Main topic:** How to use an `APIRouter`

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

## Section 2, p14

**Goal**: Adding comments to the social media app.
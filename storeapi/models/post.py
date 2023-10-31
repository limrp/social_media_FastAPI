from pydantic import BaseModel


# Models to validate incoming data
class UserPostIn(BaseModel):
    body: str


class UserPost(UserPostIn):
    id: int

from fastapi import APIRouter, Depends
from authentication.oauth2 import get_current_user

blog = APIRouter(
    prefix="/api",
    tags= ["Blogs"]
)

@blog.post("/blogs")
def blogs(get_current_user=Depends(get_current_user)):
    return "Yeah Works"
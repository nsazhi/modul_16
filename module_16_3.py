from fastapi import FastAPI, Path, HTTPException
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def get_all_users() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def create_user(
        username: Annotated[str, Path(min_length=6, max_length=15, description="Enter username", example="totoro")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="24")]) -> str:
    user_id = str(int(max(users)) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
        user_id: str,
        username: Annotated[str, Path(min_length=6, max_length=15, description="Enter username", example="totoro")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="24")]) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} has been updated"


@app.delete("/user/{user_id}")
async def delete_user(user_id: str) -> str:
    users.pop(user_id)
    return f"User {user_id} has been deleted"

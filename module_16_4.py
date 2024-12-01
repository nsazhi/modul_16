from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel, Field

# Создание экземпляра приложения FastAPI
app = FastAPI()

users = []


# Создание модели данных
class User(BaseModel):
    id: int
    username: str = Field(..., min_length=5,
                          max_length=20,
                          description="Enter username",
                          examples=["totoro"])
    age: int = Field(..., ge=18,
                     le=120,
                     description="Enter age",
                     examples=["24"])


@app.get("/users")
async def get_all_users() -> List[User]:
    """
    Получение списка всех пользователей.
    """
    return users


@app.post("/user/{username}/{age}")
async def create_user(user: User) -> User:
    """
    Создание нового пользователя.
    """
    user_id = max((us.id for us in users), default=0) + 1
    new_user = User(id=user_id, username=user.username, age=user.age)
    users.append(new_user)
    return new_user


@app.put("/user/{user_id}/{username}/{age}")
# async def update_user(user_id: int, username: str, age: int) -> User:
async def update_user(user_id: int, user: User) -> User:
    """
    Изменение данных пользователя.
    - **user_id (int)**: ID пользователя
    """
    for us in users:
        if us.id == user_id:
            us.username = user.username
            us.age = user.age
            return user
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id: int) -> User:
    """
    Удаление пользователя.
    - **user_id (int)**: ID пользователя
    """
    for i, user in enumerate(users):
        if user.id == user_id:
            del_user = users[i]
            users.remove(del_user)
            return del_user
    raise HTTPException(status_code=404, detail="User was not found")

from fastapi import FastAPI, Path
from typing import Annotated

# Создаем экземпляр приложения FastAPI
app = FastAPI()


# Определение базового маршрута
@app.get("/")
async def root() -> dict:
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def get_admin() -> dict:
    """
    Вход в систему для администраторов.
    """
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def get_user_id(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example="45")]) -> dict:
    """
    Вход в систему для пользователей.
    - **user_id (int)**: id пользователя
    """
    return {"message": f"Вы вошли как пользователь № {user_id}"}


@app.get("/user/{username}/{age}")
async def get_user_info(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="24")]) -> dict:
    """
    Информация о пользователе.
    - **username (str)**: имя пользователя
    - **age (int)**: возраст пользователя
    """
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

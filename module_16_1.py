from fastapi import FastAPI

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
async def get_user_id(user_id: int):
    """
    Вход в систему для пользователей.
    - **user_id**: id пользователя
    """
    return {"message": f"Вы вошли как пользователь № {user_id}"}


@app.get("/user")
async def get_user_info(username: str, age: int):
    """
    Информация о пользователе.
    - **username**: имя пользователя
    - **age**: возраст пользователя
    """
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

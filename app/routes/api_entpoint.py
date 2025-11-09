from fastapi import APIRouter
from app.osnovnoe import Vkuser
router = APIRouter()

temp_users = {} # вот тут надо в бд сохранять
@router.post("/vk_register/")
def vk_register(vk_user: Vkuser):
    # Сохраняем черновой объект (например, в сессию или временную таблицу)
    temp_users[vk_user.vk_id] = vk_user
    return {"message": "VK data received"}

@router.get("/register")
async def register():
    return {"message": "Registration"}




from fastapi import APIRouter
from app.osnovnoe import Vkuser
from app.models_orm import User

router = APIRouter()

# надо реализовать историю что сначала добовление имен и айди в бд
# потом вуза роли и группы все в табличку user


# написать добовление в базу данны
@router.post("/vk_register/")
def vk_register(vk_user: Vkuser):
    # Сохраняем черновой объект (например, в сессию или временную таблицу)
    USER[vk_user.vk_id] = vk_user
    return {"message": "VK data received"}

@router.post("/vk_register/univer")
def vk_register(unik: UniversityEnum):
    temp_users[vk_user.vk_id] = vk_user # и так же в бд сохраняем
    return {"message": "VK data received"}




from typing import List

from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from db import getdb
from services import categorys as category_service
from dto.categorys import Category

router = APIRouter()

@router.get("/categorys", tags=['categorys'])
async def get_categorys(db: Session = Depends(getdb)):
    return category_service.get_categorys(db)

@router.get("/categorys/{id}", tags=['categorys'])
async def get_category(id: int, db: Session =Depends(getdb)):
    return category_service.get_category(id,db)

@router.post("/categorys", tags=['categorys'])
async def create_category(data: Category, db: Session = Depends(getdb)):
    return category_service.create_category(data,db)

@router.delete("/categorys/{id}", tags=['categorys'])
async def delete_category(id: int, db: Session = Depends(getdb)):
    return category_service.delete_category(id,db)

@router.put("/categorys/{Category_id}/register/{user_id}", tags=['categorys'])
async def register_category(category_id: int, user_id:int, db: Session =Depends(getdb)):
    return category_service.sign_up_for_category(user_id,category_id,db)
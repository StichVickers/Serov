from fastapi import Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from models.categorys import Categorys
from models.user import User
from dto.categorys import Category as CategoryDto
from dto.user import User as UserDto
def create_category(data: CategoryDto ,db: Session):
    category = Categorys(name=data.name, description=data.description)
    try:
        db.add(category)
        db.commit()
        db.refresh(category)
    except Exception as e:
        print(e)
    return category


def get_categorys(db: Session):
    return  db.query(Categorys).all()


def get_category(id: int, db: Session):
    return db.query(Categorys).filter(Categorys.id == id).first()

def delete_category(id: int, db: Session):
    category = db.query(Categorys).filter(Categorys.id == id).delete()
    db.commit()
    return category

def sign_up_for_category(user_id: int, category_id: int, db: Session):
    try:
        user = db.query(User).filter(User.id == user_id).first()
        category = db.query(Categorys).filter(Categorys.id == category_id).first()

        if user is None or category is None:
            raise HTTPException(status_code=404, detail="User or category not found")

        if category.members is None:
            category.members = [user_id]
        else:
            category.members.append(user_id)

        db.commit()
        return {"message": f"User '{user.login}' successfully signed up for category '{category.name}'."}

    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="User is already signed up for this category")
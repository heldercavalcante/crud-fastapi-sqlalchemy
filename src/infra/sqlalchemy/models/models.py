from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from infra.sqlalchemy.config.database import Base
from sqlalchemy.orm import relationship


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    details = Column(String)
    price = Column(Float)
    available = Column(Boolean)
    #size = Column(String)
    user_id = Column(Integer, ForeignKey('user.id', name='fk_user'))
    category_id = Column(Integer, ForeignKey('categories.id', name='fk_category'))

    user = relationship('User', back_populates = 'products')
    category = relationship('Category', back_populates = 'categories')

    def validate(self):
        if len(self.name) < 4:
            raise Exception('name should have 4 caracteres')

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    password = Column(String)
    phone = Column(String)

    products = relationship('Product', back_populates = 'user')

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    categories = relationship('Product', back_populates = 'category')




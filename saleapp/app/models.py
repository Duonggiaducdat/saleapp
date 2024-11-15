from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app import db, app
from sqlalchemy.orm import relationship



class Category(db.Model):
    id = Column(Integer,primary_key=True,autoincrement=True )
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category')


class Products (db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    description = Column(String(255), nullable=True)
    price = Column (Float, default=0)
    image = Column(String(100), nullable=True)
    category_id= Column(Integer, ForeignKey(Category.id), nullable=False)

if __name__=='__main__':
    with app.app_context():
        pass
       # db.create_all()
       #  c1 = Category(name ='Mobile')
       #  c2 = Category(name='Tablet')
       #  c3 = Category(name='Desktop')
       #
       #  db.session.add_all([c1,c2,c3])
       #  db.session.commit()

    data = [{
        "id": 1,
        "name": "iPhone 7 Plus8",
        "description": "Apple, 32GB, RAM: 3GB, iOS13",
        "price": 17000000,
        "image":
            "https://cdn.tgdd.vn/Products/Images/42/251192/iphone-14-pro-max-tim-thumb-600x600.jpg",
        "category_id": 1
    }, {
        "id": 2,
        "name": "iPad Pro 20207",
        "description": "Apple, 128GB, RAM: 6GB",
        "price": 37000000,
        "image":
            "https://cdn.tgdd.vn/Products/Images/42/251192/iphone-14-pro-max-tim-thumb-600x600.jpg",
        "category_id": 2
    }, {
        "id": 3,
        "name": "Galaxy Note 10 Plus6",
        "description": "Samsung, 64GB, RAML: 6GB",
        "price": 24000000,
        "image":
            "https://cdn.tgdd.vn/Products/Images/42/251192/iphone-14-pro-max-tim-thumb-600x600.jpg",
        "category_id": 1
    }, {
        "id": 3,
        "name": "Galaxy Note 10 Plus5",
        "description": "Samsung, 64GB, RAML: 6GB",
        "price": 24000000,
        "image":
            "https://cdn.tgdd.vn/Products/Images/42/251192/iphone-14-pro-max-tim-thumb-600x600.jpg",
        "category_id": 1
    }, {
        "id": 3,
        "name": "Galaxy Note 10 Plus4",
        "description": "Samsung, 64GB, RAML: 6GB",
        "price": 24000000,
        "image":
            "https://cdn.tgdd.vn/Products/Images/42/251192/iphone-14-pro-max-tim-thumb-600x600.jpg",
        "category_id": 1
    }, {
        "id": 3,
        "name": "Galaxy Note 10 Plus3",
        "description": "Samsung, 64GB, RAML: 6GB",
        "price": 24000000,
        "image":
            "https://cdn.tgdd.vn/Products/Images/42/251192/iphone-14-pro-max-tim-thumb-600x600.jpg",
        "category_id": 1
    }, {
        "id": 3,
        "name": "Galaxy Note 10 Plus2",
        "description": "Samsung, 64GB, RAML: 6GB",
        "price": 24000000,
        "image":
            "https://cdn.tgdd.vn/Products/Images/42/251192/iphone-14-pro-max-tim-thumb-600x600.jpg",
        "category_id": 1
    }, {
        "id": 3,
        "name": "Galaxy Note 10 Plus1",
        "description": "Samsung, 64GB, RAML: 6GB",
        "price": 24000000,
        "image":
            "https://cdn.tgdd.vn/Products/Images/42/251192/iphone-14-pro-max-tim-thumb-600x600.jpg",
        "category_id": 1
    }]
    for p in data:
        prod = Products(name=p['name'], description=p['description'], price=p['price'], category_id=p['category_id'])
        db.session.add(prod)

    db.session.commit()

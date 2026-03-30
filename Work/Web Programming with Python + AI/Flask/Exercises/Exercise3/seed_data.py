from datetime import date
from create_tables import (
    SessionLocal,
    Brand, Category, Product, Drop, ProductDrop,
    User, Order, OrderItem
)

db = SessionLocal()

nike = Brand(name="Nike")
adidas = Brand(name="Adidas")
essentials = Brand(name="Essentials")

db.add_all([nike, adidas, essentials])
db.commit()


sneakers = Category(name="Sneakers")
hoodies = Category(name="Hoodies")
tshirts = Category(name="T-Shirts")

db.add_all([sneakers, hoodies, tshirts])
db.commit()


p1 = Product(name="Air Max 97", price=150, brand_id=nike.id, category_id=sneakers.id)
p2 = Product(name="Dunk Low Panda", price=120, brand_id=nike.id, category_id=sneakers.id)
p3 = Product(name="Essentials Hoodie", price=90, brand_id=essentials.id, category_id=hoodies.id)

db.add_all([p1, p2, p3])
db.commit()


d1 = Drop(name="Summer Drop", release_date=date(2024, 6, 1))
d2 = Drop(name="Retro Wave", release_date=date(2024, 8, 15))

db.add_all([d1, d2])
db.commit()


pd1 = ProductDrop(product_id=p1.id, drop_id=d1.id)
pd2 = ProductDrop(product_id=p1.id, drop_id=d2.id)
pd3 = ProductDrop(product_id=p2.id, drop_id=d1.id)

db.add_all([pd1, pd2, pd3])
db.commit()


u1 = User(username="john", password="1234")
u2 = User(username="emma", password="abcd")

db.add_all([u1, u2])
db.commit()

order1 = Order(user_id=u1.id, total_price=270)
order2 = Order(user_id=u2.id, total_price=90)

db.add_all([order1, order2])
db.commit()


oi1 = OrderItem(order_id=order1.id, product_id=p1.id, quantity=1)
oi2 = OrderItem(order_id=order1.id, product_id=p2.id, quantity=1)
oi3 = OrderItem(order_id=order2.id, product_id=p3.id, quantity=1)

db.add_all([oi1, oi2, oi3])
db.commit()

db.close()

print("Seed completed successfully!")
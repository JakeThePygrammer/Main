CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    full_name   VARCHAR(100),
    city        VARCHAR(50)
);

CREATE TABLE products (
    product_id   INT PRIMARY KEY,
    product_name VARCHAR(100),
    category     VARCHAR(50),
    price        DECIMAL(10,2)
);

CREATE TABLE orders (
    order_id    INT PRIMARY KEY,
    customer_id INT,
    order_date  DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY,
    order_id      INT,
    product_id    INT,
    quantity      INT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

INSERT INTO customers (customer_id, full_name, city) VALUES
(1, 'Ana Petrova', 'Skopje'),
(2, 'Marko Iliev', 'Bitola'),
(3, 'Jovana Stojanovska', 'Skopje'),
(4, 'Petar Trajkov', 'Ohrid');

INSERT INTO products (product_id, product_name, category, price) VALUES
(1, 'Laptop Lenovo', 'Electronics', 45000),
(2, 'Mouse Logitech', 'Electronics', 1500),
(3, 'Office Chair', 'Furniture', 8000),
(4, 'Desk Lamp', 'Furniture', 1200),
(5, 'USB Flash 32GB', 'Electronics', 700);

INSERT INTO orders (order_id, customer_id, order_date) VALUES
(1, 1, '2025-01-10'),
(2, 1, '2025-02-05'),
(3, 2, '2025-02-10'),
(4, 3, '2025-03-01');

INSERT INTO order_items (order_item_id, order_id, product_id, quantity) VALUES
(1, 1, 1, 1),
(2, 1, 2, 2),
(3, 2, 5, 3),
(4, 3, 3, 1),
(5, 3, 4, 2),
(6, 4, 2, 1);

SELECT * from products where category = 'Electronics' and price >= 1000 and price <= 10000 and product_name NOT LIKE '%USB%' ORDER BY price desc, product_name;
SELECT * from products where category = 'Electronics' or category = 'Furniture' and price <= 9000 and product_name LIKE 'D%' or product_name LIKE 'O%' ORDER BY category, product_name;
SELECT * from customers where city != 'Skopje' and full_name NOT LIKE 'P%' and full_name LIKE '_____%' ORDER BY city, full_name;
SELECT * from products where price > (SELECT AVG(price) from products);
SELECT * from products where 3000 <= (SELECT AVG(price) from products GROUP BY category) and (SELECT count(*) from products GROUP BY category) >= 2 GROUP BY category;




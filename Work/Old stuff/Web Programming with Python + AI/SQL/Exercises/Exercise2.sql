CREATE TABLE product(
    id INT PRIMARY KEY,
    name VARCHAR(100),
    description TEXT,
    amount INT,
    category_id INT,
    price INT,
    FOREIGN KEY(category_id) REFERENCES category(id)
);

CREATE TABLE category(
    id INT PRIMARY KEY,
    name VARCHAR(100),
    description TEXT
);

CREATE TABLE sale(
    id INT PRIMARY KEY,
    timeanddate DATETIME,
    product_id INT,
    amount INT,
    FOREIGN KEY(product_id) REFERENCES product(id)
);

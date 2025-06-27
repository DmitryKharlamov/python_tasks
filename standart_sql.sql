CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  customer_id INTEGER,
  order_date date NOT NULL,
  FOREIGN KEY (customer_id) REFERENCES customers(id)
);

CREATE TABLE order_items (
  id SERIAL PRIMARY KEY,
  order_id INTEGER,
  product_name VARCHAR(50) NOT NULL,
  quantity INTEGER,
  price DECIMAL,
  FOREIGN KEY (order_id) REFERENCES orders(id)

  );
INSERT INTO customers (name, email)
VALUES ('Иван Иванов', 'test@mail.com'),
       ('Денис Петров', 'testmail@mail.ru'),
       ('Петр Денисов', 'mail@mail.ru');

INSERT INTO orders (customer_id, order_date)
VALUES (1, '2025-06-20'),
       (1, '2025-06-19'),
       (2, '2025-06-20'),
       (3, '2025-06-20');

INSERT INTO order_items (order_id, product_name, quantity, price)
VALUES (1, 'Phone', 1, 199.99),
       (1, 'TV', 2, 399.29),
       (2, 'iPhone', 2, 400.99),
       (3, 'Airpods', 3, 90.99),
       (3, 'SamsungA51', 1, 99.00),
       (1, 'Refrigerator', 1, 10999.99);

SELECT orders.id, orders.order_date
FROM orders
JOIN customers on orders.customer_id = customers.id
WHERE customers.name = 'Иван Иванов';

SELECT product_name, quantity, price
FROM order_items
WHERE order_id = 3
ORDER BY price DESC;

SELECT customers.name, SUM(quantity * price) as total_spent
FROM customers
JOIN orders on orders.customer_id = customers.id
JOIN order_items on order_items.order_id = orders.id
GROUP BY customers.name
HAVING SUM(quantity * price) >= 10000;

SELECT customers.name, SUM(quantity * price) as total_spent
FROM customers
JOIN orders on orders.customer_id = customers.id
JOIN order_items on order_items.order_id = orders.id
GROUP BY customers.name
HAVING SUM(quantity * price) >= 10000;



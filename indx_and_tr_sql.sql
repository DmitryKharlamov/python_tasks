INSERT INTO customers (name, email)
SELECT
	‘Покупатель’ || id,
	‘email_’ || id || ‘@example.com’
FROM generate_series(1, 10000) AS id;

INSERT INTO orders (customer_id, order_date)
SELECT
	(random() * 9999 + 1)::int
	 CURRENT_DATE - (random() * 365)::int
	 FROM generate_series(1,7000);

INSERT INTO order_items (order_id, product_name, quantity, price)
SELECT
	orders.id,
	‘Товар’ || (random() *499+1)::int
	(random() *9 + 1)::int
	(random() * 99900 + 100)::numeric(10,2)
FROM orders



INSERT INTO order_items (order_id, product_name, quantity, price)
SELECT
	(random() * 6999 + 1)::int
	‘Товар’ || (random() *499+1)::int
	(random() *9 + 1)::int
    (random() * 99900 + 100)::numeric(10,2)
	 FROM generate_series(1,);993000);



CREATE INDEX idx_orders_customer_id ON orders(customer_id);

CREATE INDEX idx_order_items_order_id_price ON order_items(order_id, price);

CREATE INDEX idx_order_items_product_name ON order_items(product_name);

EXPLAIN ANALYZE
SELECT oi.id, oi.product_name, oi.price, oi.quantity
FROM order_items oi
WHERE oi.order_id = 123 AND oi.price > 1000;


EXPLAIN ANALYZE
SELECT * FROM orders
WHERE customer_id = 1;


BEGIN;
INSERT INTO orders (customer_id, order_date)
VALUES (1, CURRENT_DATE);

INSERT INTO order_items (order_id, product_name, quantity, price)
SELECT
  1,
  'Товар_' || (random() * 499 + 1)::int,
  (random() * 9 + 1)::int,
  round((random() * 99900 + 100)::numeric, 2)
FROM generate_series(1, floor(random() * 3 + 3)::int);

COMMIT;

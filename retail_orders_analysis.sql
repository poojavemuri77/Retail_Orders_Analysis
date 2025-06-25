USE ecommerce;
SELECT * FROM orders;

/*Total KPI summary*/
SELECT 
    SUM(sale_price) AS total_sales,
    SUM(profit) AS total_profit
FROM orders;

/*Show sub-categories where total sales exceeded 50,000*/
SELECT sub_category, SUM(sale_price) AS total_sales
FROM orders
GROUP BY sub_category
HAVING total_sales > 50000;

/*Most profitable category*/
SELECT category, SUM(profit) AS total_profit
FROM orders
GROUP BY category
ORDER BY total_profit DESC
LIMIT 1;

/*Find the top highest revenue generating products*/
SELECT product_id,sum(sale_price) as sales
FROM orders
GROUP BY product_id
ORDER BY sales desc
LIMIT 10;

/*Find the top 5 highest selling products in each region*/
SELECT region, product_id, sales,rn
FROM (
    SELECT region,product_id,
        SUM(sale_price) AS sales,
        ROW_NUMBER() OVER (PARTITION BY region ORDER BY SUM(sale_price) DESC) AS rn
    FROM orders
    GROUP BY region, product_id
) ranked
WHERE rn <= 5;

/*Find month over month growth comparison for 2022 and 2023 sales eg : jan 2022 vs jan 2023*/
WITH cte AS (
    SELECT 
        YEAR(order_date) AS order_year,
        MONTH(order_date) AS order_month,
        SUM(sale_price) AS sales
    FROM orders
    WHERE YEAR(order_date) IN (2022, 2023)
    GROUP BY YEAR(order_date), MONTH(order_date)
)

SELECT 
    order_month,
    SUM(CASE WHEN order_year = 2022 THEN sales ELSE 0 END) AS sales_2022,
    SUM(CASE WHEN order_year = 2023 THEN sales ELSE 0 END) AS sales_2023,
    ROUND(
        (SUM(CASE WHEN order_year = 2023 THEN sales ELSE 0 END) - 
         SUM(CASE WHEN order_year = 2022 THEN sales ELSE 0 END)) * 100.0 /
        NULLIF(SUM(CASE WHEN order_year = 2022 THEN sales ELSE 0 END), 0),
        2
    ) AS growth_percentage
FROM cte 
GROUP BY order_month
ORDER BY order_month;




-- Write your PostgreSQL query statement below
with product_year as (
    select product_id, min(year)
    from sales
    group by product_id)


select product_id, year as first_year, quantity, price
from sales
where (product_id, year) in (select * from product_year)
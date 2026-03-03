-- Write your PostgreSQL query statement below
with orders_2019 as (
    select o.buyer_id, coalesce(count(o.order_date), 0) as orders_in_2019
    from orders o
    where extract(year from o.order_date) = 2019
    group by o.buyer_id
)

select u.user_id as buyer_id, u.join_date, coalesce(o2019.orders_in_2019, 0) as orders_in_2019
from users u left join orders_2019 o2019 on u.user_id = o2019.buyer_id

-- Write your PostgreSQL query statement below
select c.name as customers from customers c
full outer join orders o on c.id = o.customerId
where o.customerId is null
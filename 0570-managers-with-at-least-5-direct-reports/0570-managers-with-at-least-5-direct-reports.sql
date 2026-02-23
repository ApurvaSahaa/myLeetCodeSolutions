-- Write your PostgreSQL query statement below
with reportcount as (select managerId, count(*)
from employee
group by managerId)

select e.name
from employee e
join 
reportcount r on e.id = r.managerId
where r.count >= 5
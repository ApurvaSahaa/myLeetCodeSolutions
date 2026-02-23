-- Write your PostgreSQL query statement below
with reportcount as (
    select managerId, count(*) as count
    from employee
    group by managerId
    having count(*) >= 5
)

select name
from employee
where id in (select managerId from reportcount)
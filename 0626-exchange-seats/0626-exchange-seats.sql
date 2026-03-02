-- Write your PostgreSQL query statement below
select
case
    when s1.id % 2 <> 0 then coalesce((select s2.id from seat s2 where s1.id = s2.id - 1), s1.id)
    when s1.id % 2 = 0 then coalesce((select s2.id from seat s2 where s1.id = s2.id + 1), s1.id)
end as id, student
from seat s1
order by id 
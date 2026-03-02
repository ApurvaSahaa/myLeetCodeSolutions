-- Write your PostgreSQL query statement below
select
case when count(*) = 1 then num
    else null
    end as num
from mynumbers
group by num
order by num desc nulls last
limit 1
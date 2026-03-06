-- Write your PostgreSQL query statement below
select query_name, 
round(sum(quality)::numeric/count(*), 2) as quality, 
round(sum(is_poor)::numeric*100/count(*), 2) as poor_query_percentage
from (select query_name, rating::numeric/position as quality, case when rating < 3 then 1 else 0 end as is_poor
from queries)
group by query_name
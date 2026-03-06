-- Write your PostgreSQL query statement below
select person_name
from (select turn, person_id, person_name, weight, sum(weight) over(order by turn rows unbounded preceding) as rolling_sum
from queue)
where rolling_sum <= 1000
order by rolling_sum desc
limit 1
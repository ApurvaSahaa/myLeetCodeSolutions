-- Write your PostgreSQL query statement below
select email from (select email, count(*) as duplicates
from person
group by email)
where duplicates > 1
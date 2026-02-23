-- Write your PostgreSQL query statement below

with onecolumn as
(select requester_id as id from requestaccepted
union all
select accepter_id as id from requestaccepted
)

select id, count(*) as num
from onecolumn
group by id
order by num desc
limit 1
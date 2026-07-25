-- Write your PostgreSQL query statement below
with messages as 
(
    select s.user_id, count(*)
    from signups s left join confirmations c on s.user_id = c.user_id
    group by s.user_id
)
,
confirmed as 
(
    select c.user_id, case when c.action='confirmed' then 1 else 0 end as confirmed_message
    from confirmations c
)
,
final_cte as
(
    select m.user_id, m.count, sum(c.confirmed_message)
    from messages m join confirmed c on m.user_id=c.user_id
    group by m.user_id, m.count
)

select s.user_id, round(coalesce(fc.sum::numeric/fc.count, 0)::numeric, 2) as confirmation_rate
from signups s left join final_cte fc on s.user_id = fc.user_id
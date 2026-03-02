-- Write your PostgreSQL query statement below
select activity_date as day, count(distinct(user_id)) as active_users
from activity
group by activity_date
having activity_date >'2019-07-27'::date - interval '30 days' and activity_date <= '2019-07-27'::date
order by activity_date
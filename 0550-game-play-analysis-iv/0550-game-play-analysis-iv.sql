-- Write your PostgreSQL query statement below
select round(count(distinct player_id) * 1.0 / (select count(distinct player_id) from activity), 2) as fraction
from activity
where (player_id, event_date - 1) in
(select player_id, min(event_date)
from activity
group by player_id)
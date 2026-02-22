-- Write your PostgreSQL query statement below
select current_day.id
from weather as current_day
where exists (
    select 1
    from weather as yesterday
    where current_day.temperature > yesterday.temperature
    and current_day.recordDate = yesterday.recordDate + 1
)

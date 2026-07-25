-- Write your PostgreSQL query statement below
with report_count as 
(

    select e.managerId, count(*) as number_of_reports
    from employee e
    group by e.managerId
    having count(*) >= 5
)

select e.name 
from employee e join report_count rc on e.id = rc.managerId

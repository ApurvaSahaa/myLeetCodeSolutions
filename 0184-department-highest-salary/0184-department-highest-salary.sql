-- Write your PostgreSQL query statement below
--select department, employee, salary
--from (select d.name as department, e.name as employee, e.salary as salary, 
--rank() over (partition by d.name order by salary desc) as ranking
--from employee e join department d on e.departmentId = d.id)
--where ranking = 1
select d.name as department, e.name as employee, e.salary as salary
from employee e join department d on e.departmentId = d.id
where (e.departmentId, e.salary) in 
(select departmentId, max(salary) from employee group by departmentId)
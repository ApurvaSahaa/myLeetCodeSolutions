-- Write your PostgreSQL query statement below
select department, employee, salary
from (select d.name as department, e.name as employee, e.salary as salary, 
dense_rank() over (partition by d.name order by e.salary desc) as rank
from employee e join department d on e.departmentId = d.id)
where rank <= 3
-- Write your PostgreSQL query statement below
select w.name, w.population, w.area
from world w
where area >= 3_000_000 or population >= 25_000_000
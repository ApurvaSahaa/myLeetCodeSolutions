-- Write your PostgreSQL query statement below
with uniquecoordinates as
(select lat, lon
from insurance
group by lat, lon
having count(*) = 1)
,
tiv_2015_values as
(select tiv_2015
from insurance
group by tiv_2015
having count(*) > 1)

select round(sum(tiv_2016)::numeric, 2) as tiv_2016
from insurance
where 
tiv_2015 in (select * from tiv_2015_values)
and
(lat, lon) in (select * from uniquecoordinates)
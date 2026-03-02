-- Write your PostgreSQL query statement below
-- in is generally more efficient than not in due to error from possible null values
-- to overcome that we can use not in with a where column is not null condition
-- or use in, not exists, or left join
select id,
case
    when p_id is null then 'Root'
    when id in (select distinct p_id from tree) then 'Inner'
    else 'Leaf'
end as type
from tree

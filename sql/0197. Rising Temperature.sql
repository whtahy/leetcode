# Write your MySQL query statement below
select
    b.id
from weather a, weather b
where
    b.temperature > a.temperature
    and datediff(b.recordDate, a.recordDate) = 1

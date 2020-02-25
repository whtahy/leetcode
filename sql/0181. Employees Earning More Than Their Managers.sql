# Write your MySQL query statement below
select
    a.name as employee
from employee a
left join (
    select
        id,
        salary
    from employee) b
on a.managerid = b.id
where
    a.salary > b.salary

# Write your MySQL query statement below
select
    b.name as department,
    a.name as employee,
    a.salary
from employee a
inner join department b
    on a.departmentid = b.id
where
    (a.departmentid, a.salary) in (
        select
            departmentid,
            max(salary)
        from employee
        group by
            departmentid
    )

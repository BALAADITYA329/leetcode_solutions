# Write your MySQL query statement below
select e.name as name, b.bonus as bonus from employee e left join bonus b
on e.empId=b.empId
where b.bonus is NULL or b.bonus<1000;
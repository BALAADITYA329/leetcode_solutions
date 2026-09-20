# Write your MySQL query statement below
select p.firstName,p.lastName,a.city,a.state from person p left join address a On p.personId=a.personId;
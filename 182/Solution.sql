# Write your MySQL query statement below
SELECT DISTINCT 
    Person1.Email AS Email 
FROM
    Person AS Person1 JOIN Person AS Person2
WHERE 
    Person1.Id!=Person2.Id AND Person1.Email=Person2.Email

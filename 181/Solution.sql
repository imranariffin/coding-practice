# Write your MySQL query statement below

SELECT Name AS Employee

FROM

(

    SELECT 

        Employee1.Id AS Id, 

        Employee1.Name as Name,

        Employee1.ManagerId AS ManagerId,

        Employee1.Salary AS Salary,

        Employee2.Salary AS MSalary

    FROM Employee AS Employee1 JOIN Employee AS Employee2

    WHERE Employee1.ManagerId=Employee2.Id

) AS X

WHERE X.Salary>X.MSalary

# Write your MySQL query statement below
SELECT 
    Today.Id
FROM
    Weather Today JOIN Weather Yesterday
WHERE
    TO_DAYS(Today.Date)-TO_DAYS(Yesterday.Date)=1 AND 
    Today.Temperature>Yesterday.Temperature

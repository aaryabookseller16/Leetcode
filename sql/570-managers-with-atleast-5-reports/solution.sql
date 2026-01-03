SELECT e.name
FROM Employee e
WHERE e.id IN ( -- this subquery gives us the name of the manager we want
    SELECT managerId
    FROM Employee
    GROUP BY managerId -- we want to check if managerId > 5
    HAVING COUNT(*) >= 5
);
SELECT e.name AS Employee -- separate new Employee column
FROM employee e 
JOIN employee m
    ON e.managerId = m.id -- how to join
WHERE e.salary > m.salary; --filter the results
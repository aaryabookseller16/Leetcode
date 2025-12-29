SELECT p.firstName, p.lastName, a.city, a.state -- the columns we want in order
FROM person p -- we want all the information from person table, so it will be the primary for left join
LEFT JOIN address a
    ON p.personId = a.personId
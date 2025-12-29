SELECT w.id
FROM Weather w -- today
JOIN Weather p -- previous day
  ON w.recordDate = DATE_ADD(p.recordDate, INTERVAL 1 DAY)
WHERE w.temperature > p.temperature;
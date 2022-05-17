SELECT ID, name
FROM student AS S1
         NATURAL JOIN takes AS T1
         NATURAL JOIN course AS C
         NATURAL JOIN section AS S2
         NATURAL JOIN time_slot AS T2
WHERE S2.year = 2022
  AND S2.semester = 'Spring'
  AND S2.building = 'East Lower Hall'
  AND (T2.day = 'F' OR T2.day = 'Friday')
  AND (T2.start_hr, T2.start_min, T2.end_hr, T2.end_min) = (10, 0, 11, 40)
  AND C.title in (SELECT title
                  FROM course
                  WHERE title LIKE '%Database%')
ORDER BY S.ID ASC;

SELECT DISTINCT
  CITY
FROM
  STATION
WHERE
  REGEXP_LIKE (CITY, '^[^aeiou].*', 'i');

-- Alternative
SELECT DISTINCT
  CITY
FROM
  STATION
WHERE
  CITY REGEXP '^[^aeiou]';
SELECT DISTINCT
  CITY
FROM
  STATION
WHERE
  REGEXP_LIKE (CITY, '[aeiou]+$', 'i');
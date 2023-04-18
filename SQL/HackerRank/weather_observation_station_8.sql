SELECT DISTINCT
  CITY
FROM
  STATION
WHERE
  REGEXP_LIKE (CITY, '^[aeiou].*[aeiou]$', 'i');

-- Alternative
SELECT DISTINCT
  city
FROM
  station
WHERE
  LEFT (city, 1) IN ('a', 'e', 'i', 'o', 'u')
  AND RIGHT (city, 1) IN ('a', 'e', 'i', 'o', 'u')
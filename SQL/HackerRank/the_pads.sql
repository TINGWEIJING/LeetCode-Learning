SELECT
  CONCAT (`Name`, '(', UPPER(LEFT (`Occupation`, 1)), ')')
FROM
  OCCUPATIONS
ORDER BY
  Name asc;

SELECT
  CONCAT (
    'There are a total of ',
    COUNT(`Name`),
    ' ',
    LOWER(`Occupation`),
    's.'
  )
FROM
  OCCUPATIONS
GROUP BY
  Occupation
ORDER BY
  COUNT(Name) asc,
  Occupation asc;
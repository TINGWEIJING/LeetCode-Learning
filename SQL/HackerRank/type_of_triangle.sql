SELECT
  CASE
    WHEN NOT (
      (A + B > C)
      AND (A + C > B)
      AND (B + C > A)
    ) THEN "Not A Triangle"
    WHEN (A = B)
    AND (B = C) THEN "Equilateral"
    WHEN (A = B)
    OR (B = C)
    OR (C = A) THEN "Isosceles"
    ELSE "Scalene"
  END
FROM
  TRIANGLES;

-- Alternative
SELECT CASE
    WHEN 2 * GREATEST(A, B, C) >= (A + B + C) THEN "Not A Triangle"
    WHEN A = B AND A = C                      THEN "Equilateral"
    WHEN A = B OR A = C OR B = C              THEN "Isosceles"
                                              ELSE "Scalene"
    END
FROM TRIANGLES
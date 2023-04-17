WITH
  challenge_count AS (
    SELECT
      ch.hacker_id,
      COUNT(ch.challenge_id) AS total_challenge
    FROM
      Challenges ch
    GROUP BY
      ch.hacker_id
  ),
  group_count AS (
    SELECT
      total_challenge,
      COUNT(hacker_id) AS total_same
    FROM
      challenge_count
    GROUP BY
      total_challenge
  )
SELECT
  h.hacker_id,
  h.name,
  cc.total_challenge
FROM
  Hackers h
  INNER JOIN challenge_count cc ON h.hacker_id = cc.hacker_id
  INNER JOIN group_count gc ON cc.total_challenge = gc.total_challenge
WHERE
  cc.total_challenge = (
    SELECT
      MAX(total_challenge)
    FROM
      challenge_count
  ) OR gc.total_same = 1
ORDER BY
  cc.total_challenge DESC,
  h.hacker_id ASC;

-- BEST ANS
/* count total submissions of challenges of each user */
WITH data
AS
(
SELECT c.hacker_id as id, h.name as name, count(c.hacker_id) as counter
FROM Hackers h
JOIN Challenges c on c.hacker_id = h.hacker_id
GROUP BY c.hacker_id, h.name
)
/* select records from above */
SELECT id,name,counter
FROM data
WHERE
counter=(SELECT max(counter) FROM data) /*select user that has max count submission*/
OR
counter in (SELECT counter FROM data
GROUP BY counter
HAVING count(counter)=1 ) /*filter out the submission count which is unique*/
ORDER BY counter desc, id
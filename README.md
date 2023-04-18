# Leetcode Learning
Tools: https://www.tldraw.com/
https://textedit.tools/snakecase

## [Top Interview](https://leetcode.com/problem-list/top-interview-questions/)
### Medium
- [237. Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/)

### Hard
- [149. Max Points on a Line](https://leetcode.com/problems/max-points-on-a-line/description/)

## [Dynamic Programming](https://leetcode.com/tag/dynamic-programming/)
- [392. Is Subsequence](https://leetcode.com/problems/is-subsequence/)
- [894. All Possible Full Binary Trees](https://leetcode.com/problems/all-possible-full-binary-trees/)
- [338. Counting Bits](https://leetcode.com/problems/counting-bits/)
- [118. Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/)
- [746. Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/)
- [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
- [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
- [1646. Get Maximum in Generated Array](https://leetcode.com/problems/get-maximum-in-generated-array/)
- [1641. Count Sorted Vowel Strings](https://leetcode.com/problems/count-sorted-vowel-strings/)


## HackerRank
### [SQL]()

### Interview 
https://www.hackerrank.com/interview/interview-preparation-kit

## SQL Practice
- https://www.mysqltutorial.org/mysql-sample-database.aspx
### Docker Setup
```bash
# run docker
docker run --name sql-learning \
  -e MYSQL_ROOT_PASSWORD=12345 \
  -p 3312:3306 \
  -v mysqldata:/var/lib/mysql \
  -d mysql:8.0-debian

# dump data
mysql \
  --host=127.0.0.1 \
  --port=3312 \
  -u root \
  -p12345 < data.sql

# connect to MySQL
mysql --host=127.0.0.1 \
  --port=3312 \
  -u root \
  -p12345

mysql --host=127.0.0.1 \
  --port=3312 \
  -D classicmodels \
  -u root \
  -p12345
```

-- Query 1: Retrieve the count of users who signed up on each day.
SELECT
    signup_date,
    COUNT(*) AS cnt_users
FROM users
GROUP BY signup_date
ORDER BY cnt_users DESC;
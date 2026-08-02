USE netflix_db;
GO
SELECT TOP 10 *
FROM dbo.netflix_customer_churn_cleaned;
GO

SELECT COUNT(*) AS total_customers
FROM dbo.netflix_customer_churn_cleaned;

SELECT COUNT(*) AS churned_customers
FROM dbo.netflix_customer_churn_cleaned
WHERE churned = 1;

--churn rate
SELECT
ROUND(
AVG(CAST(churned AS FLOAT)) * 100,
2
) AS churn_rate
FROM dbo.netflix_customer_churn_cleaned;

--Customers by Subscription
SELECT
subscription_type,
COUNT(*) AS total_customers
FROM dbo.netflix_customer_churn_cleaned
GROUP BY subscription_type
ORDER BY total_customers DESC;

--Churn by Subscription
SELECT
subscription_type,
SUM(CAST(churned AS INT)) AS churned_customers
FROM dbo.netflix_customer_churn_cleaned
GROUP BY subscription_type
ORDER BY churned_customers DESC;

--Average Monthly Fee
SELECT
subscription_type,
ROUND(AVG(monthly_fee),2) AS average_fee
FROM dbo.netflix_customer_churn_cleaned
GROUP BY subscription_type;

--Average Watch Hours
SELECT
subscription_type,
ROUND(AVG(watch_hours),2) AS average_watch_hours
FROM dbo.netflix_customer_churn_cleaned
GROUP BY subscription_type;

--Region-wise Customers
SELECT
region,
COUNT(*) AS total_customers
FROM dbo.netflix_customer_churn_cleaned
GROUP BY region
ORDER BY total_customers DESC;

--Region-wise Churn
SELECT
region,
SUM(CAST(churned AS INT)) AS churned_customers
FROM dbo.netflix_customer_churn_cleaned
GROUP BY region
ORDER BY churned_customers DESC;

--Device-wise Customers
SELECT
device,
COUNT(*) AS total_customers
FROM dbo.netflix_customer_churn_cleaned
GROUP BY device
ORDER BY total_customers DESC;

--Device-wise Churn
SELECT
device,
SUM(CAST(churned AS INT)) AS churned_customers
FROM dbo.netflix_customer_churn_cleaned
GROUP BY device
ORDER BY churned_customers DESC;

--Payment Method Analysis
SELECT
payment_method,
COUNT(*) AS customers
FROM dbo.netflix_customer_churn_cleaned
GROUP BY payment_method
ORDER BY customers DESC;

--Gender-wise Churn
SELECT
gender,
SUM(CAST(churned AS INT)) AS churned_customers
FROM dbo.netflix_customer_churn_cleaned
GROUP BY gender;

--Average Age by Churn Status
SELECT
churned,
ROUND(AVG(age),2) AS average_age
FROM dbo.netflix_customer_churn_cleaned
GROUP BY churned;

--Average Watch Hours by Churn Status
SELECT
churned,
ROUND(AVG(watch_hours),2) AS average_watch_hours
FROM dbo.netflix_customer_churn_cleaned
GROUP BY churned;

--Inactive Customers (>30 Days)
SELECT
COUNT(*) AS inactive_customers
FROM dbo.netflix_customer_churn_cleaned
WHERE last_login_days > 30;

--Favorite Genre Distribution
SELECT
favorite_genre,
COUNT(*) AS total_customers
FROM dbo.netflix_customer_churn_cleaned
GROUP BY favorite_genre
ORDER BY total_customers DESC;

--Highest Paying Customers
SELECT TOP 10
customer_id,
monthly_fee
FROM dbo.netflix_customer_churn_cleaned
ORDER BY monthly_fee DESC;

--Most Active Customers
SELECT TOP 10
customer_id,
watch_hours
FROM dbo.netflix_customer_churn_cleaned
ORDER BY watch_hours DESC;

--Average Daily Watch Time by Subscription
SELECT
subscription_type,
ROUND(AVG(avg_watch_time_per_day),2) AS avg_daily_watch_time
FROM dbo.netflix_customer_churn_cleaned
GROUP BY subscription_type;

--Churn Rate by Subscription
SELECT
subscription_type,
ROUND(AVG(CAST(churned AS FLOAT))*100,2) AS churn_rate
FROM dbo.netflix_customer_churn_cleaned
GROUP BY subscription_type
ORDER BY churn_rate DESC;
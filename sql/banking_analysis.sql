
-- Banking & Financial Transactions Analytics
-- Database: banking_analytics
-- Table: public.transactions

-- 1. Overall transaction summary
SELECT
    COUNT(*) AS total_transactions,
    SUM(amount) AS total_amount_tzs,
    ROUND(AVG(amount), 2) AS average_amount_tzs,
    MAX(amount) AS largest_transaction_tzs,
    MIN(amount) AS smallest_transaction_tzs
FROM public.transactions;

-- 2. Analysis by transaction type
SELECT
    transaction_type,
    COUNT(*) AS number_of_transactions,
    SUM(amount) AS total_amount_tzs,
    ROUND(AVG(amount), 2) AS average_amount_tzs
FROM public.transactions
GROUP BY transaction_type
ORDER BY total_amount_tzs DESC;

-- 3. Analysis by flagged status
SELECT
    is_flagged,
    COUNT(*) AS number_of_transactions,
    SUM(amount) AS total_amount_tzs
FROM public.transactions
GROUP BY is_flagged
ORDER BY is_flagged;

-- 4. Analysis by location
SELECT
    location,
    COUNT(*) AS number_of_transactions,
    SUM(amount) AS total_amount_tzs,
    ROUND(AVG(amount), 2) AS average_amount_tzs
FROM public.transactions
GROUP BY location
ORDER BY total_amount_tzs DESC;

-- 5. Analysis by channel
SELECT
    channel,
    COUNT(*) AS number_of_transactions,
    SUM(amount) AS total_amount_tzs,
    ROUND(AVG(amount), 2) AS average_amount_tzs
FROM public.transactions
GROUP BY channel
ORDER BY total_amount_tzs DESC;

-- 6. Analysis by account type
SELECT
    account_type,
    COUNT(*) AS number_of_transactions,
    SUM(amount) AS total_amount_tzs,
    ROUND(AVG(amount), 2) AS average_amount_tzs
FROM public.transactions
GROUP BY account_type
ORDER BY total_amount_tzs DESC;

-- 7. Daily transaction analysis
SELECT
    transaction_date,
    COUNT(*) AS number_of_transactions,
    SUM(amount) AS total_amount_tzs
FROM public.transactions
GROUP BY transaction_date
ORDER BY transaction_date;

-- 8. Flagged transaction details
SELECT
    transaction_id,
    customer_id,
    transaction_type,
    amount,
    transaction_date,
    channel,
    location,
    is_flagged
FROM public.transactions
WHERE LOWER(is_flagged) = 'yes'
ORDER BY amount DESC;

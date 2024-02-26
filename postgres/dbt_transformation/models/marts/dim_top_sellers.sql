with 
    sales_reps as (SELECT * FROM {{ ref ("stg_sales_rep")}}),
    sales as (SELECT * FROM {{ ref ("stg_sales")}}),
    best_sellers as(
         SELECT 
            e.employee_id,
            e.employee_name,
            SUM(CAST(s.total_sales AS DECIMAL)) AS Total_Sales_Amount
            FROM sales s
            INNER JOIN sales_reps e ON s.employee_id = e.employee_id 
            GROUP BY e.employee_id, e.employee_name
            ORDER BY Total_Sales_Amount DESC
            LIMIT 100
    )
SELECT * FROM best_sellers





     
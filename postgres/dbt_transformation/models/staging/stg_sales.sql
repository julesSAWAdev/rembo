SELECT   employee_id, SUM(CAST(sales_amount AS DECIMAL)) AS total_sales
FROM {{ source("raw_data", "sales") }}  
GROUP BY employee_id
 
 
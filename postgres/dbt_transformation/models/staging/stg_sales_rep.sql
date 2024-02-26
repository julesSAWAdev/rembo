
SELECT 
    e.employee_id,
    e.employee_name,
 FROM  {{ source("raw_data", "employee") }} e  
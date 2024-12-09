-- Use project database
use data_science_jobs;

-- Question #1. How does the supply of data science jobs change by job category over the years?
SELECT work_year, job_title, COUNT(job_title) as total_amount
from job GROUP BY work_year, job_title;

-- Question #2. How has salary in the data science sector evolved over the years?
SELECT work_year, job_title, round(avg(salary_in_usd),0) as "Avg_Salary_USD"
from job GROUP BY work_year, job_title;

-- Question #3. What is the relationship between level of experience and salary in the field of data science?
SELECT work_year, job_title, experience_level, round(avg(salary_in_usd),0) as "Avg_Salary_USD"
from job GROUP BY work_year, job_title, experience_level;

-- Question #4. What level of experience is most sought after in data science jobs: EN, MI, SE?
SELECT work_year, experience_level, COUNT(experience_level) as "Total_Jobs_level"
from job GROUP BY work_year, experience_level;

-- Question #5. What is the relationship between company size and the level of salaries offered in data science?
SELECT work_year, company_size, round(avg(salary_in_usd),0) as "Avg_Salary_USD"
from job GROUP BY work_year, company_size order by work_year, company_size desc;
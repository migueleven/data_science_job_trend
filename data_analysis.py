"""
    About the dataset

    The dataset we examined is a dataset that contains various features related to different job profiles in the Data Science field. It contains a total of 14838 rows and 11 columns.

        - Work Year: The year the job was registered
        - Experience Level: The employee's career experience level: For people working in EN (Entry-Level), MI (Mid-Level), SE (Senior-Level) and EX (Executive) positions. Executive
        - Employment Type: Employee's employment type and type of employment contract: Full-Time (FT), Part-Time (PT), Contract (CT), Freelance (FL)
        - Job Title: Employee's position or job title
        - Salary: Employee's salary
        - Salary Currency: Salary payment currency
        - Salary in Usd: Salary in US Dollars (USD)
        - Employee Residence: Employee’s place of residence or address
        - Remote Ratio: The rate at which the employee performs their work remotely, 100 = full remote, 50 = Hybrid, 0 = Person
        - Company Location: Usually the country where the company's headquarters or offices are located
        - Company Size: The size of the company: L (Large): Large Companies, M (Medium): Mid-Size Companies, S (Small): Small Companies


To analyze this dataset we will follow the next steps:

1. Loading the data: Import datasets into Python for analysis.
2. Understanding the data: Explore the structure, types, and contents of the data to identify key features.
3. Data Quality Assessment: Detect and document missing values, inconsistencies, and duplicates.
4. Cleaning the data: Address issues identified in the quality assessment to ensure data reliability.
5. Exploratory Data Analysis (EDA) and Visualization: Analyze patterns and trends, using visualizations to uncover insights.
6. Conclusions and Hypotheses: Summarize findings, propose actionable recommendations, and generate hypotheses for further analysis.
"""

# Importing libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")


# 2. Understanding Data
def understanding_data(df) -> pd.DataFrame:
    print("Data Science Jobs Info:")
    print(df.info(), "\n" + "-"*100 + "\n")
    print("Example of cash_request_df:\n", df.head(5), "\n" + "-"*100 + "\n")

    print("Data Science Jobs Summary Statistics:")
    print(df.describe().T, "\n" + "-"*100 + "\n")

    print("Check size of out dataset: ", df.shape)

    print("Checking columns names: ",df.columns) # There might be no need to change column names if there are no problematic issues with letter case or punctuation marks.

# 3. Data Quality Assessment
def assess_data_quality(df) -> pd.DataFrame:
    print("Missing Values in Data Science Jobs:") # Seems that are no null values
    print(df.isnull().sum(), "\n" + "-"*100 + "\n")

    print("Duplicated Rows in Data Science Jobs:", df.duplicated().sum(), "\n" + "-"*100 + "\n") # There are 5711 duplicated rows, this means that are similar jobs with same requirements so no need to clean it
    print("Uniques values per column:\n", df.nunique(), "\n" + "-"*100 + "\n")

# 4. Cleaning Data
def cleaning_data(df) -> pd.DataFrame:
    # There aren't missing values so no need to clean, we'll clean anyway in case sometime null columns are added
    df.dropna(inplace=True)

    # There are duplicated rows but probably are different jobs with same values, so no need to drop them
    #df = df.drop_duplicates().reset_index(drop=True)
    
    # Column 'work_year' it's integer type so we will need to convert it to str
    df['work_year'] = df['work_year'].astype(str) 

    # Remove unused columns in dataframe
    df.drop(columns=['salary','salary_currency'], axis=1, inplace=True)

    # Detecting Outliers in salary_in_usd
    # Interquartile Range (IQR) was calculated and outliers were checked.
    Q1 = df['salary_in_usd'].quantile(0.25)
    Q3 = df['salary_in_usd'].quantile(0.75)
    IQR = Q3 - Q1

    # Detecting outliers
    outliers = df[(df['salary_in_usd'] < (Q1 - 1.5 * IQR)) | (df['salary_in_usd'] > (Q3 + 1.5 * IQR))]
    #print(f"Outliers in 'salary_in_usd': \n{outliers}")

    # Reemplazar los espacios por guiones bajos en toda la columna 'job_title'
    df['job_title'] = df['job_title'].apply(lambda x: x.replace(" ", "_"))

    # Sorting cleaned data and saving it
    df.sort_values(by=['work_year'], ascending=True, inplace=True)
    df.to_csv('cleaned_sorted_data_salaries_2024.csv', index=False)
    df.to_excel('cleaned_sorted_data_salaries_2024.xlsx', index=False)

    return outliers

def exploratory_analysis(df) -> pd.DataFrame:
    """10 business questions to answer"""

    """About evolution in time"""
    # 1. How does the supply of data science jobs change by job category over the years?
    #print(df.groupby(['work_year', 'job_title'])['job_title'].value_counts())

    # 2. How has salary in the data science sector evolved over the years?
    #df.groupby(['work_year','job_title'])['salary_in_usd'].agg(['max','min','mean']).reset_index()

    # 3. Which data science job role or title has seen the largest increase in pay in recent years?
    """avg_salary_first_year = df[df['work_year'] == df['work_year'].min()].groupby('job_title')['salary_in_usd'].mean()
    avg_salary_last_year = df[df['work_year'] == df['work_year'].max()].groupby('job_title')['salary_in_usd'].mean()

    salary_difference = avg_salary_last_year - avg_salary_first_year

    print(f"The data science job role with the largest increase in salary from {df['work_year'].min()} to {df['work_year'].max()} is '{salary_difference.idxmax()}' with an increase of {salary_difference.max()} USD.")"""

    """About job modality """
    # 4. What is the difference in pay between data science jobs that are completely remote and those that require physical presence?
    #difference_salary_by_remote_ratio(df)

    # 5. How do the salaries of data scientists vary depending on whether they are freelancers or full-time employees?
    #difference_salary_by_employment_type(df)

    """About experience level """
    # 6. What is the relationship between level of experience and salary in the field of data science?
    #print((df.groupby(['work_year','job_title','experience_level'])['salary_in_usd'].agg(['max','min','mean'])).head(10))

    # 7. What level of experience is most sought after in data science jobs: entry-level, mid-level or senior-level?
    #print(df.groupby('work_year')['experience_level'].value_counts())
    #print(df[df['job_title']=='Data_Scientist'].groupby('work_year')['experience_level'].value_counts())

    """About companies"""
    # 8. Which companies have the highest demand for data science jobs?
    #print(df.groupby(['work_year','company_location'])['job_title'].value_counts().head())
    #print(df.groupby(['work_year','company_location'])['job_title'].max())
    #print(df[df['job_title']=='Data_Scientist'].groupby(['work_year','company_location'])['job_title'].value_counts())

    # 9. What is the relationship between company size and the level of salaries offered in data science?
    #print(df.groupby(['work_year','company_size'])['salary_in_usd'].mean())
    #print(df.groupby(['work_year','company_size'])['salary_in_usd'].mean())

    """About residence"""
    # 10. What is the relationship between the employee's salary and residence in relation to the location of the company?
    relation_residence_salary_company(df)

def relation_residence_salary_company(df) -> pd.DataFrame:
    # Agrupar por 'employee_residence' y 'company_location', calculando el salario promedio
    salary_by_residence_company = df[(df['job_title']=='Data_Scientist') & (df['work_year']=='2022')].groupby(['employee_residence', 'company_location'])['salary_in_usd'].mean().reset_index()

    salary_by_residence_company['salary_in_usd'] = round(salary_by_residence_company['salary_in_usd'], 0)
    # Crear una tabla pivotada para visualizar mejor los datos
    salary_pivot = salary_by_residence_company.pivot(index='employee_residence', columns='company_location', values='salary_in_usd')
    
    # Usar seaborn para crear un gráfico de calor (heatmap)
    plt.figure(figsize=(26, 8))
    sns.heatmap(salary_pivot, cmap="YlGnBu", annot=True, fmt=".1f", linewidths=.5)
    plt.title("Relationship between employee salary and company location")
    plt.xlabel("Company Location")
    plt.ylabel("Employee's Residence")
    plt.show()


def difference_salary_by_remote_ratio(df) -> pd.DataFrame:
    # Filter by modality job
    remote_jobs = df[df['remote_ratio'] == 100]
    in_person_jobs = df[df['remote_ratio'] == 0]

    # Group by job_title and work_year, calculate the average salary for each cohort
    remote_jobs_grouped = remote_jobs.groupby(['work_year', 'job_title'])['salary_in_usd'].mean().reset_index()
    in_person_jobs_grouped = in_person_jobs.groupby(['work_year', 'job_title'])['salary_in_usd'].mean().reset_index()

    # Rename the columns
    remote_jobs_grouped.rename(columns={'salary_in_usd': 'remote_salary'}, inplace=True)
    in_person_jobs_grouped.rename(columns={'salary_in_usd': 'in_person_salary'}, inplace=True)

    # Merge both dataframes by job_title and work_year
    merged_jobs = pd.merge(remote_jobs_grouped, in_person_jobs_grouped, on=['job_title', 'work_year'])

    # Calculate salary difference
    merged_jobs['salary_difference'] = merged_jobs['remote_salary'] - merged_jobs['in_person_salary']

    return print(merged_jobs)

def difference_salary_by_employment_type(df) -> pd.DataFrame:
    # Filter by employment_type job
    full_time_jobs = df[df['employment_type'] == 'FT']
    freelance_jobs = df[df['employment_type'] == 'FL']

    # Group by job_title and work_year, calculate the average salary for each cohort
    full_time_jobs_grouped = full_time_jobs.groupby(['work_year', 'job_title'])['salary_in_usd'].mean().reset_index()
    freelance_jobs_grouped = freelance_jobs.groupby(['work_year', 'job_title'])['salary_in_usd'].mean().reset_index()

    # Rename the columns
    full_time_jobs_grouped.rename(columns={'salary_in_usd': 'full_time_salary'}, inplace=True)
    freelance_jobs_grouped.rename(columns={'salary_in_usd': 'freelance_salary'}, inplace=True)

    # Merge both dataframes by job_title and work_year
    merged_jobs = pd.merge(full_time_jobs_grouped, freelance_jobs_grouped, on=['job_title', 'work_year'])

    # Calculate salary difference
    merged_jobs['salary_difference'] = merged_jobs['full_time_salary'] - merged_jobs['freelance_salary']

    return print(merged_jobs)

# Main Script
if __name__ == "__main__":
    # 1. Load the dataset
    df = pd.read_csv("DataScience_salaries_2024.csv")

    # 2. Understanding the dataset
    #understanding_data(df)

    # 3. Data Quality Assessment
    #assess_data_quality(df)

    # 4. Cleaning Data and getting outliers
    outliers = cleaning_data(df)
    print(outliers.head().sort_values(by='salary_in_usd',ascending=False))
    
    # 5. EDA
    exploratory_analysis(df)

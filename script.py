import pandas as pd
import re
import numpy as np

# Creating Function for Dataset 1
def dataset_1(df):
    def initial_exploration():
        #print(df.head())
        #print(df.shape) # 15750 rows / 21 cols
        df.columns = df.columns.str.strip().str.replace(' ', '_').str.lower()   
        #print(df.columns)
        #print(df.dtypes)

    initial_exploration()

    #######################################################################################
    # Cleaning Job Id
    #######################################################################################
    """Capturing only the numbers and converting them to Int and dropping empty rows"""

    df['job_id'] = df['job_id'].str.extract(r'(\d+)').astype('Int64')
    
    #######################################################################################
    # Cleaning job_title
    #######################################################################################
    """dropping empty rows"""

    # converting empty strings to NaNs
    df['job_title'] = df['job_title'].replace('', np.nan)
    df.dropna(subset=['job_title'], inplace=True)

    #######################################################################################
    # Cleaning object cols
    #######################################################################################
    """Normalize and lowering strings"""

    df[df.select_dtypes(include='object').columns]=(df.select_dtypes(include='object')
                                  .apply(lambda x: x.str.strip().str.lower()))
    
    #######################################################################################
    # salary_usd
    #######################################################################################    
    """Normalizing numbers, removing symbols and turning to Int"""
    
    df['salary_usd'] = df['salary_usd'].str.extract(r'(\d+)')

    # Step 1: Convert safely to numeric (in case there are leftover strings)
    df['salary_usd'] = pd.to_numeric(df['salary_usd'], errors='coerce')

    # Step 2: apply multiplication
    df['salary_usd'] = np.where(
        df['salary_usd'] < 1000,
        df['salary_usd'] * 1000,
        df['salary_usd']
    )

    # 1. Calculate the mean salary for each Job Title/Country group.
    mean_salary_by_group = df.groupby(['job_title', 'company_location'])['salary_usd'].transform('mean')

    # 2. Use 'fillna()' to replace NaN values in 'salary_usd' with the calculated mean.
    df['salary_usd'] = df['salary_usd'].fillna(mean_salary_by_group)

    # round
    df['salary_usd'] = df['salary_usd'].round(0)
    df['salary_usd'] = df['salary_usd'].astype('Int64')
    
    # Optional: Check the remaining NaNs
    #print(f"\nRemaining NaN values after group imputation: {df['salary_usd'].isna().sum()}")
    
    #######################################################################################
    # salary currency
    #######################################################################################   
    """Filling nan with eur if they belong to EU"""
    
    # define a list of EU countries
    eurozone_countries = ['denmark', 'germany', 'france', 'austria', 'ireland', 
                          'finland', 'switzerland', 'sweden', 'netherlands', 'united kingdom', 'norway']    

    # apply the conditional fill using np.where
    df['salary_currency'] = np.where(
        # Condition: Is the currency currently NaN? and Is the company EU based?
        (df['salary_currency'].isna()) & (df['company_location'].isin(eurozone_countries)),
        # IF True: impute or insert 'eur'
        'eur',
        # IF False: keep the original value
        df['salary_currency']
    )
    
    #######################################################################################
    # creating salary_eur from salary_usd
    #######################################################################################  
    usd_to_eur_rate = 0.86 # 14 october google's exchange rate
    
    #convert the entire salary_usd col to eur equivalent
    df['salary_eur'] = (df['salary_usd'] * usd_to_eur_rate).round(0)

    #######################################################################################
    # mod Experience Level based on years of experience
    #######################################################################################  

    # 1: define the conditions based on the yearsofexperience col
    conditions = [
        (df['years_experience'] <= 2),
        (df['years_experience'] > 2) & (df['years_experience'] <= 6),
        (df['years_experience'] > 6) & (df['years_experience'] <=12),
        (df['years_experience'] > 12)
    ]

    # 2: define the corresponding new labels
    choices = [
        'Entry Level',
        'Mid Level',
        'Senior',
        'Expert'
    ]
    
    # 3: apply the conditional logic
    df['experience_level'] = np.select(conditions, choices, default=None)

    #######################################################################################
    # employment type
    #######################################################################################

    employment_type_dict = {
            'fl': 'Freelance',
            'ct': 'Contract',
            'pt': 'Part Time',
            'ft': 'Full Time'
    }

    df['employment_type'] = df['employment_type'].map(employment_type_dict)

    #######################################################################################
    # company_size
    #######################################################################################

    company_size_dict = {
        'l': 'Large',
        'm': 'Medium',
        's': 'Small'
    }

    df['company_size'] = df['company_size'].map(company_size_dict)


    #######################################################################################
    # Cleaning skills_required col
    #######################################################################################
    """using the explode method to create a long format"""

    # Data cleaning: clean up the string first, this step is crucial for consistent skill grouping
    df['skills_clean'] = (
    df['required_skills']
    .str.lower()
    .str.replace(r',\s*', ',', regex=True) # Find a comma followed by ANY amount of whitespace, and replace with just a comma
    .str.strip()                          # Remove leading/trailing whitespace from the whole string
    .str.split(','))

    # Explode (unnest): turn the list of skills into new rows
    df_long = df.explode('skills_clean').rename(columns={'skills_clean': 'skill'})

    # Final cleanup: select relevant columns and drop the original skills column
    df = df_long.drop(columns=['required_skills']).reset_index(drop=True)

    # Verification
    # print("\n--- Transformed (Long Format) DataFrame (First 10 rows)---")
    # print(df[['job_title', 'salary_usd', 'skill']].head(10))
    # print(f"\nOriginal Rows: {len(df)}")
    # print(f"Transformed Rows: {len(df)}")
    # print("-" * 40)

    #######################################################################################
    # Cleaning years_of_experience
    #######################################################################################

    df['years_experience'] = df['years_experience'].round(0).astype('Int64')

    #######################################################################################
    # Cleaning post_date
    #######################################################################################
    """normalizing the dates to one format"""

    df['posting_date'] = pd.to_datetime(df['posting_date'], errors='coerce', format='mixed', dayfirst=True)


    #######################################################################################
    # Dropping unwanted columns
    #######################################################################################

    df.drop(columns=['job_id', 'salary_usd', 'salary_currency', 'employee_residence', 'remote_ratio', 'application_deadline', 
                     'job_description_length', 'benefits_score', 'notes'], inplace=True)
    


    #######################################################################################
    # Title Case job title col
    #######################################################################################

    df = df.apply(lambda col: col.str.title() if col.dtypes == 'object' else col)


    # Title case every object (string) column
    # df = df.apply(lambda col: col.str.title() if col.dtypes == 'object' else col)

    #df['job_title'] = df['job_title'].str.title()


    #######################################################################################
    # Saving Cleaned File
    #######################################################################################

    df.to_csv('Cleaned_dataset_1.csv', index=False)
    print("Cleaned File Saved Succesfully!")
    return df

if __name__ == "__main__":
    # Reading the File
    df1 = pd.read_csv('ai_job_dataset_messy_1.csv')
    
    dataset_1(df1)

    # print(df2.head())
    # print(df2.columns)
    # print(df2.shape)



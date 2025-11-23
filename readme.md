# AI Job Market Analysis 2025: Skills & Salary Insights 🇪🇺

[Tableau Dashboard](https://public.tableau.com/views/EUAISkillsSalaries20242025/Dashboard?:language=en-US&publish=yes&:sid=&:display_count=n&:origin=viz_share_link) 

![alt text](image-1.png)

## 📊 Project Overview

This data analytics project delves into the European AI job market for 2024/2025. By cleaning and analyzing a messy, real-world dataset, I uncovered the relationships between **technical skills, years of experience, and compensation** for roles like Data Scientist, Machine Learning Engineer, AI Product Manager, and others

## Data Sources

* Raw Dataset: RAW_ai_job_dataset.csv - Sourced from aggregated job postings on LinkedIn, Indeed, Glassdoor, and Kaggle. Contains ~15,000 entries with fields like job_title, salary_usd, required_skills, years_experience, company_location, etc.

## Key Goals & Questions Addressed:

* Skill Premium: Which technical skills (e.g., Python, SQL, PyTorch, Kubernetes) offer the highest salary increase when combined?
* Market Rate: What is the median and adjusted salary for roles like Data Scientist, Machine Learning Engineer, and Data Analyst based on experience level?
* Geographic Trends: How do salaries for identical AI/Data roles vary across major European job markets?


## 🛠️ Skills Demonstrated

This project showcases a full-stack data analysis workflow:

*   **Data Cleaning & Wrangling:** Handled missing values, normalized currencies, standardized strings, and reshaped data using `Pandas` and `NumPy`.
*   **Data Imputation:** Used group-based mean imputation for salary data to maintain dataset integrity.
*   **Feature Engineering:** Created new features like `experience_level` from raw years and `salary_eur` from USD conversions.
*   **Data Transformation:** Exploded the `required_skills` column to create a long-format dataset ideal for analysis.
*   **Data Visualization:** Built an interactive Tableau dashboard to present the insights clearly and effectively.
*   **Tools:** Python, Pandas, NumPy, Tableau.

## 🔑 Key Insights

* Top-Paying Skills: Combinations like Python + SQL + AWS or PyTorch + Kubernetes often boost salaries by 20-30% in roles like Machine Learning Engineer. In Germany and Switzerland, these can exceed €120k for Senior levels.
* Location Impact: Switzerland and Germany lead with median salaries ~€90k-€130k for mid-senior roles, while countries like France or Ireland average 10-15% lower.
* Experience Matters: Entry-level (0-2 years) roles median ~€25k-€45k; Experts (13+ years) can hit €145k+.
* Role Breakdown (Median Realistic Salaries in EUR):
 <img width="1113" height="319" alt="image" src="https://github.com/user-attachments/assets/543f114c-e909-4ea8-9036-c7e3f8896f69" />
* Full insights in the cleaned CSV and Tableau dashboard.

## 📁 Repository Structure
├── 📄 README.md # You are here

├── 📜 script.py # Main Python cleaning & transformation script

├── 📊 ai_job_dataset_messy_1.csv # Original messy dataset (not included in repo)

├── 📈 Cleaned_dataset_1.csv # Final cleaned dataset (output of script.py)

└── 🎨 [[Tableau_Dashboard Link]](https://public.tableau.com/views/EUAISkillsSalaries20242025/Dashboard?:language=en-US&publish=yes&:sid=&:display_count=n&:origin=viz_share_link) 


## About Me
I'm Cristian Valenzuela, a data enthusiast passionate about AI and analytics. This project showcases my skills in data cleaning, Python scripting, and visualization. Connect with me on [LinkedIn](https://www.linkedin.com/in/cristianvalenzuelaarcos/) for discussions or collaborations!
If you find this useful, star the repo or share your thoughts!


# AI Job Market Analysis 2025: Skills & Salary Insights 🇪🇺

[Tableau Dashboard Preview](https://public.tableau.com/views/EUAISkillsSalaries20242025/Dashboard?:language=en-US&publish=yes&:sid=&:display_count=n&:origin=viz_share_link) 

![alt text](image-1.png)

## 📊 Project Overview

This data analytics project delves into the European AI job market for 2024/2025. By cleaning and analyzing a messy, real-world dataset, I uncovered the relationships between **technical skills, years of experience, and compensation** for roles like Data Scientist, Machine Learning Engineer, AI Product Manager, and others

Key Goals & Questions Addressed:

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

## 📁 Repository Structure
├── 📄 README.md # You are here

├── 📜 script.py # Main Python cleaning & transformation script

├── 📊 ai_job_dataset_messy_1.csv # Original messy dataset (not included in repo)

├── 📈 Cleaned_dataset_1.csv # Final cleaned dataset (output of script.py)

└── 🎨 [[Tableau_Dashboard Link]](https://public.tableau.com/views/EUAISkillsSalaries20242025/Dashboard?:language=en-US&publish=yes&:sid=&:display_count=n&:origin=viz_share_link) 

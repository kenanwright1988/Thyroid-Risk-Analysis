# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Thyroid Cancer Risk Analysis – Data Analytics Project

## Project Overview
Introduction
Thyroid cancer is one of the fastest-growing cancer diagnoses worldwide, with risk factors ranging from genetic predisposition to environmental exposure. This project aims to provide an in-depth analysis of thyroid cancer risk factors using a large-scale dataset. By leveraging data analytics and visualization, we seek to uncover key insights into how demographic, environmental, and medical indicators contribute to thyroid cancer risk.
## Objective
The primary goal of this project is to identify and analyze the most significant risk factors associated with thyroid cancer using a data-driven approach. This involves exploring the relationships between demographic attributes (age, gender, ethnicity, country), medical indicators (TSH, T3, T4 levels), and lifestyle/environmental risk factors (radiation exposure, iodine deficiency, family history, obesity, smoking, and diabetes).
Furthermore, the project aims to detect potential biases in the dataset, ensuring fairness in predictive analysis and identifying any data-driven disparities in thyroid cancer risk.


## Key Deliverables
1.	Data Cleaning and Preprocessing – Handling missing values, feature engineering, and ensuring data consistency.
2.	Exploratory Data Analysis (EDA) – Statistical summaries, correlation analysis, and trend identification.
3.	Data Visualization – Graphical representation of key insights using bar charts, scatter plots, heatmaps, and interactive dashboards.
4.	Bias Detection & Fairness Analysis – Identifying and mitigating potential data biases.
5.	Predictive Insights – Hypothesis validation and recommendations based on findings.
6.	Interactive Dashboard – A user-friendly interface to present findings to both technical and non-technical stakeholders.

## Dataset Content
The dataset consists of 212,691 records with 17 attributes, simulating real-world thyroid cancer risk factors. The dataset includes a mix of demographic, environmental, and medical attributes, such as:
* Demographics: Age, Gender, Country, Ethnicity
* Medical Indicators: TSH (Thyroid-Stimulating Hormone), T3, T4 levels, Nodule Size
* Risk Factors: Family History, Radiation Exposure, Iodine Deficiency, Smoking, Obesity, Diabetes
* Outcome Variables: Thyroid Cancer Risk (Low, Medium, High), Diagnosis (Benign, Malignant)
This dataset is valuable for machine learning modeling, bias detection, fairness analysis, and medical research simulations in the domain of thyroid cancer risk assessment.

## Business Requirements
The analysis is guided by the following business requirements:
1.	Risk Factor Identification:
*	Determine the most critical factors contributing to thyroid cancer.
*	Evaluate how environmental exposure and medical conditions influence risk levels.
2.	Demographic Impact Analysis:
*	Assess variations in thyroid cancer risk based on age, gender, and ethnicity.
*	Identify high-risk geographical regions.
3.	Bias Detection & Fairness Analysis:
*	Identify any imbalances in the dataset that could skew analytical outcomes.
*	Ensure findings are generalizable across diverse populations.
4.	Data-Driven Decision Support:
*	Provide actionable insights for medical professionals, policymakers, and researchers.
*	Develop an interactive dashboard for stakeholders to explore findings.

## Hypotheses & Validation Approach
Hypothesis 1:
Age and gender influence thyroid cancer risk, with older individuals and females having a higher probability.
* Validation: Use box plots and regression analysis to explore how cancer risk varies across different age groups and gender distributions.

Hypothesis 2:
Certain countries and ethnicities have a higher prevalence of thyroid cancer due to genetic and environmental factors.
* Validation: Conduct geospatial analysis and visualize the distribution of thyroid cancer cases across different regions.

## Project Plan
1.	Data Acquisition & Cleaning:
* Load the dataset and handle missing values.
* Standardize data formats (e.g., categorical encoding, numerical scaling).
* Address any inconsistencies in variable definitions.
2.	Exploratory Data Analysis (EDA):
* Conduct summary statistics and distribution analysis.
* Examine correlations between thyroid cancer risk and various features.
3.	Feature Engineering & Selection:
* Create new features such as a composite risk score based on multiple risk factors.
* Perform feature selection using statistical tests.
4.	Data Visualization & Insights Generation:
* Develop plots to explore trends and patterns.
* Create comparative analyses between high-risk and low-risk groups.
5.	Dashboard Development:
* Build an interactive dashboard for easy exploration of findings.
6.	Final Reporting & Recommendations:
* Summarize findings and present actionable recommendations.

## Analysis Techniques Used
1.	Descriptive Statistics: Mean, median, variance analysis.
2.	Correlation Analysis: Pearson/Spearman correlation to identify key relationships.
3.	Chi-Square Tests: Used for evaluating categorical relationships (e.g., gender vs. cancer risk).
4.	Logistic Regression: Assessing the predictive value of medical indicators.
5.	Decision Trees & Classification Models: To improve predictive analysis of cancer diagnosis.
6.	Fairness & Bias Detection: Identifying imbalances in demographic representation.

## Ethical Considerations
* Bias & Fairness: The dataset leans towards certain ethnicities and countries, which may introduce bias. Addressed by balancing the data using resampling techniques.
* Privacy Concerns: The dataset does not contain personally identifiable information (PII).
* Transparency: All methods used are documented for reproducibility.

## Dashboard Design
* Home Page: Overview of thyroid cancer risk factors.
* Risk Factors Analysis Page: Interactive charts showing the correlation of different risk factors.
* Demographics Page: Geographical and demographic distribution insights.
* Predictive Insights Page: Machine learning-based predictions on cancer risk.

## Unfixed Bugs & Limitations
* Data Bias: Some demographic groups may be underrepresented.
* Visualization Performance: Large dataset size may slow down interactive charts.
* Missing Values: Some missing medical data may impact analysis accuracy.

## Development Roadmap
Challenges & Solutions:
* Data Imbalance: Addressed via resampling and reweighting techniques.
* Feature Selection Complexity: Used correlation analysis to select the most impactful features.
## Next Steps & Future Skills to Learn:
* Implementing deep learning models for better risk prediction.
* Advanced geospatial analytics for risk mapping.

## Main Data Analysis Libraries
Library	Usage
* Pandas - Data manipulation, cleaning
* NumPy	- Numerical operations
* Matplotlib & Seaborn - Data visualization
* Scikit-learn - Statistical tests & modeling
* Plotly - Interactive visualizations
 
 ## Credits
* ChatGPT: Assisted with ideation, structuring analysis, and optimizing Python code.
* GitHub Copilot: Provided code suggestions for visualization and statistical testing.
* Code Institute LMS: Provided best practices and foundational knowledge.



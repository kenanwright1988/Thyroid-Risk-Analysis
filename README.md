# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Thyroid Cancer Risk Analysis – Data Analytics Project

## Project Overview
Thyroid cancer is one of the fastest-growing cancer diagnoses worldwide, with risk factors ranging from genetic predisposition to environmental exposure. This project aims to provide an in-depth analysis of the dataset and uncover key insights into which demographics are at risk of having thyroid cancer!  [Uploading image.png…]()

## Objective
The primary goal of this project is to identify and analyze the demographic with different levels of thyroid cancer risk, using a data-driven approach. This involves exploring the relationships between demographic attributes such as age, gender, ethnicity, country and family history. Furthermore, the project aims to detect potential biases in the dataset and identify any data-driven disparities in thyroid cancer risk.

## Key Deliverables
1.	Data Cleaning and Preprocessing – Handling missing values, feature engineering, and ensuring data consistency.
2.	Exploratory Data Analysis (EDA) – Statistical summaries, correlation analysis, and trend identification.
3.	Data Visualization – Graphical representation of key insights using bar charts, box plots, maps, and interactive dashboards.
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

https://www.kaggle.com/datasets/ankushpanday1/thyroid-cancer-risk-prediction-dataset

## Medical Requirements
The analysis is guided by the following medical requirements:
1.	Demographic Impact Analysis:
   *	Assess variations in thyroid cancer risk based on age, gender, and ethnicity.
   *	Identify high-risk geographical regions.
2.	Bias Detection & Fairness Analysis:
   *	Identify any imbalances in the dataset that could skew analytical outcomes.
   *	Ensure findings are generalizable across diverse populations.
3.	Data-Driven Decision Support:
   *	Provide actionable insights for medical professionals, policymakers, and researchers.
   *	Develop an interactive dashboard for stakeholders to explore findings.

## Hypothesis & Validation Approach
Hypothesis: Which demographic has the higher chance of having thyriod cancer?
Hypothesis 1:
Age and gender influence thyroid cancer risk, with older individuals and females having a higher probability.
   * Validation: Use box plots and regression analysis to explore how cancer risk varies across different age groups and gender distributions.

Hypothesis 2:
Certain countries and ethnicities have a higher prevalence of thyroid cancer due to genetic and environmental factors.
   * Validation: Conduct geospatial analysis and visualize the distribution of thyroid cancer cases across different regions.

## Project Plan
# 1.	Data Acquisition & Cleaning:
     * Load the dataset and handle missing values.
     * Standardize data formats (e.g., categorical encoding, numerical scaling).
     * Address any inconsistencies in variable definitions.
# 2.	Exploratory Data Analysis (EDA):
     * Conduct summary statistics and distribution analysis.
     * Examine correlations between thyroid cancer risk and various features.
# 3.	Feature Engineering & Selection:
     * Perform feature selection using statistical tests.
# 4.	Data Visualization & Insights Generation:
     * Develop plots to explore patterns.
     * Create comparative analyses between high-risk and low-risk groups.
# 5.	Dashboard Development:
     * Build an interactive dashboard for easy exploration of findings.
# 6.	Final Reporting & Recommendations:
     * Summarize findings and present actionable recommendations.

## Analysis Techniques Used
1.	Descriptive Statistics: Mean, median, variance analysis.
2.	Correlation Analysis: Pearson/Spearman correlation to identify key relationships.
3.	Chi-Square Tests: Used for evaluating categorical relationships (e.g., gender vs. cancer risk).
4.	Logistic Regression: Assessing the predictive value of medical indicators.
5.	Fairness & Bias Detection: Identifying imbalances in demographic representation.

## Ethical Considerations
   * Bias & Fairness: The dataset leans towards certain ethnicities and countries, which may introduce bias as Caucasion population had higher records of data but we couldn't risk resampling without potentially damaging the findings for this ethnic group.
   * Privacy Concerns: The dataset does not contain personally identifiable information (PII).
   * Transparency: All methods used are documented for reproducibility.

## Dashboard Design
   * Home Page: Overview of thyroid cancer risk demographics.
   * Demographics section : Geographical and demographic distribution insights
   * Risk Factors Analysis: Interactive charts showing the correlation of different risk factors.

# ![image](https://github.com/user-attachments/assets/6891482a-0992-445e-ab45-e7bef98a70a6)

## Unfixed Bugs & Limitations
   * Data Bias: Some demographic groups may be underrepresented.
   * Visualization Performance: Large dataset size may slow down interactive charts.


## Development Roadmap
Challenges & Solutions:
   * Data Imbalance: Addressed via resampling and reweighting techniques.
   * Github collaboration: Issues with loading and updating files across different devices, troubleshooted and sorted it out, everyone needed more practice.

## Next Steps & Future Skills to Learn:
   * Implementing deep learning models for better risk prediction.
   * Advanced geospatial analytics for risk mapping.
   * Reduce bias without damaging findings.

## Main Data Analysis Libraries
Library	Usage
   * Pandas - Data manipulation, cleaning
   * NumPy	- Numerical operations
   * Matplotlib & Seaborn - Data visualization
   * Scikit-learn - Statistical tests & modeling
   * Plotly - Interactive visualizations
   * Ipywidgets -  Interactive controls
   * Statsmodel - Ordinal Encoder
 
 ## Credits
* ChatGPT: Assisted with ideation, structuring analysis, and optimizing Python code.
* GitHub Copilot: Provided code suggestions for visualization and statistical testing.
* Code Institute LMS: Provided best practices and foundational knowledge.

## Acknowledgements
We would like to extend our heartfelt gratitude to Vasilica Pavaloi and Niel McEwen for their invaluable guidance and support throughout this project. Their expertise and encouragement have been instrumental in our learning journey. We would also like to thank our team for their brilliant collaboration and insightful feedback, which greatly contributed to the successful completion of this project.

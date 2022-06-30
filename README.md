# Customer-Churn-Prediction
Churn rate is a critical metric of customer satisfaction. Low churn rates mean happy customers; high churn rates mean customers are leaving you. 

## Importance of Customer churn prediction

- Good way to create proactive marketing campaigns targeted at the customers that are about to churn
- Identifying at-risk customers
- Identifying customer pain points
- Identifying strategy/methods to lower churn and increase customer retention

## Churn Prediction workflow

- Defining problem and goal: An important financial institution is interested in analyzing its client database to increase the revenue generated from credit cardholders. They are concern about customers closing their bank accounts after accepting products from other institutions.
- Establishing data source: Some popular sources of churn data are CRM systems, analytics services, and customer feedback.
- Data preparation, exploration, and preprocessing:
- Modeling and testing:
-Deployment and monitoring:


<h2> <align="center">Customer-Churn-Prediction</h1>
<p align="center"><img src="https://tse1.mm.bing.net/th?id=OIP.AhveViSfye8s9xDhHCZXBAEsCU&pid=Api&rs=1&c=1&qlt=95&w=197&h=98" width="500" height="300"></p>


## Host organization:
* <a href="https://github.com/becodeorg"><strong>BeCode</strong></a>(Ghent campus)
<img src="https://becode.org/app/uploads/2021/06/logo-becode.png" alt="Logo" width="200" height="200">
  

## The timeline of the project:
14 days - **20/06/2022 - 01/07/2022**

## Project Goal: 
*Predict those clients with more propensity to close their bank account with the financial institution*


## Dataset details:

BankChurners.csv with attributes:
    (Clientnum, Attrition_flag, Customer_age, Gender, Dependent_count, Education_level, Martial_status, Income_category, card_category, months_on_book, Total_Revolving_Bal, Avg_Open_To_Buy, Total_Trans_Amt, Total_Amt_Chng_Q4_Q1, Total_Trans_Ct, Total_Ct_Chng_Q4_Q1, Avg_Utilization_Ratio, 


## Description:

This project is the Final Project of our AI bootcamp. In this project, we are required to understand the data given, identify which activities should be done, analyze the data using exploratory and visualization, do the data-preprocessing, as well as develop model which relevant with the problem along with the evaluation within a predetermined period of time.

The steps we have taken:
* Understanding the data
* Target Feature Exploration
* Correlations between feature and the attrition flag.
* Statistical exploration of feature that cause customer churn or not  
* Model Evaluation and selection.
* Feature Importance selection. 
  

## Used Language and Libraries:
Python libraries:
* Numpy
* Pandas 
* Scikit-learn
* Matplotlib
* Seaborn 


## Conclusion

The most important features to understand customer credit card churn, are

- Total Transaction Count

- Total Transaction Amount

- Total Revolving Balance

- Total Count Change Q4 to Q1

- Months_Inactive_12_mon 

After several experiments, we can learn that RandomForest may be the best performing model for this data set.

The actual performance of the model is unknown in the real world, because we use SMOTE to adjust the data set.
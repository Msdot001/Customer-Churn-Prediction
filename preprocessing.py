import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def preprocess(data, option):
    """
    This function is to cover all the preprocessing steps on the churn dataframe. It involves selecting important features, encoding categorical data, handling missing values,feature scaling and splitting the data
    """
    #Defining the map function
    def binary_map(feature):
        return feature.map({'Existing Customer':1, 'Attrited Customer':0})
    
    #Drop values based on operational options
    if (option == "Online"):
        columns = ['Customer_Age', 'Dependent_count', 'Education_Level', 'Marital_Status', 'Income_Category', 'Card_Category', 'Months_on_book', 'Total_Relationship_Count','Months_Inactive_12_mon','Contacts_Count_12_mon','Credit_Limit','Total_Revolving_Bal','Avg_Open_To_Buy','Total_Amt_Chng_Q4_Q1','Total_Trans_Amt','Total_Trans_Ct','Total_Ct_Chng_Q4_Q1']
        #Encoding the other categorical categoric features with more than two categories
        df = pd.get_dummies(data).reindex(columns=columns, fill_value=0)
    elif (option == "Batch"):
        pass
        df = data[['Customer_Age', 'Dependent_count', 'Education_Level', 'Marital_Status', 'Income_Category', 'Card_Category',
        'Months_on_book', 'Total_Relationship_Count','Months_Inactive_12_mon','Contacts_Count_12_mon','Credit_Limit','Total_Revolving_Bal',
        'Avg_Open_To_Buy','Total_Amt_Chng_Q4_Q1','Total_Trans_Amt','Total_Trans_Ct','Total_Ct_Chng_Q4_Q1']]
        columns = ['Customer_Age', 'Dependent_count', 'Education_Level', 'Marital_Status', 'Income_Category', 'Card_Category', 'Months_on_book', 'Total_Relationship_Count','Months_Inactive_12_mon','Contacts_Count_12_mon','Credit_Limit','Total_Revolving_Bal','Avg_Open_To_Buy','Total_Amt_Chng_Q4_Q1','Total_Trans_Amt','Total_Trans_Ct','Total_Ct_Chng_Q4_Q1']
        #Encoding the other categorical categoric features with more than two categories
        data = pd.get_dummies(data).reindex(columns=columns, fill_value=0)
    else:
        print("Incorrect operational options")


    #feature scaling
    numeric = data.select_dtypes(exclude=object).columns

    for col in data[numeric]:
        data[col] = MinMaxScaler().fit_transform(data[[col]])
    return data
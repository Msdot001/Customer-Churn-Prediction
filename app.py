#Import libraries
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


#load the model from disk
import joblib
model = joblib.load(r"model2.sav")


#Import python scripts
from preprocessing  import preprocess

def main():
    #Setting Application title
    st.title('Banking Customer Churn Prediction App')

      #Setting Application description
    st.markdown("""
     :dart:  This Streamlit app is made to predict customer churn in a financial institution use case.
    The application is functional for both online prediction and batch data prediction. 
    """)
    st.markdown("<h3></h3>", unsafe_allow_html=True)

    #Setting Application sidebar default
    image = Image.open('Data/App.jpg')
    add_selectbox = st.sidebar.selectbox(
    "How would you like to predict?", ("Online", "Batch"))
    st.sidebar.info('This app is created to predict Customer Churn')
    st.sidebar.image(image)

    if add_selectbox == "Online":
        st.info("Input data below")
        #Based on our optimal features selection
        st.subheader("Demographic data")
        #Gender = st.selectbox('Gender:', ('M', 'F'))
        Customer_Age = st.number_input('Customer_Age:', min_value=0, max_value=73, value=0)
        Dependent_count = st.number_input('Dependent_count',min_value=0, max_value=5, value=0)
        Education_Level = st.selectbox('Education_Level', ('High School','College','Graduate','Post-Graduate', 'Doctorate'))
        Marital_Status = st.selectbox('Marital_Status',('Single', 'Married', 'Divorced'))
        Income_Category = st.selectbox('Income_Category',('Less than $40K', '$40K - $60K', '$60K - $80K','$80K - $120K', '$120K +'))


        st.subheader("Bank Accouunt data")
        Card_Category = st.selectbox('Card_Category',('Blue', 'Silver', 'Gold', 'Platinum'))
        Months_on_book = st.slider('Period of relationship with bank', min_value=0, max_value=60, value=0)
        Total_Relationship_Count = st.number_input('Total number of products held by the customer',min_value=0, max_value=10, value=0)
        Months_Inactive_12_mon = st.slider('Number of months inactive in the last 12 months', min_value=0, max_value=60, value=0)
        Contacts_Count_12_mon = st.number_input('Number of Contacts in the last 12 months',min_value=0, max_value=10, value=0)
        Credit_Limit = st.number_input('Credit Limit on the Credit Card', min_value=0, max_value=40000, value=0)
        Total_Revolving_Bal = st.number_input('The unpaid portion that carries over to the next month when a customer does not pay',min_value=0, max_value=3000, value=0)
        Avg_Open_To_Buy = st.number_input('The average credit available allocated to a specific customer',min_value=0, max_value=40000, value=0)
        Total_Amt_Chng_Q4_Q1 =  st.number_input('Change in Transaction Amount (Q4 over Q1)',min_value=0, max_value=5, value=0) 
        Total_Trans_Amt = st.number_input('Total Transaction Amount',min_value=0, max_value=20000, value=0)
        Total_Trans_Ct = st.number_input('Total Transaction Count (Last 12 months)', min_value=0, max_value=2000, value=0)
        Total_Ct_Chng_Q4_Q1 = st.number_input('Change in Transaction Count (Q4 over Q1)',min_value=0, max_value=10, value=0)
        Avg_Utilization_Ratio = st.number_input('Measures how much credit you are using compared to how much you have available',min_value=0, max_value=1, value=0)

        data = {
                'Customer_Age': Customer_Age,
                #'Gender': Gender,
                'Dependent_count':Dependent_count,
                'Education_Level':Education_Level,
                'Marital_Status': Marital_Status,
                'Income_Category':Income_Category,
                'Card_Category': Card_Category,
                'Months_on_book': Months_on_book,
                'Total_Relationship_Count': Total_Relationship_Count,
                'Months_Inactive_12_mon': Months_Inactive_12_mon,
                'Contacts_Count_12_mon': Contacts_Count_12_mon,
                'Credit_Limit': Credit_Limit,
                'Total_Revolving_Bal': Total_Revolving_Bal,
                'Avg_Open_To_Buy': Avg_Open_To_Buy,
                'Total_Amt_Chng_Q4_Q1': Total_Amt_Chng_Q4_Q1,
                'Total_Trans_Amt': Total_Trans_Amt,
                'Total_Trans_Ct	': Total_Trans_Ct,
                'Total_Ct_Chng_Q4_Q1':Total_Ct_Chng_Q4_Q1	, 
                'Avg_Utilization_Ratio': Avg_Utilization_Ratio, 
                }

        features_df = pd.DataFrame.from_dict([data])
        st.markdown("<h3></h3>", unsafe_allow_html=True)
        st.write('Overview of input is shown below')
        st.markdown("<h3></h3>", unsafe_allow_html=True)
        st.dataframe(features_df)


        #Preprocess inputs
        preprocess_df = preprocess(features_df, 'Online')

        prediction = model.predict(preprocess_df)

        if st.button('Predict'):
            if prediction == 1:
                st.warning('Yes, the customer will terminate the service.')
            else:
                st.success('No, the customer is happy with Telco Services.')
        

    else:
        st.subheader("Dataset upload")
        uploaded_file = st.file_uploader("Choose a file")
        if uploaded_file is not None:
            data = pd.read_csv(uploaded_file)
            #Get overview of data
            st.write(data.head())
            st.markdown("<h3></h3>", unsafe_allow_html=True)
            #Preprocess inputs
            preprocess_df = preprocess(data, "Batch")
            if st.button('Predict'):
                #Get batch prediction
                prediction = model.predict(preprocess_df)
                prediction_df = pd.DataFrame(prediction, columns=["Predictions"])
                prediction_df = prediction_df.replace({1:'Yes, the customer will terminate the service.', 
                                                    0:'No, the customer is happy with Telco Services.'})

                st.markdown("<h3></h3>", unsafe_allow_html=True)
                st.subheader('Prediction')
                st.write(prediction_df)
            
if __name__ == '__main__':
        main()

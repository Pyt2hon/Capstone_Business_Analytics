
# Import all necessary libraries
import pandas as pd
import streamlit as st
import pickle
import statsmodels.api as sm
from scipy import stats
import numpy as np
import matplotlib as plt

#data2 = pd.read_csv("healthcare-dataset-stroke-data.csv")
#chart = data2["bmi"].dropna()
#chart.hist(bins = 10)
#st.set_option('deprecation.showPyplotGlobalUse', False)
#st.pyplot(bins = 10)


# Implement function that loads in the healthcare dataset
@st.cache()
def load_data():
    data = pd.read_csv("healthcare-dataset-stroke-data.csv")
    return data.dropna()


# Save it in the variable Stroke_data
Stroke_data = load_data()


# Implement function that loads in the healthcare dataset
@st.cache()
def load_data2():
    data2 = pd.read_csv("Y_distribution.csv")
    return data2.dropna()


# Save it in the variable Stroke_data_distribution
Stroke_data_distribution = load_data2()


@st.cache(allow_output_mutation=True)
def load_model():
    filename = "stroke_model.sav"
    loaded_model = pickle.load(open(filename, "rb"))
    return loaded_model


model = load_model()

Stroke_X = Stroke_data.drop("stroke", axis = 1)


# Set the website title to "Stroke Risk Predictor" using streamlit
st.title("Stroke Risk Predictor")

# Set the header to "Customizable Predictions"
st.header("Customizable Predictions")

# Create 10 objects with the same widths, where the individual variable-names indicate their position
row1_col1, row1_col2 = st.columns([1, 1])
row2_col1, row2_col2 = st.columns([1, 1])
row3_col1, row3_col2 = st.columns([1, 1])
row4_col1, row4_col2 = st.columns([1, 1])
row5_col1, row5_col2 = st.columns([1, 1])

# Set individual titles for each variable
row1_col1.write("Gender")
row1_col2.write("Age")
row2_col1.write("Hypertension")
row2_col2.write("Heart disease")
row3_col1.write("Marriage status")
row3_col2.write("Work type")
row4_col1.write("Residence type")
row4_col2.write("Glucose level")
row5_col1.write("BMI")
row5_col2.write("Smoking status")

# Display a radio button widget for the user to enter the gender
Gender = row1_col1.radio(
    "Enter gender:",
    options=['Male', 'Female', 'Other'], )
row1_col1.write(Gender)

# Display a slider widget for the user to enter integer values from 0 to 120
Age = row1_col2.slider("Enter age:",
                       min_value=0,
                       max_value=120,
                       value=60)  # Set a default value of 60
row1_col2.write(Age)  # Show the user the entered input

# Display a radio widget for the user to enter the hypertension state
Hypertension = row2_col1.radio(
    "Do you have hypertension?",
    options=['Yes', 'No'])
row2_col1.write(Hypertension)  # Show the user the entered input

# Display a radio widget for the user to enter the heart disease state
Heart_disease = row2_col2.radio(
    "Do you suffer from a heart disease?",
    options=['Yes', 'No'])
row2_col2.write(Heart_disease)  # Show the user the entered input

# Display a radio widget for the user to enter the marriage status
Marriage_status = row3_col1.radio(
    "Were you ever married?",
    options=['Yes', 'No'])
row3_col1.write(Marriage_status)  # Show the user the entered input

# Display a select widget for the user to enter the latest type of work
Work_type = row3_col2.selectbox(
    "What is your latest type of work?",
    options=['Private Sector', 'Self-employed', 'Government Job', 'Child/ Student', 'Never worked'])
row3_col2.write(Work_type)  # Shows the user the entered input

# Display a radio widget for the user to enter the residence type
Residence_type = row4_col1.radio("Enter residence type:",
                                 options=['Urban', 'Rural'])
row4_col1.write(Residence_type)  # Show the user the entered input

# Display a slider widget for the user to enter integer values from 0 to 300
Glucose_level = row4_col2.slider("Enter glucose level:",
                                 min_value=0,
                                 max_value=300,
                                 value=150)  # Set a default value of 150
row4_col2.write(Glucose_level)  # Show the user the entered input

# Display a slider widget for the user to enter integer values from 10.3 to 97.6
BMI = row5_col1.slider("Enter BMI:",
                       min_value=Stroke_data["bmi"].min(),  # Set the min value from the dataset as the min_value
                       max_value=Stroke_data["bmi"].max(),  # Set the max value from the dataset as the max_value
                       value=30.0)  # Set a default value of 150
row5_col1.write(BMI)  # Show the user the entered input

# Display a radio widget for the user to enter the smoking status
Smoking_status = row5_col2.radio("Enter your smoking status:",
                                  options=['Never smoked', 'Formerly smoked', 'Smokes', 'Unknown'])
row5_col2.write(Smoking_status)  # Show the user the entered input

st.write(f'The prediction for a stroke for the entered data is:')

# Adds a checkbox
if st.checkbox("Show filtered data", False):
    st.subheader("Raw Data")
    st.write(Stroke_data)

if Gender == "Male":
    v1, v2, v3 = -0.0019, 0, 0

if Gender == "Female":
    v1, v2, v3 = 0, 0, 0

if Gender == "Other":
    v1, v2, v3 = -0, 0, -0.0225

v4 = Age*0.0035

if Hypertension == "Yes":
    v5 = 0.0385

if Hypertension == "No":
    v5 = 0

if Heart_disease == "Yes":
    v6 = 0.0482

if Heart_disease == "No":
    v6 = 0

if Work_type == "Never worked":
    v7, v8, v9, v10 = 0.0339, 0, 0, 0

if Work_type == "Private Sector":
    v7, v8, v9, v10 = 0, 0.0124, 0, 0

if Work_type == "Self-employed":
    v7, v8, v9, v10 = 0, 0, -0.0173, 0

if Work_type == "Child/ Student":
    v7, v8, v9, v10 = 0, 0, 0, 0.0641

if Work_type == "Government Job":
    v7, v8, v9, v10 = 0, 0, 0, 0

if Residence_type == "Urban":
    v11 = 0.0101

if Residence_type == "Rural":
    v11 = 0

v11 = Glucose_level*0.0002
v12 = BMI*-0.0007

if Smoking_status == 'Never smoked':
    v13, v14, v15, v16 = -0.0105, 0, 0, 0

if Smoking_status == "Formerly smoked":
    v13, v14, v15, v16 = 0.0, -0.0029, 0, 0

if Smoking_status == "Smokes":
    v13, v14, v15, v16 = 0, 0, 0, -0.0060

if Smoking_status == "Unknown":
    v13, v14, v15, v16 = 0, 0, 0, 0


Stroke_probability = -0.0931 + v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16

if Stroke_probability >= 0.08:
    Stroke_statement = 1

else:
    Stroke_statement = 0

st.write(Stroke_statement)

if st.checkbox(f"Show more information about new client {i}", False):
    percentile = round(stats.percentileofscore(Stroke_data_distribution["Di"], Stroke_probability), 1)
    
    if percentile > 75:
        statement = "high"
    
    elif percentile > 50:
        statement = "medium"
    
    elif percentile < 50:
        statement = "low"
    
    else:
        st.write("An error has occurred")
    
    st.write(f"With a value of {round(Stroke_probability, 2)} client ranks in the {percentile}."
             f"percentile. That means customer is in a {statement} risk segment!")

uploaded_data = st.file_uploader("Choose a file with Customer Data for predicting Stroke")

if uploaded_data is not None:

    new_customers = pd.read_csv(uploaded_data, on_bad_lines='skip', encoding='ISO-8859-1')
    new_customers = pd.get_dummies(new_customers, drop_first=True)
    new_customers = sm.add_constant(new_customers)

    new_customers["Stroke_prediction"] = model.predict(new_customers)
    new_customers["Stroke_prediction_exact"] = new_customers["Stroke_prediction"]
    new_customers["Stroke_prediction"] = (new_customers["Stroke_prediction"] > 0.08).astype(int)

    st.write(new_customers)

    st.success(f"You successfully scored %i new customers for stroke predictions" % new_customers.shape[0])

    st.download_button(label="Download scored customer data",
                   data=new_customers.to_csv(index=False).encode("utf-8"),
                   file_name="scored_customer_data.csv")

    for i in range(0, (new_customers.shape[0])):
        if st.checkbox(f"Show more information about new client {i}", False):
            percentile2 = round(stats.percentileofscore(Stroke_data_distribution["Di"], new_customers.iloc[i, 18]),1)
            if percentile2 > 75:
                statement2 = "high"
            elif percentile2 > 50:
                statement2 = "medium"
            elif percentile2 < 50:
                statement2 = "low"
            else:
                st.write("An error has occurred")
            st.write(f"With a value of {round(new_customers.iloc[i, 18],2)} client {i} ranks in the {percentile2}."
                     f"percentile. That means customer {i} is in a {statement2} risk segment!")

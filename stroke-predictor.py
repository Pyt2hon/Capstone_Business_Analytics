# Imports all necessary libraries
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib as plt

#data2 = pd.read_csv("healthcare-dataset-stroke-data.csv")
#chart = data2["bmi"].dropna()
#chart.hist(bins = 10)
#st.set_option('deprecation.showPyplotGlobalUse', False)
#st.pyplot(bins = 10)


# Function that loads in the healthcare dataset
@st.cache()
def load_data():
    data = pd.read_csv("healthcare-dataset-stroke-data.csv")
    return data.dropna()


# Saving it in the variable Stroke_data
Stroke_data = load_data()


# Sets the website title to "Stroke Risk Predictor" using streamlit
st.title("Stroke Risk Predictor")

# Sets the header to "Customizable Predictions"
st.header("Customizable Predictions")

# Creates 10 objects with the same widths, where the individual variable-names indicate their position
row1_col1, row1_col2 = st.columns([1, 1])
row2_col1, row2_col2 = st.columns([1, 1])
row3_col1, row3_col2 = st.columns([1, 1])
row4_col1, row4_col2 = st.columns([1, 1])
row5_col1, row5_col2 = st.columns([1, 1])

# Sets individual titles for each variable
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

# Displays a radio button widget for the user to enter the gender
Gender = row1_col1.radio(
    "Enter gender:",
    options=['Male', 'Female', 'Other'], )
row1_col1.write(Gender)

# Displays a slider widget for the user to enter integer values from 0 to 120
Age = row1_col2.slider("Enter age:",
                       min_value=0,
                       max_value=120,
                       value=60)  # Sets a default value of 60
row1_col2.write(Age)  # Shows the user the entered input

# Displays a radio widget for the user to enter the hypertension state
Hypertension = row2_col1.radio(
    "Do you have hypertension?",
    options=['Yes', 'No'])
row2_col1.write(Hypertension)  # Shows the user the entered input

# Displays a radio widget for the user to enter the heart disease state
Heart_disease = row2_col2.radio(
    "Have you ever suffered from a heart disease?",
    options=['Yes', 'No'])
row2_col2.write(Heart_disease)  # Shows the user the entered input

# Displays a radio widget for the user to enter the marriage status
Marriage_status = row3_col1.radio(
    "Were you ever married?",
    options=['Yes', 'No'])
row3_col1.write(Marriage_status)  # Shows the user the entered input

# Displays a select widget for the user to enter the latest type of work
Work_type = row3_col2.selectbox(
    "What is your latest type of work?",
    options=['Private Sector', 'Self-employed', 'Government Job', 'Child/ Student', 'Never worked'])
row3_col2.write(Work_type)  # Shows the user the entered input

# Displays a radio widget for the user to enter the residence type
Residence_type = row4_col1.radio("Enter residence type:",
                                 options=['Urban', 'Rural'])
row4_col1.write(Residence_type)  # Shows the user the entered input

# Displays a slider widget for the user to enter integer values from 0 to 300
Glucose_level = row4_col2.slider("Enter glucose level:",
                                 min_value=0,
                                 max_value=300,
                                 value=150)  # Sets a default value of 150
row4_col2.write(Glucose_level)  # Shows the user the entered input

# Displays a slider widget for the user to enter integer values from 10.3 to 97.6
BMI = row5_col1.slider("Enter BMI:",
                       min_value=Stroke_data["bmi"].min(),  # Sets the min value from the dataset as the min_value
                       max_value=Stroke_data["bmi"].max(),  # Sets the max value from the dataset as the max_value
                       value=30.0)  # Sets a default value of 150
row5_col1.write(BMI)  # Shows the user the entered input

# Displays a radio widget for the user to enter the smoking status
Smoking_status = row5_col2.radio("Enter your smoking status:",
                                  options=['Never smoked', 'Formerly smoked', 'Smokes', 'Unknown'])
row5_col2.write(Smoking_status)  # Shows the user the entered input



st.write(f'Your probability for a stroke is:')

# Adds a checkbox
if st.checkbox("Show filtered data", False):
    st.subheader("Raw Data")
    st.write(Stroke_data)




#st.sidebar.write("costumer-trial-run")
#st.sidebar.button("Click here to run a costumer-trial-run")

#add_selectbox = st.sidebar.selectbox(
#    "How would you like to be contacted?",
#    ("Email", "Home phone", "Mobile phone")
#)

#with st.sidebar:
#    add_radio = st.radio(
#        "Choose a shipping method",
#        ("Standard (5-15 days)", "Express (2-5 days)")
#    )

uploaded_data = st.file_uploader("Choose a file with Customer Data for predicting Stroke")

if uploaded_data is not None:
    new_customers = pd.read_csv(uploaded_data)
    st.write(new_customers)


#@st.cache(allow_output_mutation=True)
#def load_model():
#    filename = "stroke_model_capstone"
#    loaded_model = pickle.load(open(filename, "rb"))
#    return loaded_model
# model = load_model()

#new_customers = pd.get_dummies(new_customers, drop_first = True)
#new_customers["Sroke_prediction"] = model.predict(new_customers)

#st.success(f"You successfully scored %i new customers for stroke predictions" % new_customers.shape)

#st.download_button(label = "Download scored customer data",
#                   data = new_customers.to_csv(index=False).encode("utf-8"),
#                   file_name = "scored:customer_data.csv")

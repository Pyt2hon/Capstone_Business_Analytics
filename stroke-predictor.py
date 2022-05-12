import pandas as pd
import streamlit as st
import numpy as np
import matplotlib as plt

data2 = pd.read_csv("/Users/noa/Desktop/Business Analytics/healthcare-dataset-stroke-data.csv")
chart = data2["bmi"].dropna()
#chart.hist(bins = 10)
#st.set_option('deprecation.showPyplotGlobalUse', False)
#st.pyplot(bins = 10)

@st.cache()
def load_data():
    data = pd.read_csv("/Users/noa/Desktop/Business Analytics/healthcare-dataset-stroke-data.csv")
    return data.dropna()


Stroke_data = load_data()


st.title("Stroke Risk")
st.header("Risk Calculator")

row1_col1, row1_col2 = st.columns([1, 1])
row2_col1, row2_col2 = st.columns([1, 1])
row3_col1, row3_col2 = st.columns([1, 1])
row4_col1, row4_col2 = st.columns([1, 1])
row5_col1, row5_col2 = st.columns([1, 1])

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

Gender = row1_col1.radio(
    "Enter gender:",
    options=['Male', 'Female', 'Other'], )
row1_col1.write(Gender)

Age = row1_col2.slider("Enter age:",
                       min_value=0,
                       max_value=120,
                       value=60)
row1_col2.write(Age)

Hypertension = row2_col1.radio(
    "Do you have hypertension?",
    options=['Yes', 'No'])
row2_col1.write(Hypertension)

Heart_disease = row2_col2.radio(
    "Have you ever suffered from a heart disease?",
    options=['Yes', 'No'])
row2_col2.write(Heart_disease)

Marriage_status = row3_col1.radio(
    "Were you ever married?",
    options=['Yes', 'No'])
row3_col1.write(Marriage_status)

Work_type = row3_col2.selectbox(
    "What is your latest type of work?",
    options=['Private Sector', 'Self-employed', 'Government Job', 'Child/ Student', 'Never worked'])
row3_col2.write(Work_type)

Residence_type = row4_col1.radio("Enter residence type:",
                                 options=['Urban', 'Rural'])
row4_col1.write(Residence_type)

Glucose_level = row4_col2.slider("Enter glucose level:",
                                 min_value=0,
                                 max_value=300,
                                 value=150)
row4_col2.write(Glucose_level)

BMI = row5_col1.slider("Enter BMI:",
                       min_value=Stroke_data["bmi"].min(),
                       max_value=Stroke_data["bmi"].max(),
                       value=30.0)
row5_col1.write(BMI)

Smoking_status = row5_col2.radio("Enter your smoking status:",
                                  options=['Never smoked', 'Formerly smoked', 'Smokes', 'Unknown'])
row5_col2.write(Smoking_status)

st.write(f'Your probability for a stroke is:')

# add checkbox
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

#new_customers = pd.get_dummies(new_customers, drop_first = True)
#new_customers["Sroke_prediction"] = model.predict(new_customers)

#st.success(f"You successfully scored %i new customers for stroke predictions" % new_customers.shape)

#st.download_button(label = "Download scored customer data",
#                   data = new_customers.to_csv(index=False).encode("utf-8"),
#                   file_name = "scored:customer_data.csv")


# Import all necessary libraries
import pandas as pd
import streamlit as st
import pickle
import statsmodels.api as sm
from scipy import stats
import numpy
import matplotlib.pyplot as plt


# Implement function that loads in the healthcare dataset
@st.cache()
def load_data():
    data = pd.read_csv("healthcare-dataset-stroke-data.csv")
    return data.dropna()


# Save it in the variable Stroke_data
Stroke_data = load_data()

# Drop the column stroke
Stroke_X = Stroke_data.drop("stroke", axis=1)


# Implement function that loads in the healthcare dataset
@st.cache()
def load_data2():
    data2 = pd.read_csv("Y_distribution.csv")
    return data2.dropna()


# Save it in the variable Stroke_data_distribution
Stroke_data_distribution = load_data2()


# Implement function that loads in the model
@st.cache(allow_output_mutation=True)
def load_model():
    filename = "stroke_model.sav"
    loaded_model = pickle.load(open(filename, "rb"))
    return loaded_model


# Save the model in the variable model
model = load_model()


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

# Implement all the parameters from the model for the customizable prediction
# For the variable "Gender"
if Gender == "Male":
    v1, v2, v3 = -0.0019, 0, 0

if Gender == "Female":
    v1, v2, v3 = 0, 0, 0

if Gender == "Other":
    v1, v2, v3 = -0, 0, -0.0225

# For the variable "Age"
v4 = Age*0.0035

# For the variable "Hypertension"
if Hypertension == "Yes":
    v5 = 0.0385

if Hypertension == "No":
    v5 = 0

# For the variable "Heart_disease"
if Heart_disease == "Yes":
    v6 = 0.0482

if Heart_disease == "No":
    v6 = 0

# For the variable "Work_type"
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

# For the variable "Residence_type"
if Residence_type == "Urban":
    v11 = 0.0101

if Residence_type == "Rural":
    v11 = 0

# For the variable "Glucose_level"
v12 = Glucose_level*0.0002

# For the variable "BMI"
v13 = BMI*-0.0007

# For the variable "Smoking_status"
if Smoking_status == 'Never smoked':
    v14, v15, v16, v17 = -0.0105, 0, 0, 0

if Smoking_status == "Formerly smoked":
    v14, v15, v16, v17 = 0.0, -0.0029, 0, 0

if Smoking_status == "Smokes":
    v14, v15, v16, v17 = 0, 0, 0, -0.0060

if Smoking_status == "Unknown":
    v14, v15, v16, v17 = 0, 0, 0, 0

# Calculate the Stroke probability by adding the values and the constant of the OLS model
Stroke_probability = -0.0931+v1+v2+v3+v4+v5+v6+v7+v8+v9+v10+v11+v12+v13+v14+v15+v16+v17

# Set a threshold and create a statement
if Stroke_probability >= 0.08:
    Stroke_statement = "At risk!"

# Create a statement for low-risk-customers
else:
    Stroke_statement = "Not at risk!"

# Print the statement
st.subheader(f'The prediction for the entered data is: {Stroke_statement}')

# Add a checkbox that returns a statement considering their stroke value and the distribution of the stroke dataset
if st.checkbox(f"Show more information about client", False):
    percentile = round(stats.percentileofscore(Stroke_data_distribution["Di"], Stroke_probability), 1)

    if percentile > 90:  # Set the percentile threshold for high risk patients at 90
        statement = "high"

    elif percentile > 75:  # Set the percentile threshold for medium-high risk patients at 75
        statement = "medium-high"

    elif percentile > 50:  # Set the percentile threshold for medium risk patients at 50
        statement = "medium"

    elif percentile < 50:  # Set the percentile threshold for low risk patients at below 50
        statement = "low"

    else:
        st.write("An error has occurred")

    # Print a statement regarding the new information
    st.write(f"With a value of {round(Stroke_probability, 2)} client ranks in the {percentile}."
             f"percentile. That means customer is in a {statement} risk segment!")

# Add a checkbox that returns a plot considering their stroke value and the distribution of the stroke dataset
if st.checkbox(f"Show a plot regarding their position in the risk distribution", True):

    # Instantiate a plot using matplotlib.pyplot with an appropriate size
    fig, ax = plt.subplots(figsize=(20, 10))

    # Create an arrow visualizing that the customer's stroke risk is above 0.3
    if Stroke_probability > 0.3:
        colors = ["#4169E1"] * 38  # Set the color of the distribution to blue
        plt.arrow(0.25, 30, 0.08, 0, head_width=10, head_length=0.015, fc='r', ec='r', )  # Set fitting attributes
        plt.text(0.26, 35, r"Customer's value is above: 0.3")  # Text to help understand the arrow

    # Create an arrow visualizing that the customer's stroke risk is between -0.07 and -0.06
    elif (Stroke_probability < -0.06) and (Stroke_probability > -0.07):
        colors = ["#4169E1"] * int(100 * Stroke_probability + 8) + ['#FF0000'] + ["#4169E1"] * int(
            (37 - 100 * Stroke_probability + 8))  # Blue for all bins except the one containing the customer (red)
        t = numpy.linspace(0, 360, 360)  # Make a circle to later distort it to an ellipse
        x1 = 0.02 * numpy.cos(numpy.radians(t)) - 0.08  # Set x-radius to 0.02 and set center to -0.08
        y1 = 10 * numpy.sin(numpy.radians(t))  # Set y-radius to 10 and set center to 0 (default)
        plt.plot(x1, y1, color='red')  # Plot the ellipse

    # Create an arrow visualizing that the customer's stroke risk is between 0.25 and 0.3
    elif (Stroke_probability < 0.3) and (Stroke_probability > 0.25):
        colors = ["#4169E1"] * int(100 * Stroke_probability + 8) + ['#FF0000'] + ["#4169E1"] * int(
            (37 - 100 * Stroke_probability + 8))  # Blue for all bins except the one containing the customer (red)
        t = numpy.linspace(0, 360, 360)  # Make a circle to later distort it to an ellipse
        x2 = 0.03 * numpy.cos(numpy.radians(t)) + 0.28  # Set x-radius to 0.03 and set center to 0.28
        y2 = 10 * numpy.sin(numpy.radians(t))  # Set y-radius to 10 and set center to 0 (default)
        plt.plot(x2, y2, color='red')  # Plot the ellipse

    # Create an arrow visualizing that the customer's stroke risk is below -0.08
    elif Stroke_probability < -0.08:
        colors = ["#4169E1"] * 38  # Set the color of the distribution to blue
        plt.arrow(-0.06, 30, -0.07, 0, head_width=10, head_length=0.01, fc='r', ec='r')  # Set fitting attributes
        plt.text(-0.128, 35, r"Customer's value is below: -0.08")    # Text to help understand the arrow

    # Set colors flexible to which bin is red (depending of the stroke value "Stroke_probability")
    else:
        colors = ["#4169E1"] * int(100 * Stroke_probability + 8) + ['#FF0000'] + ["#4169E1"] * int(
            (37 - 100 * Stroke_probability + 8))  # Blue for all bins except the one containing the customer (red)

    # Plot the distribution with 38 bins
    n, bins, patches = plt.hist(Stroke_data_distribution["Di"], bins=38)

    # Adapt the color of each patch
    for color, patch in zip(colors, patches):
        patch.set_facecolor(color)

    # Plot title with fitting fontsize
    plt.title('Distribution of stroke values', fontsize=25)

    # Plot xlabel with fitting fontsize
    plt.xlabel('Stroke value', fontsize=20)

    # Plot ylabel with fitting fontsize
    plt.ylabel('Amount of individuals', fontsize=20)

    # Plot a text helping the user with fitting fontsize
    plt.text(0.1, 350, r"Customer's risk increases in this direction", fontsize=20)
    plt.text(0.1, 320, r"-------------------------------------------------------->", fontsize=20)

    # Plot the figure
    st.pyplot(fig)


# Give the option to upload data
uploaded_data = st.file_uploader("Choose a file with Customer Data for predicting Stroke")

# Create actions if data is uploaded
if uploaded_data is not None:

    # Read in csv, get dummies and add a constant to predict values
    new_customers = pd.read_csv(uploaded_data, on_bad_lines='skip', encoding='ISO-8859-1')
    new_customers = pd.get_dummies(new_customers, drop_first=True)
    new_customers = sm.add_constant(new_customers)

    # Predict values and save the in a new column
    new_customers["Stroke_prediction"] = model.predict(new_customers)
    new_customers["Stroke_prediction_exact"] = new_customers["Stroke_prediction"]  # For exact values
    new_customers["Stroke_prediction"] = (new_customers["Stroke_prediction"] > 0.08).astype(int)  # With threshold

    # Print out the newly generated dataset
    st.write(new_customers)

    # Print success message
    st.success(f"You successfully scored %i new customers for stroke predictions" % new_customers.shape[0])

    # Give the option to Download the scored customer data
    st.download_button(label="Download scored customer data",
                       data=new_customers.to_csv(index=False).encode("utf-8"),
                       file_name="scored_customer_data.csv")

    # Create a for loop to return a statement considering their stroke value and the distribution of the stroke dataset
    for i in range(0, (new_customers.shape[0])):
        if st.checkbox(f"Show more information about new client {i}", False):
            percentile2 = round(stats.percentileofscore(Stroke_data_distribution["Di"], new_customers.iloc[i, 18]), 1)

            if percentile2 > 90:  # Set the percentile threshold for high risk patients at 90
                statement2 = "high"

            elif percentile2 > 70:  # Set the percentile threshold for medium-high risk patients at 70
                statement2 = "medium-high"

            elif percentile2 > 50:  # Set the percentile threshold for medium risk patients at 50
                statement2 = "medium"

            elif percentile2 < 50:  # Set the percentile threshold for low risk patients at below 50
                statement2 = "low"

            else:
                st.write("An error has occurred")

            # Print a summarizing text
            st.write(f"With a value of {round(new_customers.iloc[i, 18],2)} client {i} ranks in the {percentile2}."
                     f"percentile. That means customer {i} is in a {statement2} risk segment!")

    for i in range(0, (new_customers.shape[0])):
        if st.checkbox(f"Show even more information about new client {i}", False):
            # Instantiate a plot using matplotlib.pyplot with an appropriate size
            fig2, ax = plt.subplots(figsize=(20, 10))

            # Create an arrow visualizing that the customer's stroke risk is above 0.3
            if new_customers.iloc[i, 18] > 0.3:
                colors = ["#4169E1"] * 38  # Set the color of the distribution to blue
                plt.arrow(0.25, 30, 0.08, 0, head_width=10, head_length=0.015, fc='r',
                          ec='r', )  # Set fitting attributes
                plt.text(0.26, 35, r"Customer's value is above: 0.3")  # Text to help understand the arrow

            # Create an arrow visualizing that the customer's stroke risk is between -0.07 and -0.06
            elif (new_customers.iloc[i, 18] < -0.06) and (new_customers.iloc[i, 18] > -0.07):
                colors = ["#4169E1"] * int(100 * new_customers.iloc[i, 18] + 8) + ['#FF0000'] + ["#4169E1"] * int(
                    (
                                37 - 100 * new_customers.iloc[i, 18] + 8))  # Set blue and red bins
                t = numpy.linspace(0, 360, 360)  # Make a circle to later distort it to an ellipse
                x1 = 0.02 * numpy.cos(numpy.radians(t)) - 0.08  # Set x-radius to 0.02 and set center to -0.08
                y1 = 10 * numpy.sin(numpy.radians(t))  # Set y-radius to 10 and set center to 0 (default)
                plt.plot(x1, y1, color='red')  # Plot the ellipse

            # Create an arrow visualizing that the customer's stroke risk is between 0.25 and 0.3
            elif (new_customers.iloc[i, 18] < 0.3) and (new_customers.iloc[i, 18] > 0.25):
                colors = ["#4169E1"] * int(100 * new_customers.iloc[i, 18] + 8) + ['#FF0000'] + ["#4169E1"] * int(
                    (37 - 100 * new_customers.iloc[i, 18] + 8))  # Set blue and red bins
                t = numpy.linspace(0, 360, 360)  # Make a circle to later distort it to an ellipse
                x2 = 0.03 * numpy.cos(numpy.radians(t)) + 0.28  # Set x-radius to 0.03 and set center to 0.28
                y2 = 10 * numpy.sin(numpy.radians(t))  # Set y-radius to 10 and set center to 0 (default)
                plt.plot(x2, y2, color='red')  # Plot the ellipse

            # Create an arrow visualizing that the customer's stroke risk is below -0.08
            elif new_customers.iloc[i, 18] < -0.08:
                colors = ["#4169E1"] * 38  # Set the color of the distribution to blue
                plt.arrow(-0.06, 30, -0.07, 0, head_width=10, head_length=0.01, fc='r',
                          ec='r')  # Set fitting attributes
                plt.text(-0.128, 35, r"Customer's value is below: -0.08")  # Text to help understand the arrow

            # Set colors flexible to which bin is red (depending of the stroke value "Stroke_probability")
            else:
                colors = ["#4169E1"] * int(100 * new_customers.iloc[i, 18] + 8) + ['#FF0000'] + ["#4169E1"] * int(
                    (37 - 100 * new_customers.iloc[i, 18] + 8))  # Set blue and red bins

            # Plot the distribution with 38 bins
            n, bins, patches = plt.hist(Stroke_data_distribution["Di"], bins=38)

            # Adapt the color of each patch
            for color, patch in zip(colors, patches):
                patch.set_facecolor(color)

            # Plot title with fitting fontsize
            plt.title('Distribution of stroke values', fontsize=25)

            # Plot xlabel with fitting fontsize
            plt.xlabel('Stroke value', fontsize=20)

            # Plot ylabel with fitting fontsize
            plt.ylabel('Amount of individuals', fontsize=20)

            # Plot a text helping the user with fitting fontsize
            plt.text(0.1, 350, r"Customer's risk increases in this direction", fontsize=20)
            plt.text(0.1, 320, r"-------------------------------------------------------->", fontsize=20)

            # Plot the figure
            st.pyplot(fig2)

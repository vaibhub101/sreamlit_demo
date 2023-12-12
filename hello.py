import streamlit as st
import pandas as pd 

st.write("hey this is my first streamlit app!")

st.title("Welcome")

# Heading in bold letters
st.header("Python Developer")

# sub header
st.subheader("Fresher")

# Display any message
st.info("Information details of user")

# For any warning message
st.warning("Complete the project in time or else get fired!")

#input the value
x = st.text_input("Candidate Name : ")
# write 
st.write(f"Hi {x} ", "Lets begin your career journey")

#error message
#st.error("Wrong")

#Markdown
#st.markdown(":moon:")

# write a caption
st.caption("Write a caption")

# display mathematical expression
# st.latex(r''' a+b x^2 + c ''')

# Widgets
st.checkbox('Lets Begin')

# button
st.button("click")

st.radio("Select your gender", ["Male", "Female", "other"])

# Select box
st.selectbox("Pick your career", ["ML Engineer", "Data Analyst", "DevOps Engineer", "Java Developer"])

# multiselect
st.multiselect("Past Experience", ["Trainee", "Internship", "Engineer role" ])

# Rating by selectslider
st.select_slider("How would you rate yourself in Python", ["Beginner", "Average", "Good", "Excellent"])

st.slider("Familiarity with AWS and DevOps", 1, 10)

st.write("If you want to transit your career into data field, here is some salary structure of random employees in India working as the Data scientist. Have a look")

# import the csv file
data = pd.read_csv("salary_dataset.csv")
st.write(data)

st.file_uploader("Upload your CV/Resume")


import streamlit as st

st.title("BMI calculator")

#enter the weight
weight = st.number_input("enter your weight in kgs: ", value=1)

height_status = st.radio("enter the format of height: ", ('meter', 'feet', 'centimeters'))

if(height_status == 'meter'):
    height = st.number_input('meter:', value=1)
    bmi = (weight/(height**2))

elif(height_status == 'feet'):
    height = st.number_input('feet:', value=1)
    bmi = (weight/((height/3.28)**2))

if(height_status == 'centimeters'):
    height = st.number_input('centimeters:', value=1)
    bmi = (weight/((height/100)**2))

if(st.button("calculate BMI")):
    st.text("your BMI index is {}".format(bmi))

    if (bmi < 16):
        st.error("You are Extremely Underweight")
    elif (bmi >= 16 and bmi < 18.5):
        st.warning("You are Underweight")
    elif (bmi >= 18.5 and bmi < 25):
        st.success("Healthy")
    elif (bmi >= 25 and bmi < 30):
        st.warning("Overweight")
    elif (bmi >= 30):
        st.error("Extremely Overweight")




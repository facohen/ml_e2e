import streamlit as st
import pandas as pd
from joblib import load
import streamlit as st
from sklearn.linear_model import ElasticNet


#Loading up the Regression model we created
model = load('./models/ml/diabetes_v2.joblib')

#Caching the model for faster loading
@st.cache


# Define the prediction function
def predict(age, sex, bmi, bp, s1, s2, s3, s4, s5, s6):

    prediction = model.predict(pd.DataFrame([[age, sex, bmi, bp, s1, s2, s3, s4, s5, s6]], columns=['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']))
    return prediction


st.title('Diabetes Progression Predictor')
st.image("""https://www.thestreet.com/.image/ar_4:3%2Cc_fill%2Ccs_srgb%2Cq_auto:good%2Cw_1200/MTY4NjUwNDYyNTYzNDExNTkx/why-dominion-diamonds-second-trip-to-the-block-may-be-different.png""")
st.header('Enter the characteristics of the patient:')
age = st.number_input('age:', min_value=0.1, max_value=1.0, value=0.5)
sex = st.number_input('sex:', min_value=0.1, max_value=1.0, value=0.5)
bmi = st.number_input('bmi:', min_value=0.1, max_value=1.0, value=0.5)
bp = st.number_input('bp:', min_value=0.1, max_value=1.0, value=0.5)
s1 = st.number_input('s1:', min_value=0.1, max_value=1.0, value=0.5)
s2 = st.number_input('s2:', min_value=0.1, max_value=1.0, value=0.5)
s3 = st.number_input('s3:', min_value=0.1, max_value=1.0, value=0.5)
s4 = st.number_input('s4:', min_value=0.1, max_value=1.0, value=0.5)
s5 = st.number_input('s5:', min_value=0.1, max_value=1.0, value=0.5)
s6 = st.number_input('s6:', min_value=0.1, max_value=1.0, value=0.5)

#cut = st.selectbox('Cut Rating:', ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])

if st.button('Predict Progression'):
    progression = predict(age, sex, bmi, bp, s1, s2, s3, s4, s5, s6)
    st.success(f'The predicted progression of diabetes is  ${progression[0]:.2f} ')
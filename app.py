import streamlit as st
import pickle
import numpy as np
import pandas as pd

# load model
with open("ford_xgb_model.pkl","rb") as file:
    model = pickle.load(file)

with open("columns.pkl","rb") as file:
    columns = pickle.load(file)

with open("scaler.pkl","rb") as file:
    scaler = pickle.load(file)

st.markdown("""
<style>

.block-container {
    padding-top: 0rem !important;
}

header[data-testid="stHeader"] {
    display: none;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #667eea, #764ba2);
}

.main-title {
    text-align:center;
    color:white;
    font-size:72px;
    font-weight:800;
    text-shadow: 3px 3px 10px rgba(0,0,0,0.3)
}

.pred-box {
    background:white;
    padding:20px;
    border-radius:15px;
    text-align:center;
    box-shadow:0px 4px 15px rgba(0,0,0,0.2);
}

.price {
    color:#4CAF50;
    font-size:35px;
    font-weight:bold;
}

.stButton>button {
    width:100%;
    background:linear-gradient(90deg,#FF512F,#DD2476);
    color:white;
    border:none;
    border-radius:10px;
    height:50px;
    font-size:18px;
    font-weight:bold;
}

.stButton>button:hover {
    background:linear-gradient(90deg,#DD2476,#FF512F);
}
            
.stApp label{
    font-size:48px !important;
            font-weight:700 !important;
            color:white !important;  
    }

</style>
""", unsafe_allow_html=True)

st.markdown("""
    '<h1 style="text-align:center;
            color:white;">🚗 Ford Car Price Predictor</h1>""",
    unsafe_allow_html=True
)

# st.title("Ford Car Price Prediction")

year = st.number_input("Year 📅",min_value=1990,max_value=2030,value=2018)
mileage = st.number_input("Mileage ⛽",min_value=0,value=30000)
tax = st.number_input("Tax 💸",min_value=0,value=150)
mpg = st.number_input("MPG ⛽",min_value=0.0,value=50.0)
engineSize = st.number_input("Engine Size 🔧",min_value=0.0,value=1.5)
model_name = st.selectbox("Model 🏷️",["Fiesta","Focus","Kuga","Mondeo","EcoSport","Puma"])
transmission = st.selectbox("Transmission ⚙️",["Manual","Automatic","Semi-Automatic"])
fuelType = st.selectbox("Fueal Type ⛽ / 🔋 (EV)",["Petrol","Diesel","Hybrid","Electric"])


if st.button("Predict Price"):
    data = pd.DataFrame(
        np.zeros((1,len(columns))),
        columns=columns
    )

    data["year"]=year
    data["mileage"]=mileage
    data["tax"]=tax
    data["mpg"]=mpg
    data["engineSize"]=engineSize

    model_col = f"model_{model_name}"
    trans_col = f"transmission_{transmission}"
    fuel_col = f"fuelType_{fuelType}"

    if model_col in data.columns:
        data[model_col]=1
    
    if trans_col in data.columns:
        data[trans_col]=1
    
    if fuel_col in data.columns:
        data[fuel_col]=1

    num_cols = ["year","mileage","tax","mpg"]
    data[num_cols] = scaler.transform(data[num_cols])

    prediction = model.predict(data)

    # st.success(f"Predicted Price: ${prediction[0]:,.2f}")
    st.markdown(f"""
<div class="pred-box">
    <h2>Estimated Car Price 🎯</h2>
    <p class="price">£{prediction[0]:,.2f}</p>
</div>
""", unsafe_allow_html=True)
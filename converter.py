import streamlit as st  # type: ignore

st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f4f4f9;
            color: #333;
        }
        .head {
            font-size: 36px;
            text-align: center;
            font-weight: bold;
            background: linear-gradient(90deg,#16a085,#3498db);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .footer{
            display: block;
            text-align: center;
            margin-left: auto;
            margin-right: auto;
            padding: 10px;
            border-radius: 8px;
            font-size: 20px;
            font-weight: 600;
            width: 50%;
            color: black;
            background: linear-gradient(90deg,#66D2CE,#4CC9FE)
        }

        .stNumberInput {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 50%;
        }        
        .stButton > button {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%; 
            padding: 15px;
            font weight: bold; 
        }
        .stButton > button:hover {
            background-color: #4CC9FE;
            border: 2px solid #4CC9FE;
        }      
        .bottom { 
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 50%;
            padding: 12px;
            text-align:center;
            color:white;
            background-color: #66D2CE;
            font-size: 20px;
            border-radius: 8px;
            margin-top: 20px;
            margin-bottom: 20px
        }
    </style>
""", unsafe_allow_html=True)


st.markdown(f'<h1 class="head"> Unit converter using python and streamlit </h1>',unsafe_allow_html=True)

list = st.selectbox("Select unit",["Length","Weight","Temperature"],index=None,placeholder="Select Unit")


col1,col2 = st.columns(2,gap="medium")
if list == "Length":
    with col1:
        from_units = st.selectbox("From Unit",["Meter","Kilometer","Centimeter","Milimeter","Miles","Yards","Feet","Inches"])
    with col2:
        to_units = st.selectbox("To Unit",["Kilometer","Meter","Centimeter","Milimeter","Miles","Yards","Feet","Inches"])
elif list == "Weight":
    with col1:
        from_units = st.selectbox("From Unit",["Kilogram","Gram","Pound","Ounce"])
    with col2:
        to_units = st.selectbox("To Unit",["Gram","kilogram","Pound","Ounce"])
elif list == "Temperature":
    with col1:
        from_units = st.selectbox("From Unit",["kelvin","celcius","fahranheit"])
    with col2:
        to_units = st.selectbox("To Unit",["celcius","kelvin","fahranheit"])

value = st.number_input("Enter a number", 1, step=1)

def length_Weight(value, from_unit, to_unit):
    length_units = {
        "Meter": 1.0,
        "Kilometer": 0.001,
        "Centimeter": 100,
        "Milimeter": 1000,
        "Miles": 0.000621371,
        "Yards": 1.09361,
        "Feet": 3.28084,
        "Inches": 39.3701,
        "Kilogram": 1.0,
        "Gram": 1000,
        "Pound": 2.20462,
        "Ounce": 35.274,
    }
    return round(((value / length_units[from_unit]) * length_units[to_unit]),4)

def temp(value, from_unit, to_unit):
    if from_unit=="kelvin" and to_unit=="fahranheit":
        return round((value - 273.15) * 9/5 + 32,4)
    elif from_unit=="kelvin" and to_unit=="celcius":
        return round(value - 273.15,4)
    elif from_unit=="celcius" and to_unit=="fahranheit":
        return round((value * 9/5) + 32,4)
    elif from_unit=="celcius" and to_unit=="kelvin":
        return round(value + 273.15,4)
    elif from_unit=="fahranheit" and to_unit=="kelvin":
        return round((value - 32) * 5/9 + 273.15,4)
    elif from_unit=="fahranheit" and to_unit=="celcius":
        return round((value - 32) * 5/9,4)
    
if st.button("Convert unit"):
    if list == "Length" or list == "Weight":
        result = length_Weight(value, from_units, to_units)
        st.markdown(f"""<div class = "bottom"> {result}<br>
        {value} {from_units} is equal to {result} {to_units}.</div>""",unsafe_allow_html=True)
    elif list == "Temperature":
        result = temp(value, from_units, to_units)
        st.markdown(f"""<div class = "bottom"> {result}<br>
        {value} {from_units} is equal to {result} {to_units}.</div>""",unsafe_allow_html=True)

st.markdown(f'<div class="footer"> Developed by Faiqa Farooq </div>',unsafe_allow_html=True)



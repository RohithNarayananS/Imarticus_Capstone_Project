import streamlit as st
import pickle
import pandas as pd
from PIL import Image


def load_model():
    with open('saved_steps.pkl','rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

xgb_model = data["Model"]


def SDecoder(output):
    i = output
    if i == 0.0:
        i = " # Normal # - * Your are doing a good job, your baby's health is good & normal, you can proceed with your usual prescribed checkups. *"
    elif i == 1.0:
        i = " # Suspect # - ** Take care of your health and activities; you should meet your Gynaecologist for precautionary reasons **"
    elif i == 2.0:
        i = " # At Risk # - *** You must get admitted to a hospital as soon as possible ***"
    else:
        i = " # At Risk # - *** You must get admitted to a hospital as soon as possible ***"
    return i


def show_predict_page():
    st.title(" Maternal Health Risk Testing")

    logo = Image.open("OIP.jpg")
    st.image(logo)

    st.write("""## We need certain Important Information to produce the Test Results, so kindly Download the Form file, fill it using your Cardiotocography (CTG) report and upload it for testing""")
    
    def convert_df(df):
        return df.to_csv().encode('utf-8')

    DF=pd.read_csv('Form.csv')
    csv = convert_df(DF)

    download_file=st.download_button(label="Download Form as CSV file", data=csv, file_name='Form.csv', mime='text/csv')
    st.write("#### Fill the form by given order and the values must be seperated by a comma ','")
    colA, colB, colC , colD = st.columns(4)
    with colA:
        display_form=colA.button("Display Form")
    with colB:
        pass
    with colC:
        pass
    with colD:
        pass


    if download_file is not None:
        DF=pd.read_csv('Form.csv')
        if display_form:
            clear_form=st.button("Clear Form")  
            st.write(DF)
            if clear_form:
                st.write(" ")
    

    uploaded_file = st.file_uploader("Upload your csv file", type=["csv"], accept_multiple_files=False )
    col1, col2, col3 , col4 = st.columns(4)
    with col1:
        display=col1.button("Display Data")
    with col2:
        pass
    with col3 :
        pass
    with col4:
        predict=col4.button("Predict")
    
    if uploaded_file is not None:
        df=pd.read_csv(uploaded_file)
        if display:
            clear=st.button("Clear")  
            st.write(df)
            if clear:
                st.write("")
        if predict:        
            Result=xgb_model.predict(df)
            result=SDecoder(Result)
            st.subheader(f"The Predicted Status is {result}")
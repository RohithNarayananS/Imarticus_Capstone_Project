import streamlit as st
from PIL import Image


def show_explore_page():
    B1=st.button('Influence of Fetal Heart Rate')
    if B1:
        FHR = Image.open("FHR.png")
        st.image(FHR)
    B2=st.button('Accuracy of the Test')
    if B2:
        Acc = Image.open("Acc.png")
        st.image(Acc)
    B3=st.button('Factors Affecting The Result')
    if B3:
        Feature = Image.open("Feature.png")
        st.image(Feature)
    B4=st.button('Correlation of the Attributes')
    if B4:
        corr = Image.open("corr.png")
        st.image(corr)  
    B5=st.button('Influence of Prolongued Deceleration')
    if B5:
        Dece = Image.open("Dece.png")
        st.image(Dece)        
    clear=st.button('Clear Graph')     
    if clear:
        st.write(" ")
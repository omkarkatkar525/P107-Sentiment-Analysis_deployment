# -*- coding: utf-8 -*-
"""P107-Sentiment Analysis_deployment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1d7yzQzM7r4-WCXBIwNn754s7JsSJ6DzV
"""

import numpy as np
import pickle
import pandas as pd

import streamlit as st 

from PIL import Image


clf = pickle.load(open('nlp_model.pkl', 'rb'))
cv=pickle.load(open('transfomers.pkl','rb'))

def welcome():
    return "Welcome All"


def sentiment_analysis(message):
    data=[message]
    vect = cv.transform(data).toarray()
    my_prediction = clf.predict(vect)
    
    print(my_prediction)
    return my_prediction


def main():
    st.title("Sentiment Analysis")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    message = st.text_input("Review","Type Here")
  
    result=""
    if st.button("Predict"):
        result=sentiment_analysis(message)
    if result==2:
     p='positive Review'
    elif result==1:
     Neu='Neutral Review'
    elif result==0:
     Neg='Negative Review'
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Built By Omkar Katkar")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    

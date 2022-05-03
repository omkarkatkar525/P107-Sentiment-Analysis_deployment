# -*- coding: utf-8 -*-
"""P107-Sentiment Analysis_deployment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1d7yzQzM7r4-WCXBIwNn754s7JsSJ6DzV
"""

import numpy as np
import pickle
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

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
    if my_prediction==2:
     prediction='Positive Review'
    elif my_prediction==1:
     prediction='Neutral Review'
    elif my_prediction==0:
     prediction='Negative Review'
    print(prediction)
    return prediction


def main():
    st.title("Sentiment Analysis")
    html_temp = """
    <div style="background-color:orange;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Sentiment Analysis ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    message = st.text_input("Review","Type Here")
  
    result=""
    if st.button("Predict"):
        result=sentiment_analysis(message)
   
    st.success(result)
    pred_test=clf.predict_proba(vect)
    st.text(pred_test[:1,1:2])
    
    if st.button("About"):
        st.text("Built By Omkar Katkar")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()

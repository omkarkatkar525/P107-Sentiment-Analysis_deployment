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


clf = pickle.load(open('nlp_random_model.pkl', 'rb'))
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
    
  
    return prediction

def probability(message):
    data_1=[message]
    vect_1= cv.transform(data_1).toarray()
    pred_test = clf.predict_proba(vect_1)
    a=pred_test[:1,0:1]
    b=pred_test[:1,1:2]
    c=pred_test[:1,2:3]
    d=st.write(f"Probability of Negative Review : {a}")
    e=st.write(f"Probability of Neutral Review : {b}")
    f=st.write(f"Probability of Positive Review : {c}")
    return d,e,f

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
    prob=""
   
    if st.button("Predict"):
        result=sentiment_analysis(message)
        st.success(result)
        prob=probability(message) 
        
      
    if st.button("About"):
        st.text("Built By Omkar Katkar")
        

if __name__=='__main__':
    main()


from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
from pickle import load
import streamlit as st 

from PIL import Image
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
#from sklearn.externals import joblib
import joblib

clf=pickle.load(open("nlp_model.pkl",'rb'))
cv=pickle.load(open("transfomers.pkl",'rb'))


def welcome():
    return "Welcome All"

def predict_note_authentication(message):
    data = [message]
    vect = cv.transform(data).toarray()
    my_prediction = clf.predict(vect)
    #print(my_prediction)
    return render_template('result.html',prediction = my_prediction)

def main():
 st.title("Sentiment analysis")
    html_temp = """<div style="background-color:indigo;padding:10px"><h2 style="color:LightSalmon;text-align:center;">Streamlit Incident Impact Prediction ML App </h2></div>"""
    st.markdown(html_temp,unsafe_allow_html=True)
    message = st.text_input("index","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(message)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Built By Omkar Katkar")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()

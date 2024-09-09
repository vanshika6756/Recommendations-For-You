import streamlit as st;
import pickle
from flask import Flask,render_template,request
import pandas as pd
import pickle
import numpy as np

st.header("Top 50 most popular books")

popular_df=pickle.load(open('popular_df27.pkl','rb'))
# print(type(list((popular_df['Book-Title']))))

popular_df=list((popular_df['Book-Title']))
# print(popular_df[1])

for i in range(len(popular_df)):
    st.write(f'{i+1} {popular_df[i]}')
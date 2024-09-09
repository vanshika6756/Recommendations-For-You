import streamlit as st;
import pickle
from flask import Flask,render_template,request
import pandas as pd
import pickle
import numpy as np

st.header("Book Recommendations For You")




pt27=pickle.load(open('pt27.pkl','rb'))
similarity=pickle.load(open('similarity27.pkl','rb'))
final_rating=pickle.load(open('final_ratings27.pkl','rb'))
book=pickle.load(open('book27.pkl','rb'))


input=st.selectbox('search a book',list(book['Book-Title']))




def recommend():
    user_input = input

    # Check if user input exists in the index
    if user_input in pt27.index:
        index = np.where(pt27.index == user_input)[0][0]
        similar_items = sorted(list(enumerate(similarity[index])), key=lambda x: x[1], reverse=True)[1:5]

        data = []
        for i in similar_items:
            item = []
            temp_df = book[book['Book-Title'] == pt27.index[i[0]]]
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

            data.append(item)
        for i in data:
            st.write(i)
    else:
        st.write(f"Book with title '{user_input}' not found in the dataset.")

if st.button('Recommend'):
    recommend()
import streamlit as st
import pickle
pickle_in=open('Salaryprediction.pkl','rb')
model=pickle.load(pickle_in)
years=st.number_input('years of experience')
if st.button('PREDICT'):
  salary=model.predict([['years']])
  st.success(f'salary predicted is {salary}')


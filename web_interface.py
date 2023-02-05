import streamlit as st
import functions

st.title('Simple Task List')
st.subheader('Use this page to track your daily tasks')

st.write('Your tasks:')
for task in functions.get_tasks():
    st.checkbox(task)

st.text_input(label= '', placeholder='Enter a new task...')

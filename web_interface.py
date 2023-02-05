import streamlit as st
import functions

task_list = functions.get_tasks()


def add_task():
    new_task = st.session_state['task_input']
    task_list.append(new_task + '\n')
    functions.save_tasks(task_list)


st.title('Simple Task List')
st.subheader('Use this page to track your daily tasks')
st.write('Your tasks:')

for index, task in enumerate(task_list):
    checkbox = st.checkbox(task, key=task)
    if checkbox:
        task_list.pop(index)
        functions.save_tasks(task_list)
        del st.session_state[task]
        st.experimental_rerun()

st.text_input(label='text entry', label_visibility='hidden',
              placeholder='Enter a new task...', on_change=add_task,
              key='task_input')

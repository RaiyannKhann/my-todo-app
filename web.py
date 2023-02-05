import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state['todo']+'\n'
    todos.append(new_todo)
    functions.write_todos(todos)


st.title("My To-Do App")
st.subheader("These are your to-dos:")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label=' ', placeholder='enter todo here...', on_change=add_todo, key='todo')


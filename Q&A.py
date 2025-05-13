import streamlit as st
from LLM import read

st.title('Q&A NLP App')

st.write("What would you like to do?")

option = 'Q&A'

st.header("Please enter the text below.")

user_input = st.text_input("Enter your text here: ")

question=''
if option =='Q&A':
    question = st.text_input("Please enter what you're looking for in the text: ")
    
if st.button("Run"):            
    
    if option == 'Q&A':
        
        output = read(user_input, question)
        
        st.write("")
        
        st.write('##### {}'.format('Answer for the provided lookup and text: ',))
        
        st.write(output)


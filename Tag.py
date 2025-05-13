import streamlit as st
from LLM import tag

st.title('Word Tagging NLP App')
st.header("Please enter the text below.")

user_input = st.text_input("Enter your text here: ")

if st.button("Run"):
  
  output = tag(user_input)
  
  st.write("")
  st.write('##### {}'.format('Tagging for the provided text: ',))
  
  for result in output:
      st.write(result)
      
   

import streamlit as st
from LLM import unmask

st.title('Word Unmasking NLP App')

st.header("Please enter the text below.")
user_input = st.text_input("Enter your text here: ")

if st.button("Run"):

  output = unmask(user_input)
  
  st.write("")
  
  st.write('##### {}'.format('Answer for the provided mask: ',))
  
  for result in output:
      st.write(result)

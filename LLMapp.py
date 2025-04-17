import streamlit as st
from LLMpy import classify

st.title('Sentiment Classification')

st.header("Please enter the text you would like to classify.")

user_input = st.text_input("Enter your text here: ")

if user_input:
    output = classify(user_input)
    
    st.write("")
    
    st.write('##### {}'.format('Classification for the provided text: ',))

    st.write('## {}'.format(output[0]['label']+':&nbsp;&nbsp;'+str(output[0]['score']*100)+'%'))

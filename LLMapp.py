import streamlit as st
from LLM import classify, summarize, tag, read, generate, translate, unmask

st.title('Multi-function NLP App')

st.write("What would you like to do?")

options = ['Classify', 'Summarize', 'Tag', 'Q&A', 'Generate', 'Translate', 'Unmask']

option = st.selectbox("Choose an option:", options)

if option == 'Generate':
    st.write('Please note that the maximum allowed input for the generator is 50 tokens.')

st.header("Please enter the text below.")

user_input = st.text_input("Enter your text here: ")

question=''
if option =='Q&A':
    question = st.text_input("Please enter what you're looking for in the text: ")

language=''
if option == "Translate":
    language = st.text_input("Enter target language (e.g., French, Deutsch):")

if st.button("Run"):

    if option == 'Classify':
        
        output = classify(user_input)
        
        st.write("")
        
        st.write('##### {}'.format('Classification for the provided text: ',))

        st.write('## {}'.format(output[0]['label']+':&nbsp;&nbsp;'+str(output[0]['score']*100)+'%'))

    elif option == 'Summarize':
        
        output = summarize(user_input)
        
        st.write("")
        
        st.write('##### {}'.format('Summerization for the provided text: ',))
        
        st.write(output)
        
    elif option == 'Tag':
        
        output = tag(user_input)
        
        st.write("")
        
        st.write('##### {}'.format('Tagging for the provided text: ',))
        
        for result in output:
            st.write(result)
            
    elif option == 'Q&A':
        
        output = read(user_input, question)
        
        st.write("")
        
        st.write('##### {}'.format('Answer for the provided lookup and text: ',))
        
        st.write(output)

    elif option == 'Generate':
        output = generate(user_input)
        
        st.write("")
        
        st.write('##### {}'.format('Generated text: ',))
        
        st.write(output)
        
    elif option == 'Translate':
        output = translate(user_input,language)
        
        st.write("")
        
        st.write('##### {}'.format('Translated text: ',))
        
        st.write(output)
        
    elif option == 'Unmask':
        
        output = unmask(user_input)
        
        st.write("")
        
        st.write('##### {}'.format('Answer for the provided mask: ',))
        
        for result in output:
            st.write(result)

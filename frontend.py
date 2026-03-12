from rag_pipeline import answer_query, retrieve_docs, llm_model

# setup stramlit updload pdf functionality
import streamlit as st


uploaded_file = st.file_uploader("Choose a PDF file", type="pdf", accept_multiple_files=False)


# step 2 chatbot skelton (question answering)
user_query = st.text_area("Enter Your Prompt: ",height=150, placeholder="Ask Anything!")

ask_question = st.button("Ask Question")

if ask_question:
    
    if uploaded_file:
        
        st.chat_message("user").write(user_query)
    
        # RAG Pipline
        retrieved_docs = retrieve_docs(user_query)
        response = answer_query(retrieved_docs, llm_model, user_query)
        # fixed_response = "Hi this is a fixed response to test the chatbot functionality."
        st.chat_message("user").write(response)
        
    else:
        st.error("Please upload a PDF file before asking a question.")
        
    


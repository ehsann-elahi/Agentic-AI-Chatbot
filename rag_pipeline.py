from langchain_ollama import ChatOllama
from vector_database import faiss_db
from langchain_core.prompts import ChatPromptTemplate

# setup llm model with Ollama

llm_model = ChatOllama(
    model="deepseek-r1",
    temperature=0
)

def retrieve_docs(query):
    return faiss_db.similarity_search(query)


def get_context(documents):
    context = "\n".join([doc.page_content for doc in documents])
    return context

custom_prompt_template = """
Use the piece of information provided to answer the question.
If you don't know the answer, say you don't know. Don't provide any information that is not in the context.
Always use all the information provided in the context to answer the question.
Don't provide anything out of the context. Always use all the information provided in the context to answer the question. 
Question: {question}
Context: {context}
Answer:
"""

def answer_query(documents, model, query):
    context = get_context(documents)
    prompt = ChatPromptTemplate.from_template(custom_prompt_template)
    chain = prompt | model
    return chain.invoke({"question": query, "context": context})


# question = "What is the Universal Declaration of Human Rights?"
# retrieved_docs = retrieve_docs(question)
# print("AI Lawyer: ", answer_query(retrieved_docs, llm_model, question))

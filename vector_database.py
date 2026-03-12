# uploaded a load raw pdf file
from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS


pdf_directory = 'pdfs/'

def upload_pdf(file):
    with open(pdf_directory + file.name, "wb") as f:
        f.write(file.getbuffer())
        

def load_pdf(file_path):
    loader = PDFPlumberLoader(file_path)
    documents = loader.load()
    return documents


# file_path = 'udhr_booklet_en_web.pdf'
# documents = load_pdf(file_path)
# print(len(documents))



# create chunks

def create_chunks(documents):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200, add_start_index=True)
    text_chunks = text_splitter.split_documents(documents)
    return text_chunks
    
file_path = "pdfs/udhr_booklet_en_web.pdf"

documents = load_pdf(file_path)
# print("Documents: ",len(documents))
text_chunks = create_chunks(documents)

# print("Text chunks: ",len(text_chunks))
        
        
# step3 Setup embeddings(with Deepseekr1 with ollama locally)

ollama_model = "nomic-embed-text"
def get_embedding_model(ollama_model):
    embeddings = OllamaEmbeddings(model=ollama_model)
    return embeddings


# step4 create vector database with FAISS

FAISS_DB_PATH = "vectorstore/db_faiss"
faiss_db=FAISS.from_documents(text_chunks, get_embedding_model(ollama_model))
faiss_db.save_local(FAISS_DB_PATH)
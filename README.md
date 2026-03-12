1)Environment Setup

Using Pipenv

Pipenv is a tool that manages dependencies and virtual environments for Python projects.

Install Pipenv if you don't have it:

pip install pipenv
Navigate to the project directory and create a virtual environment:

pipenv install
Activate the virtual environment:

pipenv shell
(Optional) Install any additional dependencies:

pipenv install <package_name>

2)Running the Project


The project consists of three Python files, each corresponding to a different phase of the project:

To run the App directly
streamlit run main.py
To run app in different phases
Phase 1: Run the first phase using:

streamlit run frontend.py
Phase 2: Run the second phase using:

python vector_database.py
Phase 3: Run the third phase using:

python rag_pipeline.py
Ensure that all dependencies are installed before running the scripts.


3)Make sure to Download Ollama Locally

For Embedding and save in faiss db
ollama pull mxbai-embed-large

For Deepseek-r1
ollama pull deepseek-r1

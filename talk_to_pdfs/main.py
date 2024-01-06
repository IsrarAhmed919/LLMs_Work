import os
import warnings
from langchain.document_loaders import UnstructuredPDFLoader
from langchain.indexes import VectorstoreIndexCreator



class ASK_PDF:
    def __init__(self):
        os.environ['OPENAI_API_KEY'] = '' # add your open ai api key here

    def vectorize(self, text_folder):
        warnings.filterwarnings("ignore")
        loaders = [UnstructuredPDFLoader(os.path.join(text_folder, fn)) for fn in os.listdir(text_folder)] 
        index = VectorstoreIndexCreator().from_loaders(loaders)
        warnings.resetwarnings()
        return index
    
    def ask_pdf(self, index, query):
        warnings.filterwarnings("ignore")
        result=index.query(query)
        warnings.resetwarnings()
        return result
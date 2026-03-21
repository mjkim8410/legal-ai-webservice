from parser import DocParser
from dbmanager import DBManager

def query(query_text=""):
    # 1. Initialize parser and DB
    parser = DocParser()  # same model used for embeddings
    db_manager = DBManager()  # loads persisted DB automatically

    # 3. Create embedding for the query
    query_embedding = parser.embed(query_text).tolist()  # convert numpy -> list for Chroma

    # 4. Query Chroma
    context = ""
    # context += "### Current Law ###\n"
    current_context = db_manager.query(query_embedding, n_results=3, current=True) 
    context += current_context
    # context += "\n### Important!!!: Upcoming Changes, not yet in effect ###\n"
    # future_context = db_manager.query(query_embedding, n_results=1, current=False)   
    # context += future_context

    return context
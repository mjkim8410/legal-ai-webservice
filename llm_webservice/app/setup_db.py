from .parser import DocParser
from .dbmanager import DBManager
import os

INPUT_FOLDER = "data/docx"

def init_db():
    parser = DocParser()
    print("DocParser initialized.")

    db_manager = DBManager()  # PersistentClient will keep data on disk
    print("DBManager initialized.")

    # Only add docs if the collection is empty
    if db_manager.collection.count() == 0:
        for file in os.listdir(INPUT_FOLDER):
            if not file.lower().endswith(".docx"):
                continue
            print(f"Processing {file}")
            input_path = os.path.join(INPUT_FOLDER, file)
            text = parser.read_docx(input_path)
            statute, abbreviation, articles = parser.chunk_by_article(text)

            parsed_articles = []
            for article in articles:
                parsed_article = parser.parse_article(statute, abbreviation, article)
                if parsed_article:
                    parsed_articles.append(parsed_article)

            embedded_articles = []
            for parsed_article in parsed_articles:
                parsed_article["embedding"] = parser.embed(parsed_article["body"])
                embedded_articles.append(parsed_article)

            db_manager.add_docs(embedded_articles)
    else:
        print("DB already initialized. Skipping .docx parsing.")
    
    return db_manager
    
    




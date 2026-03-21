import chromadb
from chromadb.config import Settings
import uuid
import os

class DBManager:
    def __init__(self, persist_dir="./chroma_db", collection_name="rag_db"):
        import os
        os.makedirs(persist_dir, exist_ok=True)

        # Use the new PersistentClient for disk persistence
        self.client = chromadb.PersistentClient(path=persist_dir)
        self.collection = self.client.get_or_create_collection(collection_name)

    def add_qa(self, qa_pairs, embeddings):
        ids = [str(uuid.uuid4()) for _ in qa_pairs]

        documents = [q for q, _ in qa_pairs]

        metadatas = [
            {
                "answer": a,
                "type": "qa"
            }
            for _, a in qa_pairs
        ]

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas
        )

    def add_docs(self, embedded_articles):
        """
        embedded_articles: list of dicts, each with keys:
            'statute', 'abbreviation', 'article', 'title', 'body', 'embedding'
        """
        ids = [str(uuid.uuid4()) for _ in embedded_articles]

        documents = [a["body"] for a in embedded_articles]  # the text to store
        embeddings = [a["embedding"].tolist() for a in embedded_articles]  # numpy -> list for Chroma

        metadatas = [
            {
                "statute": a["statute"] or "",
                "abbreviation": a["abbreviation"] or "",
                "article": a["article"] or "",
                "title": a["title"] or "",
                "status": a["status"] or "",
                "effective_date": a["effective_date"] or "",
                "type": "doc"
            }
            for a in embedded_articles
        ]

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas
        )


    def query(self, query_embedding, n_results=3, current=True):
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results,
            where={"status": "current" if current else "future"}  # filter by article status
        )

        docs = results["documents"][0]
        metas = results["metadatas"][0]

        context = []

        for doc, meta in zip(docs, metas):
            if meta["type"] == "qa":
                context.append(f"Q: {doc}\nA: {meta['answer']}")
            else:
                # Include statute, article, title in the context
                statute = meta.get("statute", "")
                article = meta.get("article", "")
                title = meta.get("title", "")
                header = f"[{statute} | {article} | {title}]"
                context.append(f"{header}\n{doc}")
                if meta.get("status") == "future":
                    effective_date = meta.get("effective_date", "N/A")
                    context.append(f"(Note: This article is not yet in effect. Effective date: {effective_date})")

        return "\n\n".join(context)


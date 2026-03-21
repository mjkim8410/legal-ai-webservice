from pypdf import PdfReader
from sentence_transformers import SentenceTransformer

def read_pdf(file_name):
    reader = PdfReader(file_name)

    text = ""
    for page in reader.pages:
        text += page.extract_text()

    return text


def chunk_text(text, chunk_size=500):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i+chunk_size])
        chunks.append(chunk)

    return chunks

def get_embeddings(chunks):

    model = SentenceTransformer(
        "BAAI/bge-m3"
        )

    embeddings = model.encode(
        chunks,
        normalize_embeddings=True
        )
    
    return embeddings
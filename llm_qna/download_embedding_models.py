from sentence_transformers import SentenceTransformer
import os

models = [
    "BAAI/bge-m3",
    "dragonkue/BGE-m3-ko",
    "kykim/bert-kor-base"
]

os.makedirs("embedding_models", exist_ok=True)

for model_name in models:
    print(f"Downloading {model_name}…")
    model = SentenceTransformer(model_name)
    local_path = os.path.join("embedding_models", model_name.replace("/", "_"))  # e.g., models/BAAI_bge-m3
    model.save(local_path)
    print(f"Saved model locally: {local_path}")
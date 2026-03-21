from huggingface_hub import snapshot_download
import os

'''
mistral_models_path = 'mistral_models/7B-Instruct-v0.3'
os.makedirs(mistral_models_path, exist_ok=True)

snapshot_download(repo_id="mistralai/Mistral-7B-Instruct-v0.3", allow_patterns=["params.json", "consolidated.safetensors", "tokenizer.model.v3"], local_dir=mistral_models_path)
'''

mistral_models_path = 'Qwen/Qwen3.5-9B'
os.makedirs(mistral_models_path, exist_ok=True)

snapshot_download(repo_id="Qwen/Qwen3.5-9B", local_dir=mistral_models_path)

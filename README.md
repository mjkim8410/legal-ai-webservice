# ⚖️ Legal AI Web Service

A modern AI-powered legal question answering system that retrieves relevant legal documents and generates accurate, context-aware answers using a Retrieval-Augmented Generation (RAG) pipeline.

---

## 🚀 Overview

This project is a full-stack web application that allows users to ask legal questions in natural language and receive answers grounded in real legal documents.

It addresses a key limitation of LLMs — hallucination — by integrating **retrieval over legal corpora** before generation.

It combines:

* semantic search over legal texts
* vector database retrieval
* large language model (LLM) generation

to deliver reliable and explainable responses.

---

## 🔥 What I Built

- Designed and implemented a **complete RAG pipeline** from scratch  
- Built a backend API using Flask to handle query processing and inference  
- Implemented semantic search using **ChromaDB vector database**  
- Integrated **embedding model (BGE-m3)** for Korean legal text retrieval  
- Integrated **LLM (Qwen)** for answer generation  
- Optimized inference using **GPU acceleration (PyTorch CUDA)**  
- Developed a React-based frontend for real-time interaction  

---

## ✨ Features

* 🔍 **Natural Language Querying**
  Ask legal questions in Korean

* 📚 **Context-Aware Answers**
  Retrieves relevant legal provisions before generating responses

* ⚡ **GPU-Accelerated Inference**
  Fast embeddings and LLM responses using CUDA

* 🧠 **RAG Architecture**
  Combines retrieval + generation for improved accuracy

* 🌐 **Full-Stack Application**

  * Backend: Flask API
  * Frontend: React (Vite)

---

## 🏗️ System Architecture

```
User Input (React Frontend)
        ↓
Flask API (/ask endpoint)
        ↓
Embedding Model (SentenceTransformers)
        ↓
ChromaDB Vector Search
        ↓
Relevant Legal Context
        ↓
LLM (Qwen)
        ↓
Generated Answer
        ↓
Frontend Display
```

---

## 🛠️ Tech Stack

### Backend

* Python
* Flask
* ChromaDB
* SentenceTransformers
* PyTorch (CUDA)

### Frontend

* React (Vite)
* JavaScript
* Fetch API

### AI / ML

* Embedding Model: BGE-m3 (Korean optimized)
* LLM: Qwen

---

## 📁 Project Structure

```
legal-ai-webservice/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── setup_db.py
│   ├── query_db.py
│   └── qwen.py
├── data/
│   └── docx/              # legal documents
├── frontend/
│   ├── src/
│   └── index.html
├── requirements.txt
├── run.py
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/mjkim8410/legal-ai-webservice.git
cd legal-ai-webservice
```

---

### 2. Backend setup

Create virtual environment:

```
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Install PyTorch with CUDA:

```
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

---

### 3. Run backend

```
python run.py
```

Server runs at:

```
http://127.0.0.1:5000
```

---

### 4. Frontend setup

```
cd frontend
npm install
npm run dev
```

Frontend runs at:

```
http://localhost:5173
```

---

## 📡 API Usage

### POST `/ask`

**Request:**

```json
{
  "query": "개인정보 보호법 위반 시 처벌은?"
}
```

**Response:**

```json
{
  "query": "...",
  "answer": "..."
}
```

---

## ⚙️ Key Design Decisions

### 1. Retrieval-Augmented Generation (RAG)
- Avoided hallucination by grounding responses in retrieved legal documents  
- Improved factual accuracy compared to pure LLM responses  

### 2. Persistent Vector Database
- Precomputed embeddings stored in ChromaDB  
- Eliminated repeated embedding computation → faster response time  

### 3. Shared Model Instances
- Prevented model reloading per request  
- Reduced latency significantly  

### 4. GPU Acceleration
- Used CUDA for embedding + LLM inference  
- Enabled near real-time responses  

---

## 💡 Key Takeaways

- Built a **production-like AI system architecture** combining backend + ML  
- Gained hands-on experience with **RAG, vector databases, and LLM pipelines**  
- Learned how to optimize model inference for real-world usage  
- Understood trade-offs between retrieval quality and generation accuracy  

---

## ⚠️ Notes

* Not intended for production legal advice
* Requires GPU for optimal performance

---

## 🚀 Future Improvements

* Chat-style conversational UI
* Document upload & dynamic indexing
* Model switching (multiple LLMs)
* Answer source highlighting (citations)
* Deployment (Docker / Cloud)

---

## 👤 Author

Minjun Kim
Computer Science Graduate, University of Manchester

---

## 📄 License

This project is for educational and portfolio purposes.

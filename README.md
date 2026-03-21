# ⚖️ Legal AI Web Service

A modern AI-powered legal question answering system that retrieves relevant legal documents and generates accurate, context-aware answers using a Retrieval-Augmented Generation (RAG) pipeline.

---

## 🚀 Overview

This project is a full-stack web application that allows users to ask legal questions in natural language and receive answers grounded in real legal documents.

It combines:

* semantic search over legal texts
* vector database retrieval
* large language model (LLM) generation

to deliver reliable and explainable responses.

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

## 🏗️ Architecture

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

## 🧠 Key Design Decisions

* **Persistent Vector DB**
  Avoids rebuilding embeddings on every run

* **Shared Model Instances**
  Prevents reloading models per request → improves performance

* **GPU Utilization**
  Enables real-time responses for LLM and embeddings

* **Modular Architecture**
  Clear separation between parsing, DB, and inference

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

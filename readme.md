# AI Video Lecture Assistant

This project is a simple Retrieval-Augmented Generation (RAG) application that allows users to ask questions about a lecture video and receive answers based only on that video's transcript.

The application extracts the transcript from a lecture, converts it into embeddings, stores them in a FAISS vector database, and retrieves the most relevant sections to generate answers using an LLM. It also displays the timestamps where the topic is discussed in the video.

---

## Features

- Ask questions related to a lecture video
- Semantic search using FAISS
- Answers generated using an LLM
- Displays relevant timestamps from the lecture
- Simple Streamlit interface

---

## Project Workflow

```
Video
   │
   ▼
Transcript Extraction
   │
   ▼
Text Segmentation
   │
   ▼
Sentence Embeddings
   │
   ▼
FAISS Vector Database
   │
   ▼
Relevant Context Retrieval
   │
   ▼
LLM Response Generation
   │
   ▼
Answer + Timestamp
```

---

## Tech Stack

- Python
- Streamlit
- Sentence Transformers (all-MiniLM-L6-v2)
- FAISS
- Groq API (Llama 3.3 70B)
- Whisper

---

## Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Video-Lecture-Assistant.git
```

Move into the project directory

```bash
cd AI-Video-Lecture-Assistant
```

Install the required libraries

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your Groq API key

```env
GROQ_API_KEY=your_api_key_here
```

Run the Streamlit app

```bash
streamlit run app.py
```

---

## Example

**Question**

> What are Core Web Vitals?

**Answer**

The application retrieves the most relevant transcript chunks, generates an answer using the LLM, and displays the timestamps where the topic is discussed.

---

## Project Structure

```
├── app.py
├── query.py
├── process_video.py
├── segmentation.py
├── build_embeddings.py
├── build_faiss.py
├── embeddings.json
├── segments.json
├── video.index
├── requirements.txt
├── .env
└── README.md
```

---

## What I Learned

While building this project, I learned about:

- Retrieval-Augmented Generation (RAG)
- Semantic search
- Sentence embeddings
- Vector databases using FAISS
- Prompt engineering
- Integrating LLM APIs
- Building simple web applications with Streamlit

---


## Author

**Vishal Kumar Singh**


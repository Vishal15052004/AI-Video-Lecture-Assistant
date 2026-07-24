import json 
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from api_key import client

def format_time(seconds):
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return f"{minutes:02}:{seconds:02}"

#load model
model=SentenceTransformer("all-MiniLM-L6-v2")

#load FAISS index
index=faiss.read_index("video.index")

#load original segments
with open("embeddings.json","r",encoding="utf-8") as f:
    segments=json.load(f)


def ask_question(query):
    

    #convert question into embedding
    query_embedding=model.encode([query],convert_to_numpy=True)

    query_embedding=np.array(query_embedding,dtype="float32")

    #search top 3 similiar chunks
    distances, indices = index.search(query_embedding, 3)

    print("Distances:", distances)
    print("Indices:", indices)


    print("\nMost Relevant Chunk:\n")

    for i in indices[0]:
        print("=" * 60)
        print("Chunk Number:", i)

        print(
        f"Timestamp: {format_time(segments[i]['start'])} --> {format_time(segments[i]['end'])}"
    )
        

        print(segments[i]["text"])

    context = ""

    for i in indices[0]:
        context += f"""
    Timestamp: {format_time(segments[i]['start'])} - {format_time(segments[i]['end'])}

    {segments[i]['text']}
    """

    prompt = f"""
    You are an AI Video Lecture Assistant.

    You must answer ONLY using the lecture transcript provided below.

    Rules:
    1. Give a complete and natural answer.
    2. If information is spread across multiple transcript chunks, combine it into one answer.
    3. Do NOT say "The answer is not explicitly defined".
    4. Do NOT mention the context or transcript.
    5. If the answer is not found, reply exactly:
    "I couldn't find the answer in the video."
    6. At the end, list the relevant timestamps used.

    Lecture Transcript:

    {context}

    Question:
    {query}

    Answer:
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content

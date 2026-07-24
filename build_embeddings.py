from sentence_transformers import SentenceTransformer
import json

#load model

model = SentenceTransformer("all-MiniLM-L6-v2")

#load segments
with open("segments.json", "r", encoding="utf-8") as f:
    segments=json.load(f)

#extract text
texts = [segment["text"] for segment in segments]

#generate embeddings
embeddings = model.encode(
    texts,
    convert_to_numpy=True,
    show_progress_bar=True
)

#adding embeddings to each segment
for segment,embedding in zip(segments,embeddings):
    segment["embedding"]=embedding.tolist()

#save output
with open("embeddings.json", "w", encoding="utf-8") as f:
    json.dump(segments,f,indent=4)

print("embedding donee")


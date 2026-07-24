import json
import numpy as np
import faiss

with open("embeddings.json", "r", encoding="utf-8") as f:
    segments= json.load(f)

embeddings=np.array(
    [segment["embedding"]for segment in segments],
    dtype="float32"
)

dimension = embeddings.shape[1]

index=faiss.IndexFlatL2(dimension)

index.add(embeddings)

faiss.write_index(index,"video.index")

print("faiss index created")
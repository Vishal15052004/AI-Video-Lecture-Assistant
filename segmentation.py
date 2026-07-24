import json

# Load Whisper output
with open("whisper_output.json", "r", encoding="utf-8") as f:
    result = json.load(f)

segments = result["segments"]

CHUNK_SIZE = 700      # Maximum characters per chunk
OVERLAP = 150         # Characters to overlap

chunks = []

current_text = ""
current_start = None
current_end = None

for segment in segments:

    text = segment["text"].strip()

    if current_start is None:
        current_start = segment["start"]

    # If adding this segment keeps us under chunk size
    if len(current_text) + len(text) < CHUNK_SIZE:

        current_text += " " + text
        current_end = segment["end"]

    else:

        chunks.append({
            "text": current_text.strip(),
            "start": current_start,
            "end": current_end
        })

        # Create overlap
        overlap_text = current_text[-OVERLAP:]

        current_text = overlap_text + " " + text
        current_start = segment["start"]
        current_end = segment["end"]

# Save last chunk
if current_text:

    chunks.append({
        "text": current_text.strip(),
        "start": current_start,
        "end": current_end
    })

with open("segments.json", "w", encoding="utf-8") as f:
    json.dump(chunks, f, indent=4)

print(f"Created {len(chunks)} chunks")
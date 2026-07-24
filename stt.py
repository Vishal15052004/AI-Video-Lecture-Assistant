import whisper 
import json

model= whisper.load_model("large-v2")

result = model.transcribe(audio="audio/2 _SEO and Core Web Vitals in HTML.mp3" ,
                         language = "hi",
                         task ="translate",
                         word_timestamps=False)

print(result["text"])
with open("whisper_output.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=4)



import nltk
nltk.download('vader_lexicon')
import streamlit as st
from pathlib import Path
from nltk.sentiment import SentimentIntensityAnalyzer
import glob

analyzer = SentimentIntensityAnalyzer()

positiv = []
negativ = []

diary_paths = glob.glob("diary/*txt")

for path in diary_paths:
    with open(path, "r") as file:
        note = file.read()
        file_name = Path(path).stem
        mood = analyzer.polarity_scores(note)
        if mood["neg"] < mood["pos"]:
            positiv.append({"name": file_name, "mood": mood["pos"], "text": note})
        else:
            negativ.append({"name": file_name, "mood": mood["neg"], "text": note})

print(len(positiv))
print(positiv)
print(len(negativ))
print(negativ)

st.title("Diary mood")
st.line_chart(positiv, x="mood", y="name", x_label="date", y_label="Positive")
st.line_chart(negativ, x="mood", y="name", x_label="date", y_label="Negative", color="#ec5353")
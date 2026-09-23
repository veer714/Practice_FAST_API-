from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import re
import string
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

tf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

app = FastAPI()

class UserInput(BaseModel):
    text: str

def transform_text(text: str) -> str:
    tokens = re.findall(r'\b\w+\b', text)
    tokens = [t for t in tokens if t.isalnum()]
    tokens = [t for t in tokens if t not in ENGLISH_STOP_WORDS and t not in string.punctuation]
    return " ".join(ps.stem(t) for t in tokens)

@app.post("/predict")
def predict(user_input: UserInput):
    transformed = transform_text(user_input.text)
    vector_input = tf.transform([transformed])
    result = int(model.predict(vector_input)[0])   # <-- convert numpy.int64 to int

    return {
        "prediction": result,
        "label": "Spam" if result == 1 else "Not Spam"
    }
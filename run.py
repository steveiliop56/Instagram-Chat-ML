import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk

# Load the saved model
model_path = 'model/model.pkl'
classifier = joblib.load(model_path)

# Load the vectorizer
vectorizer_path = 'model/vectorizer.pkl'
vectorizer = joblib.load(vectorizer_path)

# Download the required NLTK resources
nltk.download('punkt')

# Preprocess text
def preprocess_text(text):
    tokens = nltk.word_tokenize(text.lower())
    return ' '.join(tokens)

# Interactive prompt
while True:
    sentence = input("Enter a sentence (or 'quit' to exit): ")
    if sentence.lower() == 'quit':
        break

    preprocessed_sentence = preprocess_text(sentence)
    feature = vectorizer.transform([preprocessed_sentence])
    predicted_style = classifier.predict(feature)[0]
    print(f"The sentence is written in the style of: {predicted_style}")

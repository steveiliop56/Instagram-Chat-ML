import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
import os
import joblib

def read_sentences_from_file(filename):
    with open(filename, 'r') as file:
        sentences = file.readlines()
    return [sentence.strip() for sentence in sentences]

data_folder = 'data/'  # Specify the path to your data folder
people = []  # Initialize an empty list to store people's names
sentences = []
styles = []

# Iterate over the files in the data folder
for filename in os.listdir(data_folder):
    if filename.endswith('.txt'):
        person = os.path.splitext(filename)[0]  # Extract the person's name from the file name
        people.append(person)  # Add the person's name to the list

        file_path = os.path.join(data_folder, filename)
        person_sentences = read_sentences_from_file(file_path)
        sentences.extend(person_sentences)
        styles.extend([person] * len(person_sentences))

nltk.download('punkt')  # Download the required NLTK resources

def preprocess_text(text):
    tokens = nltk.word_tokenize(text.lower())
    return ' '.join(tokens)

preprocessed_sentences = [preprocess_text(sentence) for sentence in sentences]

vectorizer = TfidfVectorizer()
features = vectorizer.fit_transform(preprocessed_sentences)

X_train, X_test, y_train, y_test = train_test_split(features, styles, test_size=0.2, random_state=42)

classifier = LinearSVC()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
print(classification_report(y_test, y_pred))

# Save the trained model and vectorizer
model_path = 'model/model.pkl'
vectorizer_path = 'model/vectorizer.pkl'
joblib.dump(classifier, model_path)
joblib.dump(vectorizer, vectorizer_path)

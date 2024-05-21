import os
import math
from collections import Counter
from radon.complexity import cc_visit
from sklearn.feature_extraction.text import HashingVectorizer, TfidfTransformer, CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.base import BaseEstimator, TransformerMixin

# Paths to your data
js_path = "./Batch-File-examples"
obfuscated_js_path = "./Obf_data"

# Function to calculate entropy
def calculate_entropy(text):
    if not text:
        return 0
    counter = Counter(text)
    total_chars = len(text)
    entropy = -sum((count / total_chars) * math.log2(count / total_chars) for count in counter.values())
    return entropy

# Function to calculate cyclomatic complexity
def calculate_cyclomatic_complexity(code):
    try:
        blocks = cc_visit(code)
        return sum(block.complexity for block in blocks)
    except Exception:
        return 0

# Custom transformer to add entropy as a feature
class EntropyTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        return np.array([[calculate_entropy(text)] for text in X])

# Custom transformer to add cyclomatic complexity as a feature
class ComplexityTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        return np.array([[calculate_cyclomatic_complexity(text)] for text in X])

# Load the data
corpus = []
labels = []
file_types_and_labels = [(js_path, 0), (obfuscated_js_path, 1)]

# Reading files
for files_path, label in file_types_and_labels:
    files = os.listdir(files_path)
    for file in files:
        file_path = os.path.join(files_path, file)
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as myfile:
                data = myfile.read().replace("\n", "")
                data = str(data)
                corpus.append(data)
                labels.append(label)
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(corpus, labels, test_size=0.3, random_state=42)

# Build the pipeline for the model
text_clf = Pipeline([
    ('features', FeatureUnion([
        ('text', Pipeline([
            ('vect', HashingVectorizer(input='content', ngram_range=(1, 3), alternate_sign=False)),
            ('tfidf', TfidfTransformer(use_idf=True)),
        ])),
        ('entropy', EntropyTransformer()),
        ('complexity', ComplexityTransformer()),
    ])),
    ('clf', RandomForestClassifier(class_weight='balanced', n_estimators=100, random_state=42)),
])

# Train the model
text_clf.fit(X_train, y_train)

# Predict on the test set
y_test_pred = text_clf.predict(X_test)

# Print accuracy and confusion matrix
print("Accuracy:", accuracy_score(y_test, y_test_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_test_pred))

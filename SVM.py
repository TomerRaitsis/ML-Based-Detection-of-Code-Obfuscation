import os
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.pipeline import Pipeline

# Function to calculate entropy
def calculate_entropy(data):
    histogram = np.bincount(np.frombuffer(data, dtype=np.uint8), minlength=256)
    probabilities = histogram / len(data)
    entropy = -np.sum([p * np.log2(p) for p in probabilities if p != 0])
    return entropy

# Paths to the directories containing data
js_path = "./Batch-File-examples"
obfuscated_js_path = "./Obf_data" 

# Initialize lists to hold data and labels
corpus = []
labels = []
file_types_and_labels = [(js_path, 0), (obfuscated_js_path, 1)]

# Load data from directories and calculate entropy
for files_path, label in file_types_and_labels:
    files = os.listdir(files_path)
    for file in files:
        file_path = os.path.join(files_path, file)
        try:
            with open(file_path, "rb") as myfile:  # Open in binary mode
                data = myfile.read()
                entropy = calculate_entropy(data)
                corpus.append([entropy])  # Append entropy instead of raw data
                labels.append(label)
        except Exception as e:
            print(e)

print(list(zip(corpus,labels)))

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(corpus, labels, test_size=0.2, random_state=42)

# Create a pipeline with SVC
pipeline = Pipeline([
    ('classifier', SVC(kernel="linear"))  # SVC classifier
])

# Fit the pipeline to the training data
pipeline.fit(X_train, y_train)

# Predict labels for the test set
predictions = pipeline.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)

# Print confusion matrix
conf_matrix = confusion_matrix(y_test, predictions)
print("Confusion Matrix:")
print(conf_matrix)


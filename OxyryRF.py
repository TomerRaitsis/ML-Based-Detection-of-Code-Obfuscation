import os
import math
from collections import Counter
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt

# Paths to your data
train_paths_and_labels = [("./Datasets/Batch-File-examples", 0), ("./Datasets/Obf_data_Jlaive", 1)]
test_paths_and_labels = [("./Datasets/Non_Obfuscated", 0), ("./Datasets/Obf_data_Oxyry", 1)]

# Function to calculate entropy
def calculate_entropy(text):
    if not text:
        return 0
    counter = Counter(text)
    total_chars = len(text)
    entropy = -sum((count / total_chars) * math.log2(count / total_chars) for count in counter.values())
    return entropy

# Load the training data
train_corpus = []
train_labels = []
for files_path, label in train_paths_and_labels:
    files = os.listdir(files_path)
    for file in files:
        file_path = os.path.join(files_path, file)
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as myfile:
                data = myfile.read().replace("\n", "")
                data = str(data)
                train_corpus.append(data)
                train_labels.append(label)
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

# Load the test data
test_corpus = []
test_labels = []
for files_path, label in test_paths_and_labels:
    files = os.listdir(files_path)
    for file in files:
        file_path = os.path.join(files_path, file)
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as myfile:
                data = myfile.read().replace("\n", "")
                data = str(data)
                test_corpus.append(data)
                test_labels.append(label)
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

# Calculate entropy for training and test data points
train_entropy = [calculate_entropy(text) for text in train_corpus]
test_entropy = [calculate_entropy(text) for text in test_corpus]

# Print dataset statistics
print(f"Total training files: {len(train_corpus)}")
print(f"Total test files: {len(test_corpus)}")

# Create and train Random Forest model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit([[entropy] for entropy in train_entropy], train_labels)

# Predict on the test set
y_test_pred = clf.predict([[entropy] for entropy in test_entropy])

# Print accuracy and confusion matrix
accuracy = accuracy_score(test_labels, y_test_pred)
conf_matrix = confusion_matrix(test_labels, y_test_pred)

print(f"\nAccuracy: {accuracy}")
print(f"Confusion Matrix:\n{conf_matrix}")

# Plot entropy distribution
plt.figure(figsize=(12, 6))
plt.hist([train_entropy[i] for i in range(len(train_labels)) if train_labels[i] == 0], bins=50, alpha=0.5, label='Non-obfuscated (Train)', color='blue')
plt.hist([train_entropy[i] for i in range(len(train_labels)) if train_labels[i] == 1], bins=50, alpha=0.5, label='Obfuscated (Train)', color='red')
plt.hist([test_entropy[i] for i in range(len(test_labels)) if test_labels[i] == 0], bins=50, alpha=0.5, label='Non-obfuscated (Test)', color='green')
plt.hist([test_entropy[i] for i in range(len(test_labels)) if test_labels[i] == 1], bins=50, alpha=0.5, label='Obfuscated (Test)', color='orange')
plt.xlabel('Entropy')
plt.ylabel('Frequency')
plt.title('Entropy Distribution of Non-Obfuscated and Obfuscated Files')
plt.legend(loc='upper right')
plt.show()


import os
import math
from collections import Counter
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt

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

# Calculate entropy for all data points
X_train_entropy = [calculate_entropy(text) for text in X_train]
X_test_entropy = [calculate_entropy(text) for text in X_test]

# Create and train SVM model
clf = SVC(kernel='linear', random_state=42)

clf.fit([[entropy] for entropy in X_train_entropy], y_train)

# Predict on the test set
y_test_pred = clf.predict([[entropy] for entropy in X_test_entropy])

# Print accuracy
print("Accuracy:", accuracy_score(y_test, y_test_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_test_pred))

# Calculate entropy for all data points (train and test)
all_entropy = [calculate_entropy(text) for text in corpus]

# Determine colors for all data points based on true labels (blue for non-obfuscated, red for obfuscated)
all_colors = ['blue' if label == 0 else 'red' for label in labels]

# Count the number of obfuscated and non-obfuscated data points
num_non_obfuscated = labels.count(0)
num_obfuscated = labels.count(1)

# Plot the scatter plot for all data
plt.figure(figsize=(10, 6))
plt.scatter(all_entropy, labels, color=all_colors)

# Add labels and title
plt.xlabel('Entropy')
plt.ylabel('Label')
plt.title(f'Entropy vs. Label (Non-obfuscated: {num_non_obfuscated}, Obfuscated: {num_obfuscated})')
plt.show()


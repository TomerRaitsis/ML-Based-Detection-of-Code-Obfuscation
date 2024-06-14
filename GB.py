import os
import math
from collections import Counter
from sklearn.ensemble import GradientBoostingClassifier
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

total_files = 0
obfuscated_files = 0
non_obfuscated_files = 0

# Reading files
for files_path, label in file_types_and_labels:
    files = os.listdir(files_path)
    total_files += len(files)
    if label == 1:
        obfuscated_files += len(files)
    else:
        non_obfuscated_files += len(files)
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

# Print dataset statistics
print(f"Total files: {total_files}")
print(f"Non-obfuscated files: {non_obfuscated_files}")
print(f"Obfuscated files: {obfuscated_files}")

# Calculate entropy for all data points
all_entropy = [calculate_entropy(text) for text in corpus]

# Split the data into training and test sets
X_train_entropy, X_test_entropy, y_train, y_test = train_test_split(all_entropy, labels, test_size=0.3, random_state=42)

# Create and train Gradient Boosting model
clf = GradientBoostingClassifier(n_estimators=100, random_state=42)
clf.fit([[entropy] for entropy in X_train_entropy], y_train)

# Predict on the test set
y_test_pred = clf.predict([[entropy] for entropy in X_test_entropy])

# Print accuracy and confusion matrix
accuracy = accuracy_score(y_test, y_test_pred)
conf_matrix = confusion_matrix(y_test, y_test_pred)

print(f"\nAccuracy: {accuracy}")
print(f"Confusion Matrix:\n{conf_matrix}")

# Plot entropy distribution
plt.figure(figsize=(12, 6))
plt.hist([all_entropy[i] for i in range(len(labels)) if labels[i] == 0], bins=50, alpha=0.5, label='Non-obfuscated', color='blue')
plt.hist([all_entropy[i] for i in range(len(labels)) if labels[i] == 1], bins=50, alpha=0.5, label='Obfuscated', color='red')
plt.xlabel('Entropy')
plt.ylabel('Frequency')
plt.title('Entropy Distribution of Non-Obfuscated and Obfuscated Files')
plt.legend(loc='upper right')
plt.show()


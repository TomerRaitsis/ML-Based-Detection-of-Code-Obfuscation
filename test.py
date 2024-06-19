import os
import math
import numpy as np
from collections import Counter
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
import re

# Paths to your data
base_path = "./Datasets"  # Adjust this path to your data location
folders = ["Non_Obfuscated", "Obf_data_Jlaive", "Obf_data_Oxyry", "Obf_data_PyArmor", "Obf_data_Pyobfuscate", "Obf_data_FCTPyobfuscator"]

# Function to calculate entropy
def calculate_entropy(text):
    if not text:
        return 0
    counter = Counter(text)
    total_chars = len(text)
    entropy = -sum((count / total_chars) * math.log2(count / total_chars) for count in counter.values())
    return entropy

# Function to extract features
def extract_features(text):
    tokens = re.findall(r'\b\w+\b', text)
    token_lengths = [len(token) for token in tokens]
    
    if len(token_lengths) == 0:
        avg_token_length = 0
        median_token_length = 0
        std_token_length = 0
    else:
        avg_token_length = np.mean(token_lengths)
        median_token_length = np.median(token_lengths)
        std_token_length = np.std(token_lengths)
    
    unique_tokens = len(set(tokens))
    total_tokens = len(tokens)
    unique_token_ratio = unique_tokens / total_tokens if total_tokens > 0 else 0
    
    keywords = ['var', 'function', 'if', 'else', 'for', 'while', 'return', 'break', 'continue']
    keyword_count = sum(text.count(keyword) for keyword in keywords)
    
    string_literals = re.findall(r'\".*?\"|\'[^\']*\'', text)
    string_entropy = np.mean([calculate_entropy(s) for s in string_literals]) if string_literals else 0
    
    lines = text.splitlines()
    comment_lines = sum(1 for line in lines if line.strip().startswith('//') or line.strip().startswith('#'))
    total_lines = len(lines)
    comment_density = comment_lines / total_lines if total_lines > 0 else 0
    
    entropy = calculate_entropy(text)
    
    return [entropy, avg_token_length, median_token_length, std_token_length, unique_token_ratio, keyword_count, string_entropy, comment_density]

# Load the data
corpus = []
labels = []
features = []
folder_label_map = {"Non_Obfuscated": 0, "Obf_data_Jlaive": 1, "Obf_data_Oxyry": 1, "Obf_data_PyArmor": 1, "Obf_data_Pyobfuscate": 1, "Obf_data_FCTPyobfuscator": 1}

X_train_combined, X_test_combined, y_train_combined, y_test_combined = [], [], [], []

# Reading files and extracting features
for folder in folders:
    folder_path = os.path.join(base_path, folder)
    label = folder_label_map[folder]
    files = os.listdir(folder_path)
    
    # Temporary lists to store data from the current folder
    folder_features = []
    folder_labels_list = []
    
    for file in files:
        file_path = os.path.join(folder_path, file)
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as myfile:
                data = myfile.read()
                folder_features.append(extract_features(data))
                folder_labels_list.append(label)
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

    # Split the data for the current folder
    X_train, X_test, y_train, y_test = train_test_split(folder_features, folder_labels_list, test_size=0.3, random_state=42)
    
    # Append to the combined lists
    X_train_combined.extend(X_train)
    X_test_combined.extend(X_test)
    y_train_combined.extend(y_train)
    y_test_combined.extend(y_test)

print("X_train=", len(X_train_combined))
print("X_test=", len(X_test_combined))
print("y_train=", len(y_train_combined))
print("y_test=", len(y_test_combined))

# Convert lists to numpy arrays
X_train_combined = np.array(X_train_combined)
X_test_combined = np.array(X_test_combined)
y_train_combined = np.array(y_train_combined)
y_test_combined = np.array(y_test_combined)

# Create and train Random Forest model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train_combined, y_train_combined)

# Predict on the test set
y_test_pred = clf.predict(X_test_combined)

# Print accuracy, confusion matrix, and classification report
accuracy = accuracy_score(y_test_combined, y_test_pred)
conf_matrix = confusion_matrix(y_test_combined, y_test_pred)
report = classification_report(y_test_combined, y_test_pred)

print(f"\nAccuracy: {accuracy}")
print("\nConfusion Matrix:\n")
print(conf_matrix)
print("\nClassification Report:\n")
print(report)

# Plot confusion matrix
plt.figure(figsize=(10, 7))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['Non-Obfuscated', 'Obfuscated'], yticklabels=['Non-Obfuscated', 'Obfuscated'])
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()

# Plot feature importances
feature_names = ['Entropy', 'Avg Token Length', 'Median Token Length', 'Std Token Length', 'Unique Token Ratio', 'Keyword Count', 'String Entropy', 'Comment Density']
importances = clf.feature_importances_
indices = np.argsort(importances)[::-1]

plt.figure(figsize=(12, 8))
plt.title("Feature Importances")
plt.bar(range(len(importances)), importances[indices], align="center")
plt.xticks(range(len(importances)), [feature_names[i] for i in indices], rotation=45, ha='right')
plt.xlabel("Feature")
plt.ylabel("Importance")
plt.tight_layout()
plt.show()


import os
import math
import numpy as np
from collections import Counter
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import re
import seaborn as sns

# Paths to your data
base_path = "./Datasets"  # Adjust this path to your data location
folders = ["Non_Obfuscated", "Obf_data_Jlaive", "Obf_data_Oxyry", "Obf_data_PyArmor", "Obf_data_Pyobfuscate"]

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
folder_labels = {"Non_Obfuscated": 0, "Obf_data_Jlaive": 1, "Obf_data_Oxyry": 1, "Obf_data_PyArmor": 1, "Obf_data_Pyobfuscate": 1}

total_files = 0
obfuscated_files = 0
non_obfuscated_files = 0
folder_features = {folder: [] for folder in folders}

# Reading files and extracting features
for folder in folders:
    folder_path = os.path.join(base_path, folder)
    label = folder_labels[folder]
    files = os.listdir(folder_path)
    total_files += len(files)
    if label == 1:
        obfuscated_files += len(files)
    else:
        non_obfuscated_files += len(files)
    for file in files:
        file_path = os.path.join(folder_path, file)
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as myfile:
                data = myfile.read()
                corpus.append(data)
                labels.append(label)
                file_features = extract_features(data)
                features.append(file_features)
                folder_features[folder].append(file_features)
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

# Print dataset statistics
print(f"Total files: {total_files}")
print(f"Non-obfuscated files: {non_obfuscated_files}")
print(f"Obfuscated files: {obfuscated_files}")

# Convert folder features to numpy arrays for analysis
for folder in folders:
    folder_features[folder] = np.array(folder_features[folder])

# Analyze and plot feature distributions for each folder
feature_names = ['Entropy', 'Avg Token Length', 'Median Token Length', 'Std Token Length', 'Unique Token Ratio', 'Keyword Count', 'String Entropy', 'Comment Density']

for i, feature_name in enumerate(feature_names):
    plt.figure(figsize=(10, 6))
    for folder in folders:
        if folder_features[folder].shape[0] > 0:
            sns.kdeplot(folder_features[folder][:, i], label=folder, fill=True)
    plt.title(f'Distribution of {feature_name}')
    plt.xlabel(feature_name)
    plt.ylabel('Density')
    plt.legend()
    plt.show()

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=42)

# Create and train Random Forest model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Predict on the test set
y_test_pred = clf.predict(X_test)

# Print accuracy, confusion matrix, and classification report
accuracy = accuracy_score(y_test, y_test_pred)
conf_matrix = confusion_matrix(y_test, y_test_pred)
report = classification_report(y_test, y_test_pred)

print(f"\nAccuracy: {accuracy}")
print(f"Confusion Matrix:\n{conf_matrix}")
print(f"Classification Report:\n{report}")

# Plot feature importances
importances = clf.feature_importances_
indices = np.argsort(importances)[::-1]

plt.figure(figsize=(10, 8))
plt.title("Feature Importances")
plt.bar(range(len(importances)), importances[indices], align="center")
plt.xticks(range(len(importances)), [feature_names[i] for i in indices], rotation=45)
plt.xlabel("Feature")
plt.ylabel("Importance")
plt.show()


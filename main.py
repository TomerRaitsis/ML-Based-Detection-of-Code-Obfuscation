import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.svm import SVC
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from Utils import extract_features, load_and_split_data, load_and_split_data_v2, train_and_evaluate_model, plot_feature_importances

# Paths to your data
base_path = "./Datasets"  # Adjust this path to your data location
folders = ["Non_Obfuscated", "Obf_data_Jlaive", "Obf_data_Oxyry", "Obf_data_PyArmor", "Obf_data_Pyobfuscate", "Obf_data_FCTPyobfuscator"]

# Number of runs
num_runs = 10

# Initialize accumulators for results
svm_accuracies = []
gb_accuracies = []
rf_accuracies = []

# Feature names
feature_names = ['Entropy', 'Avg Token Length', 'Median Token Length', 'Std Token Length', 'Unique Token Ratio', 'Keyword Count', 'String Entropy', 'Comment Density']

for i in range(num_runs):
    print(f"\nRun {i+1}/{num_runs}")
    
    # Load and split the data
    X_train, X_test, y_train, y_test = load_and_split_data(base_path, folders, extract_features)

    # SVM Model
    print("\nTraining SVM Model")
    svm_clf = SVC(kernel='linear', random_state=i)
    svm_clf, svm_accuracy, svm_conf_matrix = train_and_evaluate_model(svm_clf, X_train, y_train, X_test, y_test)
    svm_accuracies.append(svm_accuracy)

    # Gradient Boosting Model
    print("\nTraining Gradient Boosting Model")
    gb_clf = GradientBoostingClassifier(n_estimators=100, random_state=i)
    gb_clf, gb_accuracy, gb_conf_matrix = train_and_evaluate_model(gb_clf, X_train, y_train, X_test, y_test)
    gb_accuracies.append(gb_accuracy)
    
    # Random Forest Model
    print("\nTraining Random Forest Model")
    rf_clf = RandomForestClassifier(n_estimators=100, random_state=i)
    rf_clf, rf_accuracy, rf_conf_matrix = train_and_evaluate_model(rf_clf, X_train, y_train, X_test, y_test)
    rf_accuracies.append(rf_accuracy)

# Compute mean accuracy
mean_svm_accuracy = np.mean(svm_accuracies)
mean_gb_accuracy = np.mean(gb_accuracies)
mean_rf_accuracy = np.mean(rf_accuracies)

print(f"\nMean SVM Accuracy: {mean_svm_accuracy}")
print(f"\nMean Gradient Boosting Accuracy: {mean_gb_accuracy}")
print(f"\nMean Random Forest Accuracy: {mean_rf_accuracy}")

# Plot feature importances for Gradient Boosting and Random Forest
plot_feature_importances(gb_clf, "Gradient Boosting", feature_names)

plot_feature_importances(rf_clf, "Random Forest", feature_names)


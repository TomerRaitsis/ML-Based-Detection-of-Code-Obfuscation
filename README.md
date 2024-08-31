# ML-Based Detection of Code Obfuscation

## Overview

This project focuses on the detection and classification of code obfuscation using machine learning models. Code obfuscation is a technique used to protect software by making its code difficult to understand, thereby preventing reverse engineering and unauthorized access. However, it can also be used for malicious purposes, hiding vulnerabilities, or malicious features in the software.

In this project, we explore various code obfuscation techniques, their ethical implications, and develop models to classify obfuscated versus non-obfuscated code. Our research leverages several machine learning models, including Random Forest, Gradient Boosting, and Support Vector Machines (SVM), to identify obfuscation techniques employed by tools such as Jlaive, Oxyry, PyObfuscate, Pyarmor, and Py-obfuscator.

## Project Structure

- **Data Collection and Preparation**: 
  - The data collection phase involved sourcing a diverse set of EXE and BAT files for obfuscation and non-obfuscated data.
  - Automation scripts were developed to streamline the obfuscation process using the Jlaive tool.
  - Ensured diversity in the dataset to cover various types of EXE files and addressed file integrity issues with rigorous validation checks.

- **Model Selection and Implementation**:
  - Selected Random Forest (RF), Gradient Boosting (GB), and Support Vector Machine (SVM) for their suitability in binary and multi-class classification tasks.
  - Initially achieved 100% accuracy on the training dataset, indicating overfitting, leading to further testing with new obfuscators.
  - Enhanced model training with additional features like string entropy, token length statistics, comment density, and unique token ratio, improving model robustness.

- **Feature Engineering**:
  - Key features included string entropy, average token length, standard deviation of token length, median token length, overall code entropy, comment density, unique token ratio, and keyword count.
  - These features were selected based on their potential to capture the nuances introduced by different obfuscation techniques.

- **Model Performance**:
  - The final dataset included obfuscated and non-obfuscated files from various sources, with the Gradient Boosting model achieving the highest accuracy of 97.30%.
  - A confusion matrix was generated to assess the performance of the Gradient Boosting model in classifying obfuscated and non-obfuscated files.

## Obfuscation Tools Overview

- **Jlaive**: An open-source tool that obfuscates .exe files into batch scripts using AES/XOR encryption for data protection.
- **Oxyry**: Provides basic obfuscation for Python code, focusing on renaming symbols and removing documentation strings.
- **PyObfuscate**: A Python-specific tool that employs a combination of lexical and control flow obfuscation techniques.
- **Pyarmor**: A popular tool that offers strong obfuscation for Python scripts, including encryption of code objects and protection against debugging and tampering.
- **Py-obfuscator**: A basic tool for Python code obfuscation, suitable for small projects and personal use.

## Ethical Considerations

While obfuscation is essential for protecting intellectual property and enhancing software security, it also raises significant ethical concerns:

- **Transparency and Accountability**: Obfuscation can obscure code transparency, making it difficult to hold developers accountable for software behavior.
- **Potential for Malicious Use**: Obfuscation can conceal harmful features or hidden data collection mechanisms, leading to potential misuse of user data.

## Conclusion

This project underscores the importance of balancing the need for code protection through obfuscation with ethical considerations such as transparency and accountability. Our models demonstrate the potential for accurate detection and classification of obfuscated code, providing valuable tools for improving software security.

## Future Work

Future research could explore AI-based obfuscation methods and leverage advancements in quantum computing to develop more robust security measures.

## References

- [Jlaive GitHub Repository](https://github.com/witchfindertr/Jlaive)
- [Oxyry Obfuscation Platform](https://pyob.oxyry.com/)
- [PyObfuscate Tool](https://pyobfuscate.com/pyd)
- [Pyarmor GitHub Repository](https://github.com/dashingsoft/pyarmor)
- [Py-Obfuscate FCT](https://freecodingtools.org/py-obfuscator)

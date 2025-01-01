#Step 1: Import Required Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report,ConfusionMatrixDisplay
#Step 2: Load and Prepare the Dataset
# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
#Step 3: Standardize the Data (Optional but Recommended)
# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
#Step 4: Train the KNN Model
# Create an instance of the KNN classifier with k=5
knn_model = KNeighborsClassifier(n_neighbors=5)
# Train the model
knn_model.fit(X_train, y_train)
#Step 5: Make Predictions
# Make predictions on the test set
y_pred = knn_model.predict(X_test)
#Step 6: Evaluate the Model
# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')
# Generate a confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print('Confusion Matrix:\n', conf_matrix)
# Display a classification report
class_report = classification_report(y_test, y_pred)
print('Classification Report:\n', class_report)
# Plot the confusion matrix
ConfusionMatrixDisplay(knn_model, X_test)
ConfusionMatrixDisplay.from_estimator(knn_model, X_test, display_labels=iris.target_names, cmap=plt.cm.Blues)
plt.show()
#Step 7: Choosing the Optimal k Value (Optional)
# Evaluate the model with different k values
k_values = range(1, 26)
accuracies = []
for k in k_values:
 knn_model = KNeighborsClassifier(n_neighbors=k)
 knn_model.fit(X_train, y_train)
 y_pred = knn_model.predict(X_test)
 accuracies.append(accuracy_score(y_test, y_pred))
# Plot the accuracy vs. k values
plt.plot(k_values, accuracies)
plt.xlabel('k')
plt.ylabel('Accuracy')
plt.title('Accuracy vs. k Value')
plt.show()

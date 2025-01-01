# 1. Import Libraries
import pandas as pd
from sklearn.datasets import load_iris # type: ignore
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt

# 2. Load Dataset
iris = load_iris()
X = iris.data # Features
y = iris.target # Labels

# 3. Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
# 4. Train Decision Tree Model
clf = DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)
# 5. Visualize the Decision Tree
plt.figure(figsize=(15, 10))
tree.plot_tree(clf, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
plt.show()

# 6. Evaluate the Model
accuracy = clf.score(X_test, y_test)
print(f"Accuracy: {accuracy:.2f}")
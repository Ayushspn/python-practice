# Import necessary libraries
from sklearn.datasets import load_iris              # Load the Iris dataset
from sklearn.model_selection import train_test_split # Split dataset into train and test sets
from sklearn.tree import DecisionTreeClassifier      # Decision Tree model
from sklearn.metrics import accuracy_score, classification_report # Evaluation metrics
from sklearn import tree                             # For tree visualization
import matplotlib.pyplot as plt

# Load dataset
X, y = load_iris(return_X_y=True)  # X = features (sepal length, sepal width, petal length, petal width), y = labels (species)

# Split dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



# Initialize Decision Tree classifier with max depth of 3 to prevent overfitting
clf = DecisionTreeClassifier(max_depth=3, random_state=42)

# Train the model on training data
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Evaluate model performance using accuracy and classification report
print("Accuracy:", accuracy_score(y_test, y_pred))  # Prints overall accuracy
print("Report:\n", classification_report(y_test, y_pred))  # Prints precision, recall, F1-score per class

# Visualize the Decision Tree
plt.figure(figsize=(12, 8))
tree.plot_tree(
    clf,
    filled=True, 
    feature_names=load_iris().feature_names, 
    class_names=load_iris().target_names,
    rounded=True,
    fontsize=10
)
plt.title("Decision Tree Visualization")
plt.show()

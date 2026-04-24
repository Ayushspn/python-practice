# Import libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
X, y = load_iris(return_X_y=True)

# Split data (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize Random Forest with 100 trees
rf = RandomForestClassifier(n_estimators=100, max_depth=3, random_state=42)

# Train the model
rf.fit(X_train, y_train)

# Predict on test data
y_pred = rf.predict(X_test)

# Evaluate performance
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Feature importance
import pandas as pd
feature_importance = pd.Series(rf.feature_importances_, index=load_iris().feature_names)
print("\nFeature Importance:\n", feature_importance.sort_values(ascending=False))

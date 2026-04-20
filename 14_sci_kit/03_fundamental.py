from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

# Load dataset
housing = fetch_california_housing(as_frame=True)
X = housing.data[["MedInc", "HouseAge", "AveRooms"]]
y = housing.target

# Initialize model
model = LinearRegression()

# Perform 5-fold cross-validation
scores = cross_val_score(model, X, y, cv=5, scoring='r2')

print("Cross-validation scores:", scores)
print("Average R² score:", scores.mean())

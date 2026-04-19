from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
housing = fetch_california_housing(as_frame=True)
df = housing.frame

# print(df)

# Features and target
X = df[["MedInc", "HouseAge", "AveRooms"]]
y = df["MedHouseVal"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(X_train)
# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate
print("Score:", model.score(X_test, y_test))

from sklearn.linear_model import LinearRegression

# Train Model using Linear Regression
model = LinearRegression()  # Create an instance of Linear Regression
model.fit(X_train, y_train)  # Fit the model with training data

# Make Predictions
y_pred = model.predict(X_test)  # Predict the diseases for the test data

# Model Evaluation
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score

mse = mean_squared_error(y_test, y_pred)  # Mean Squared Error
r2 = r2_score(y_test, y_pred)  # R-squared value
print("Mean Squared Error:", mse)
print("R-squared:", r2)

# Accuracy Calculation (convert predicted values to disease classification)
threshold = 0.5  # This threshold can be adjusted based on the problem
y_pred_class = [1 if pred > threshold else 0 for pred in y_pred]
accuracy = accuracy_score(y_test, y_pred_class)

print("Accuracy:", accuracy)

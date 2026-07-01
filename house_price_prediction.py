import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

#Load dataset
df = pd.read_csv("train.csv")

print("Dataset Shape:", df.shape)

#Checking the missing values
features = ['GrLivArea', 'BedroomAbvGr', 'FullBath', 'SalePrice']
print("\nMissing Values:")
print(df[features].isnull().sum())

#Correlation Matrix
print("\nCorrelation Matrix:")
print(df[features].corr())

#Visualizations
plt.figure(figsize=(6,4))
sns.heatmap(df[features].corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()

plt.figure(figsize=(8,5))
sns.scatterplot(x='GrLivArea', y='SalePrice', data=df)
plt.title("Living Area vs Sale Price")
plt.show()

plt.figure(figsize=(8,5))
sns.scatterplot(x='BedroomAbvGr', y='SalePrice', data=df)
plt.title("Bedrooms vs Sale Price")
plt.show()

plt.figure(figsize=(8,5))
sns.scatterplot(x='FullBath', y='SalePrice', data=df)
plt.title("Bathrooms vs Sale Price")
plt.show()

#Feature Selection
X = df[['GrLivArea', 'BedroomAbvGr', 'FullBath']]
y = df['SalePrice']

#Train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

#Train Model
model = LinearRegression()
model.fit(X_train, y_train)

#Prediction
y_pred = model.predict(X_test)

#evaluation
print("\nModel Performance")

print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

#Actual VS Predicted Graph
plt.figure(figsize=(8,5))
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted House Prices")
plt.show()

#Saving Model
joblib.dump(model, "house_price_model.pkl")

print("\nModel Saved Successfully!")

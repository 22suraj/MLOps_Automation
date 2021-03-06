import pandas as pd
dataset = pd.read_csv('/home/SalaryData.csv')
y = dataset['Salary']
x = dataset['YearsExperience']
X = x.values.reshape(30,1)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
accuracy = model.score(X_test,y_test)
print(accuracy*100)


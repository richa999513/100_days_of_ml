import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

np.random.seed(42)

X = np.random.rand(50,1)*100
y = 3.5*X + np.random.rand(50,1)*20

model = LinearRegression()
model.fit(X,y)

y_pred = model.predict(X)

plt.figure(figsize=(8,6)) 
plt.scatter(X, y, color='blue', label='Data Points') 
plt.plot(X, y_pred, color='red', linewidth=2, label='Regression Line') 
plt.title('Linear Regression on Random Dataset')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()

print("Slope (Coefficient):", model.coef_[0][0])
print("Intercept:", model.intercept_[0])
import sys
import LinearRegression
from matplotlib import pyplot as plt

n = int(input("Enter number of values: "))

X = input("\nEnter the x values : ").strip().split()
y = input("Enter the y values : ").strip().split()

if len(X) != n or len(y) != n:
    print("Invalid data.")
    sys.exit(0)

for i in range(n):
    X[i] = int(X[i])
    y[i] = int(y[i])

m, b = LinearRegression.gradient_descent(X, y, 0.01, 1000)

print("\n")
print(m, b)

new_data = [m * x_val + b for x_val in X]

plt.plot(X, y, 'o')
plt.plot(X, new_data)

plt.show()

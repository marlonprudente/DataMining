import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=3)

df = pd.read_csv("iris.csv")

X = df.iloc[:,0:4].values

y = df[['variety']].values.ravel()

knn.fit(X,y)


print(knn.predict([[6.5, 5.5, 4.5, 1.3]]))

print(knn.predict([[1.5, 2.5, 2.0, 0.3]]))
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing


knn = KNeighborsClassifier(n_neighbors=3)

#Le o arquivo CSV e limita em um numero de 10k de linhas
df = pd.read_csv("../Data/public/test_dataset.csv", nrows=10000)

#Transforma todas as strings no dataset em um valor unico

for column in df.columns:
      le = preprocessing.LabelEncoder()
      df[column] = le.fit_transform(df[column])

#Informa os valores de entrada (No caso coluna 0 a 6)
X = df.iloc[:,0:6].values

#Informa a saida (No caso a coluna silhouette)
y = df[['silhouette']].values.ravel()

#Executa o treinamento
knn.fit(X,y)




##silhouette
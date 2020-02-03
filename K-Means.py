# -*- coding: utf-8 -*-
"""

@authors: Jibin Jiju Abraham, Jithin V. Nair, Sanjeev Nishad, Viknesh
"""

import pandas as pd
import numpy as np

PCA1=pd.read_csv(r'D:\\Data Science\\New Datas\\Data Science\\PCA1.csv',encoding='latin1')

PCA1.head()

PCA1=PCA1.dropna()

PCA1.head(1000)

PCA1.to_csv(r'D:\\Data Science\\New Datas\\Data Science\\PCA_Final.csv')


from sklearn import preprocessing

y=PCA1[['ORB%', 'DRB%', 'TRB%', 'AST%', 'STL%', 'BLK%', 'TOV%',
       'FG%', '3P%', '2P%', 'eFG%', 'FT%', 'Height', 'Weight']]

dataset1_standardized=preprocessing.scale(y)

dataset1_standardized=pd.DataFrame(dataset1_standardized)

from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters = 8, init = 'k-means++', random_state = 42)

y_kmeans = kmeans.fit_predict(dataset1_standardized)
print(y_kmeans)

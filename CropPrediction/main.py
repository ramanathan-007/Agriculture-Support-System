import numpy as np
import matplotlib.pyplot as plt
import pickle
import pandas as pd

dataset = pd.read_csv('Crop_recommendation.csv')
m = dataset.isnull().sum()
# print(m)

# dataset['label'].fillna(dataset['label'].mean(), inplace=True)

y = dataset['label']
x = dataset.drop(['label'], axis=1)

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test  = train_test_split(x ,y , test_size=0.2, random_state=0)

from sklearn.neighbors import KNeighborsClassifier

kn_classifier = KNeighborsClassifier()

kn_classifier.fit(x_train.values,y_train.values)




pickle.dump(kn_classifier,open('main.pkl','wb'))

main = pickle.load(open('main.pkl','rb'))

print(kn_classifier.predict((np.array([[90,40,40,20,80,7,200]]))))

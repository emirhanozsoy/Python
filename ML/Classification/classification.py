# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:40:44 2018

@author: emirhan
"""

import numpy as np
from sklearn import preprocessing,neighbors,model_selection
import pandas as pd 
    
accuracies=[]

for i in range(100):
    df=pd.read_csv('breast-cancer-wisconsin.data')
    df.replace('?', -99999, inplace=True)
    df.drop(['id'], 1, inplace=True)
    
    X = np.array(df.drop(['class'], 1))
    y = np.array(df['class'])
     
    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)
    
    clf = neighbors.KNeighborsClassifier(n_jobs=-1)
    clf.fit(X_train,y_train)
    
    accuracy=clf.score(X_test,y_test)
#    
#    print(accuracy)
#    
#    example_measures=np.array([[4,2,1,1,1,2,3,2,1],[4,2,3,1,1,2,2,2,1],[10,2,3,6,4,7,3,1,1]])
#    example_measures=example_measures.reshape(len(example_measures),-1)
#    
#    prediction = clf.predict(example_measures)
#    print(prediction)
    accuracies.append(correct/total)

print('Scikit accu:', sum(accuracies)/len(accuracies))
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_breast_cancer
cancer=load_breast_cancer()
print(cancer)
x=cancer.data[:,:2]
y=cancer.target
y_name=cancer.target_names

xd=pd.DataFrame(x)
yd=pd.DataFrame(y_name)

print(y)

print(xd)
print(x)


sns.heatmap(yd.isnull())

from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.svm import SVC

svm_model=SVC(kernel="rbf",gamma=.5,C=1)
svm_model.fit(x,y)

import matplotlib.colors
mycol=matplotlib.colors.ListedColormap(["red","green"])
DecisionBoundaryDisplay.from_estimator(
    svm_model,
    x,
    response_method="predict",
    xlabel=cancer.feature_names[0],
    ylabel=cancer.feature_names[1],
    cmap=mycol

)
radius=x[:,0]
txt=x[:,1]
plt.scatter(radius,txt,c=y,s=20)
plt.scatter(10,15,s=60)

inp=[[10,15]]
yp=svm_model.predict(inp)
print(y_name[yp[0]])
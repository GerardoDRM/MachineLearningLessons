#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

from outlier_cleaner import outlierCleaner
from sklearn.linear_model import LinearRegression

'''
  We found that there are more outliers on enron data,
  this outliers own to people that can be suspicius on the case
  so this is an example where outliers can show us some info that
  represents points that we need to pay attention
 '''

### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
# Remove outlier TOTAL key
data_dict.pop("TOTAL",0)
data = featureFormat(data_dict, features)

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

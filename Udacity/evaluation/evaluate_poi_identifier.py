#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.cross_validation import train_test_split
from sklearn.datasets import fetch_lfw_people
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.30, random_state=42)

### it's all yours from here forward!
clf = DecisionTreeClassifier()
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
# Get accuracy
ac = accuracy_score(pred, labels_test)
print(ac)


### your code goes here
# POIs number on test set
print("Number of POIs predicted:", int(sum(pred)))
# NUmber of people in test set
print "Total number of people in test set:", len(pred)
# accuracy with all 0.
ac = accuracy_score([0.] * len(pred), labels_test)
print(ac)

true_positives = 0
false_positives = 0
false_negatives = 0

for pred, actual in zip(pred, labels_test):
	if pred == actual and actual == 1:
		true_positives += 1
	elif pred == 1 and actual == 0:
		false_positives += 1
	elif pred == 0 and actual == 1:
		false_negatives += 1

print "True Positives:", true_positives
print "False Positives", false_positives
print "False Negatives", false_negatives


print "\nPrecision (POIs):", float(true_positives)/(true_positives + false_positives)
print "Recall (POIs)", true_positives/(true_positives + false_negatives)

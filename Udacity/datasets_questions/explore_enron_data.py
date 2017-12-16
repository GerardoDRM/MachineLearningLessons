#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
# Data points
print(len(enron_data))
# Features available
person_features = enron_data[enron_data.keys()[0]]
print(len(person_features))
# Finding POIs
pois = filter(lambda x:x["poi"] == 1, enron_data.values())
print(len(pois))
# James Prentice Stock
pretince = {k:v for k,v in enron_data.items() if k == "PRENTICE JAMES"}
print(pretince)
# Wesley Colwell
colwell = {k:v for k,v in enron_data.items() if "COLWELL" in k}
print(colwell)
# Folks with email and salary info
email_address = len([i for i in enron_data.values() if i["email_address"] != 'NaN'])
salary = len([i for i in enron_data.values() if i["salary"] != 'NaN'])
print(salary, email_address)
# People with not total payments
total_payments = len([i for i in enron_data.values() if i["total_payments"] == 'NaN'])
print(total_payments)

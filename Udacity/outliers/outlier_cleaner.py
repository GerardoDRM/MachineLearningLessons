#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    # Get dict of predictions and store position
    pre_data = {i:predictions[i][0] - net_worths[i][0] for i in range(len(predictions))}
    # Remove 10% of outliers
    percentage = int(len(predictions) - (len(predictions) * .10))
    # Sort by value (error)
    pred = sorted(pre_data.items(), key=lambda x:x[1])[:percentage]
    # Add clean data
    cleaned_data = [(ages[p[0]], net_worths[p[0]], p[1]) for p in pred]
    return cleaned_data

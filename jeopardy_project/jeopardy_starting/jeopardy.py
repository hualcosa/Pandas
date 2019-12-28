# This was a project i've made during pandas course in Codecademy

import pandas as pd
pd.set_option('display.max_colwidth', -1)

# Loading the data
dataset = pd.read_csv("jeopardy.csv")
#print(dataset.columns)

# Renaming misformatted data
dataset = dataset.rename(columns = {
' index': 'index', ' Show Number': 'Show Number', ' Air Date': 'Air Date', ' Round': 'Round', ' Category': 'Category', ' Value':'Value', ' Question': 'Question', ' Answer': 'Answer' 
})
#print(dataset[" Question"])

# Filtering the dataset by a list of rows
def filter_data(data, words):
    filter = lambda x: all(word.lower() in x.lower() for word in words)
    # Applies the lambda function to the question Column
    return data.loc[data["Question"].apply(filter)]

# testing the filter function
filtered = filter_data(dataset, ["King", "England"])
#print(filtered['Question'])

# Adding a new column. If the value of the float column is not "None", then we cut off the first character (which is a dollar sign), and replace all commas with nothing, and then cast that value to a float. If the answer was "None", then we just enter a 0.
jeopardy_data["Float Value"] = jeopardy_data["Value"].apply(lambda x: float(x[1:].replace(',','')) if x != "None" else 0)

# Filtering the dataset and finding the average value of those questions
filtered = filter_data(jeopardy_data, ["King"])
print(filtered["Float Value"].mean())

# A function to find the unique answers of a set of data
def get_answer_counts(data):
    return data["Answer"].value_counts()

# Testing the answer count function
print(get_answer_counts(filtered))

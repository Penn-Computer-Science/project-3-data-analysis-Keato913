import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random

data = pd.read_csv('.github\Survey data.py')
surveyData = pd.DataFrame(data)
print("-_"*20)
print("Head of the DataFrame")
print(surveyData.head())

print("-_"*20)
print("Tail of the DataFrame")
print(surveyData.tail())

print("-_"*20)
print("Summary of DataFrame")
print(surveyData.info())

print("-_"*20)
print("Stats")
print(round(surveyData.describe()))

print("-_"*20)
print("First student data")
print(surveyData.iloc[0])
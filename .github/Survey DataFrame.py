import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random

data = pd.read_csv('.github\data.csv')
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
print("First person's data")
print(surveyData.iloc[0])

print("-_"*20)
print("Average GPA per morning person")
print(surveyData.groupby('Morning person?')['GPA'].mean())

surveyData.groupby('Before bed')['Hours of sleep'].mean()

surveyData.groupby('Before bed')['Hours of sleep'].mean().plot(kind="bar")
plt.title("Average sleep by what you do before bed")
plt.xlabel("sleep(Hours)")
plt.ylabel("before bed")
plt.show()

surveyData.groupby('Before bed')['Hours of sleep'].mean().plot(kind="line")
plt.title("Average sleep by what you do before bed")
plt.xlabel("sleep(Hours)")
plt.ylabel("before bed")
plt.show()

surveyData.groupby('Before bed')['Hours of sleep'].mean().plot(kind="box")
plt.title("Average sleep by what you do before bed")
plt.xlabel("sleep(Hours)")
plt.ylabel("before bed")
plt.show()

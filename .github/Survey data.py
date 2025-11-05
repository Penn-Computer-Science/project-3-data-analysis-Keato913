import pandas as pd
import random
import matplotlib.pyplot as plt


bebed = ["Doomscroll", "Watch TV", "Read", "Nothing"]
showers = ["Morning", "Night", "Never"]
mPerson = ["Yes", "No"]
sleep  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
GPA = ["Zero-One", "One-Two", "Two-Three", "Three-Four", "Four-Five" ,"Five-Six", "Six-Seven", "Seven-Eight", "Eight-Nine", "Nine-Ten"]
Amount = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

data = {
    "Before bed": [random.choice(bebed) for _ in Amount],
    "showers": [random.choice(showers) for _ in Amount],
    "Morning person?": [random.choice(mPerson) for _ in Amount],
    "Hours of sleep": [random.choice(sleep) for _ in Amount],
    "GPA": [round(random.uniform(0.0, 4.0),2) for _ in Amount]
}

surveyData = pd.DataFrame(data)
surveyData.to_csv('data.csv',index=False)



# importing the modules to be used in the code
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

 #importing your data or csv file


data = pd.read_csv("tips.csv")


# to see the data in our sample_data
data
print (data)

#to add a new calculated column.

data["tipsize"] = data["tip"] * data["size"]
print (data)

#data subsets based on a condition
timedinner = data[data.time == 'Dinner']
daydinner = data[data.day =="Sat"]
print (timedinner)
print (daydinner)



plt.bar(timedinner.day, timedinner.tip)
plt.title("Time Day Tip")
plt.xlabel("Day")
plt.ylabel("Tip")
plt.show()


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import the villager file
data = pd.read_csv("villagers.csv")
#print(data)

#look at the contents of the data 
#print(data.info) 
#no null values

#Find the number of distinct species
species = data['Species'].value_counts()

#create a bar chart of the most frequent species
species.plot(kind='bar',color= 'purple')
plt.xlabel('Species')
plt.ylabel('Count')
plt.title('Frequency of Villagers by Species')
plt.yticks(range(0, int(species.max()) + 1, 1)) 
plt.grid(alpha=0.3)  
plt.tight_layout()
plt.show()
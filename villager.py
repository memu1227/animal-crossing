import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import squarify

#scrape the villagers list from nookipedia website
#according to html code inspect: <table class="styled color-villager sortable...>
#url to scrape: https://nookipedia.com/wiki/Villager/New_Horizons
url = 'https://nookipedia.com/wiki/Villager/New_Horizons'

#find index of the villagers list table
tables = pd.read_html(url)
#check how many tables on this page
#print(len(tables)) #theres only one table 
#grab that table
villagers_df = pd.read_html(url)[0]

#inspect table
#print(villagers_df.shape)
#print(villagers_df.head())

#drop poster column bc its irrelevant here
villagers_df = villagers_df.drop(columns=['Poster'])

#check to see if its dropped
#print(villagers_df.head()) #its dropped

#save to csv for future use maybe
villagers_df.to_csv('villagers.csv', index=False)
#print(data)

#look at the contents of the data 
#print(villagers_df.info) 
#no null values

#Find the number of distinct species
species = villagers_df['Species'].value_counts()
print(species.sum()) #417
print(species.min()) #4
print(species.max()) #23
print(len(species)) #35

#squarify.plot(sizes=species.values, label=species.index, alpha=0.8)
#plt.axis('off')
#plt.show()

#create a  horizontal bar chart of the most frequent species
species.plot(kind='barh', color='purple', figsize=(8, 12))
plt.ylabel('Species')
plt.xlabel('Count')
plt.title('Frequency of Villagers by Species')
plt.grid(axis='x', alpha=0.3)

# Add labels at the end of each bar
ax = plt.gca()
for i, (species_name, count) in enumerate(species.items()):
    ax.text(count + 0.3, i, str(int(count)), va='center', fontsize=9)

plt.tight_layout()
#plt.show()

#sort dataset to analyze species
pd.set_option('display.max_rows', None) 
species_table = villagers_df.sort_values('Species')
#print(species_table)

#distribution of personalities after removing A and B
villagers_df['Personality_Combined'] = villagers_df['Personality'].str.replace(' \(A\)| \(B\)', '', regex=True)

#Create cross-tabulation of Personality vs Gender
personality_gender = pd.crosstab(villagers_df['Personality_Combined'], villagers_df['Gender'])

plot = personality_gender.plot(
    kind='bar', 
    stacked=True, 
    figsize=(12, 6),
    color=['pink', 'lightblue']
)

plt.ylabel('Count')
plt.xlabel('Personality')
plt.title('Villagers by Personality and Gender')
plt.legend(title='Gender')
plt.grid(axis='y', alpha=0.3)
plt.xticks(rotation=45, ha='right')

# Add total count labels at top of bars
totals = personality_gender.sum(axis=1)
for i, total in enumerate(totals):
    plot.text(i, total + 0.5, str(int(total)), ha='center', fontsize=9)

plt.tight_layout()
#plt.show()

# species and gender
species_gender = pd.crosstab(villagers_df['Species'], villagers_df['Gender'])

plot2 = species_gender.plot(
    kind='barh', 
    stacked=True, 
    figsize=(12, 10),  
    color=['pink', 'lightblue']
)

plt.xlabel('Count')  
plt.ylabel('Species')  
plt.title('Villagers by Species and Gender')
plt.legend(title='Gender')
plt.grid(axis='x', alpha=0.3)

# Add total count labels at end of bars (x position, not y)
totals2 = species_gender.sum(axis=1)
for i, total in enumerate(totals2):
    plot2.text(total + 0.5, i, str(int(total)), va='center', fontsize=9)  

plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import numpy as np
import csv

ranking_graph=pd.read_csv("seasonalAnimeInfo.csv")

#removing whitespaces
ranking_graph = ranking_graph.rename(columns={' Studio': 'Studio'})
ranking_graph = ranking_graph.rename(columns={' Ratings': 'Ratings'})

ranking_graph= ranking_graph.sort_values('Ratings', ascending=True)
#print(ranking_graph.head())
#print(ranking_graph.describe())

x=ranking_graph['Title']

y=ranking_graph.Ratings
plt.xlabel('Ratings/10')

plt.barh(x,y, height=0.5)

#The y-values v are both the x-location and the string values for ax.text, and conveniently the barplot has a metric of 1 for each bar, so the enumeration i is the y-location.
for i, v in enumerate(y):
    plt.text(v, i, " "+str(v), color='blue', va='center')


#y_pos = [i for i, _ in enumerate(x)]
#plt.barh(x_pos, y, color='red', alpha=0.2)
#plt.xticks(range(len(x)))


plt.subplots_adjust(left=0.48,bottom=0.07,right=0.99,top=0.95)
plt.savefig('AnimeData.png', bbox_inches='tight')
plt.show()


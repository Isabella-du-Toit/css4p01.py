# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 09:21:40 2024

@author: Isabella
"""
import pandas as pd
file = pd.read_csv("movie_dataset.csv", index_col=0)

#q10_most common actor, note multiple each movie
#Split the file contents into words using the split() function. Create a dictionary for counting the number of occurrences of each word. Create a counter variable to count a number of unique words. Traverse the dictionary and increment the counter for every unique word.
print(file["Actors"])
actors = (file["Actors"])
print(actors)

actors_str = ",".join(str(element) for element in actors)
actors_split = actors_str.split(",")

from collections import defaultdict
temp = defaultdict(int)
# memoizing count
for sub in actors_split:
    for wrd in sub.split(","):
        temp[wrd] += 1
 
# getting max frequency
res = max(temp, key=temp.get)
 
# printing result
print("Word with maximum frequency : " + str(res))#Christian Bale
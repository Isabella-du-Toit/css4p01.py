# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 11:14:51 2024

@author: Isabella
"""
#importing data
import pandas as pd

file = pd.read_csv("movie_dataset.csv", index_col=0)
print(file)

#remove nans or replace with average
revenue_avg = file["Revenue (Millions)"].mean()
file["Revenue (Millions)"].fillna(revenue_avg, inplace = True)
print(file)

metascore_avg = file["Metascore"].mean()
file["Metascore"].fillna(metascore_avg, inplace = True)
print(file)

print(file.info())#datatypes
print(file.describe())

#check visually for outliers and replace
#q1_highest rated movie
print(file["Rating"].min())#1.9
print(file["Rating"].max())#9.0

print(file[file["Rating"] <2])#Disaster Movie
print(file[file["Rating"] >8.9])#q1_The Dark Knight

#q2_average revenue for all movies
print(revenue_avg)#q2_82.96

#q3_average revenue for movies 2015 to 2017
subset_rev2015 = (file[file["Year"] > 2014])
subset_rev = (subset_rev2015[subset_rev2015["Year"] < 2018])
rev_subset_avg = subset_rev["Revenue (Millions)"].mean()
print(rev_subset_avg)#68.06

#q4_movies released 2016
print(file[file["Year"] == 2016])#297

#q5_director Christopher Nolan
print(file[file["Director"] == "Christopher Nolan"])#5

#q6_ratings of at least 8
print(file[file["Rating"]>=8])#78

#q7_median rating for Christopher Nolan directed movies
CN_subset = (file[file["Director"] == "Christopher Nolan"])
print(CN_subset)
print(CN_subset["Rating"].median())#8.6

#q8_year with highest rating = 2007
subset_2016 = (file[file["Year"] == 2016])
print(subset_2016["Rating"].mean()) #6.4367

subset_2008 =(file[file["Year"] == 2008])
print(subset_2008["Rating"].mean()) #6.7846

subset_2007 =(file[file["Year"] == 2007])
print(subset_2007["Rating"].mean()) #7.1339

subset_2006 =(file[file["Year"] == 2006])
print(subset_2006["Rating"].mean()) #7.1250

#import matplotlib.pyplot as plt
#plot = plt.bar(file["Year"], file ["Rating"])

#requires answer
#q9_percentage increase in movies made between 2006 and 2016
in_2006 = (file[file["Year"] == 2006])
print(in_2006) #44 movies
print(file) #1000 movies

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

#q11_number of unique genres, note multiple each movie
print(file["Genre"])
genre = (file["Genre"])
print(genre)
genre_ls = genre.tolist()
genre_str = ",".join(str(element) for element in genre_ls)
genre_split = genre_split = genre_str.split(",")
unique_set = set(genre_split)
unique_count = len(unique_set)
print(unique_count)#20

#q12_correlation of numerical features
#corr_matrix = file.corr()['Rating']

#q13_github respiratory



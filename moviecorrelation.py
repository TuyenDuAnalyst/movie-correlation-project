# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SNHX_ROlWggW4szyxEVF4-3hs1wrz3M4
"""

# Commented out IPython magic to ensure Python compatibility.
#Import libraries

import pandas as pd
import seaborn as sns
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
plt.style.use ('ggplot')
from matplotlib.pyplot import figure

# %matplotlib inline 
matplotlib.rcParams['figure.figsize'] = (12,8) # Adjust the configuration of the plots we will create

#Read in the data

df = pd.read_csv('/content/movies.csv')

# Let's look at the data

df.head()

#Let's see if there is any missing data
for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    print('{} - {}%'.format(col, round(pct_missing*100)))

# dropping the rows having NaN values
df =df.dropna()

# Data types for our columns
df.dtypes

# change data type of columns

df['budget'] = df['budget'].astype('int64')
df['gross'] = df['gross'].astype('int64')

df

#Create correct Year column
df["yearcorrect"] = df['released'].astype(str).str.split(" ", expand=True)[2]
df

df =df.sort_values(by=['gross'], inplace=False, ascending=False)

pd.set_options('display.max_rows', None)

# Drop any duplicated

df.drop_duplicates()

df

# Budget high correlation
# company high correlation

#Scatter plot with budget vs gross

plt.scatter(x=df['budget'], y=df['gross'])
plt.title('Budget vs Gross Earnings')
plt.xlabel('Gross Earning')
plt.ylabel('Budget for Film')
plt.show()

df.head()

# Plot budget vs gross using seaborn

sns.regplot (x='budget', y='gross', data=df, scatter_kws={"color": "red"}, line_kws={"color": "blue"})

#Let's start looking at correlation

df.corr(method='pearson') #pearson, kendall, spearman

#High correlation between budget and gross
# I was right

correlation_matrix = df.corr(method='pearson')
sns.heatmap(correlation_matrix, annot =True)
plt.title('Correlation Matric for Numeric Features')
plt.xlabel('Movie Features')
plt.ylabel('Movie Features')
plt.show()

#Look at company

df.head()

df_numerized = df

for col_name in df_numerized.columns:
  if (df_numerized[col_name].dtype == 'object'):
        df_numerized[col_name] = df_numerized[col_name].astype('category')
        df_numerized[col_name] = df_numerized[col_name].cat.codes

df_numerized

df

correlation_matrix = df_numerized.corr(method='pearson')
sns.heatmap(correlation_matrix, annot =True)
plt.title('Correlation Matric for Numeric Features')
plt.xlabel('Movie Features')
plt.ylabel('Movie Features')
plt.show()

df_numerized.corr()

correlation_mat = df_numerized.corr()
corr_pairs = correlation_mat.unstack()
corr_pairs

sorted_pairs = corr_pairs.sort_values()
sorted_pairs

high_corr = sorted_pairs[(sorted_pairs) > 0.5]
high_corr

#Votes and budget have the highest correlation to gross earnings

#Company has low correlation
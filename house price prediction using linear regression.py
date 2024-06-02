# -*- coding: utf-8 -*-
"""Day 41: Project 1 - House Price Prediction using Linear Regression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1w2fiy4bv_WjAS8sISVJxBYDGn0AoxM_P

# Importing the libraries
"""

import pandas as pd # Data Manipulation
import numpy as np # Numerical Python -> Mathematical operation
import matplotlib.pyplot as plt # Data visualization
import seaborn as sns # Data visualization
import re # Data Cleaning
from sklearn.linear_model import LinearRegression # Algorithm
from sklearn.preprocessing import LabelEncoder # Converting the categorical data into numerical data
from sklearn.metrics import r2_score # Accuracy Metric
from sklearn.model_selection import train_test_split # Spliting the dataset into training & testing dataset
import pickle

"""# Problem Statement

* You have been given a dataset that describes the functionality of houses. Now, based on the given features, you have to build a model to predict the house price.

# Defining the dataset

Link: https://drive.google.com/file/d/1yrVwfX1LjISQ6vdR1Kaht-S1_8y2Gk6z/view?usp=sharing
"""

df = pd.read_csv('/content/drive/MyDrive/ShapeAI DST 11021 Oct-Jan Batch 2021-22/Datasets/Housing.csv')

"""# EDA - Exploratory Data Analysis"""

df.head()

df.tail()

df.shape[0]

df.shape[1]

df.shape

df.columns

len(df.columns)

df.info()

df.describe()

df.dtypes

df.nunique()

df.isna().sum()

df.isna().sum().sum()

sns.boxplot(df.price) # Checking for the outliers

# IQR = Q3 - Q1

IQR = df.price.quantile(0.75) - df.price.quantile(0.25)
IQR

lower_limit = df.price.quantile(0.25) - 1.5*IQR
upper_limit = df.price.quantile(0.75) - 1.5*IQR

lower_limit

upper_limit

# -35000 to 22,75,000.0

df.price.describe()

17,50,000

# Find out the values that are outside the upper bound
df[df["price"] >upper_limit]

len(df)

545 - 527

df.head()

df.mainroad.unique()



# Yes -> 1
# No -> 0
df.mainroad.replace(['yes', 'no'], [1,0])

newdf = df.copy()

enc = LabelEncoder()

newdf.mainroad

newdf.mainroad = enc.fit_transform(newdf.mainroad)

newdf.head()

newdf.mainroad.unique()

newdf.basement.unique()

newdf.basement.value_counts()

newdf.basement

enc.fit_transform(newdf.basement)

df['mainroad'] = enc.fit_transform(df['mainroad'])
df['guestroom'] = enc.fit_transform(df['guestroom'])
df['basement'] = enc.fit_transform(df['basement'])
df['hotwaterheating'] = enc.fit_transform(df['hotwaterheating'])
df['airconditioning'] = enc.fit_transform(df['airconditioning'])
df['prefarea'] = enc.fit_transform(df['prefarea'])

df.head()

df.furnishingstatus.unique()

df.furnishingstatus.value_counts()

df.furnishingstatus = enc.fit_transform(df.furnishingstatus)

df.furnishingstatus.value_counts()

1 -> semi-furnished
2 -> unfurnished
0 -> furnished

"""# Observations:

1. Data Strength - 545
2. Number of Random Variables - 13
3. None of the columns contained Null Values
4. Columns - price, area, bedrooms, bathrooms, stories & parking has numerical values
5. Columns - mainroad, guestroom, hotwaterheating, airconditioning, preface & furnishing status has object values
"""

len(df)

len(df.columns)

df.dtypes

df.describe()

df.corr()

plt.figure(figsize=(10,10))
sns.heatmap(df.corr(), annot=True, cmap='Greens')

plt.scatter(df.area, df.price)
plt.xlabel('Area')
plt.ylabel('Price')
plt.grid()

sns.pairplot(df)

df.bedrooms.unique()

plt.figure(figsize=(50,50))
df.boxplot()

df[['area']].boxplot()

for i in df.columns:
  df[[f'{i}']].boxplot()
  plt.plot()

df.furnishingstatus.value_counts()

# How many values are there where bedrooms is more than 4
df.bedrooms[df.bedrooms >= 4].count()

df.bedrooms.value_counts().plot.bar()

sns.histplot(df.price)

# What is the price of the house where bedrooms are 4 and bathroom is 2
df[['price','bedrooms','bathrooms']][(df.bedrooms==4) & (df.bathrooms ==2)]
# Price Bedroom Bathroom

len(df[['price','bedrooms','bathrooms']][(df.bedrooms==4) & (df.bathrooms ==2)])

"""# Machine Learning

* Defining the model/algorithm
"""

model = LinearRegression()

"""* Defining the Independent & dependent variable"""

df.head(2)

X = df.iloc[:,1:]
y = df.price

X

"""# Train Test Split"""

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

len(X_train)

len(X_test)

"""* Training the model"""

model.fit(X_train, y_train)

model.coef_

# Cost function (Intercept Value)
model.intercept_

y = c +m1x1 + m2x2 + m3x3 +...+ m(n)x(n)

"""# Testing/Prediction"""

y_pred = model.predict(X_test)

y_pred

y_test

newdf = pd.DataFrame({"Actual Value": y_test,
                      "Predicted Value": y_pred})

newdf

plt.scatter(newdf['Actual Value'], newdf['Predicted Value'])
plt.xlabel('Actual Value')
plt.ylabel('Predicted Value')
plt.title('Actual V/s Predicted')

newdf.corr()

sns.heatmap(newdf.corr(), annot=True, cmap='magma')

plt.scatter(X_test.area, y_test)
plt.scatter(X_test.area, y_pred, color='r')
plt.plot(y,y, c='black')
plt.grid()

plt.scatter(y_test, y_pred)
plt.plot(y,y, c='black')
plt.grid()

"""# Performance"""

r2_score(y_test, y_pred)

# Accuracy = 65

model.predict([[2400, 2,2,2,2,2,2,1,1,1,1,1]])[0]

"""# Exporting the model"""

with open('model.pkl', 'wb') as files:
  pickle.dump(model, files)

df

def norm_fun(i):
  x = (i-i.min())/(i.max() - i.min())
  return x

df_normalize = norm_fun(df.iloc[:,1:])

df_normalize

df_normalize.describe()

df_normalize[['area']].boxplot()

0.6 - 1.0
# -*- coding: utf-8 -*-
"""Covid19_Vaccination_Rates.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mnqciM0HJsCnIJeaeX6IjITu-ueGX9E3

# insert intro

**Now we will import the needed libraries**
"""

from google.colab import drive #mounting drive 
drive.mount('/content/gdrive')

# Commented out IPython magic to ensure Python compatibility.
# Import pandas , scipy, and math
# %matplotlib inline
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import math

import seaborn as sns #importing seaborn for visualizations  
sns.set()

# suppress warnings (warnings do not prevent the code from executing)
import warnings
warnings.filterwarnings("ignore")

"""**Now we will read and test the mount of the CSV . We will also fill null values as well as begin some generic analysis.**  """

df = pd.read_csv('/content/gdrive/My Drive/Colab Datasets/country_vaccinations2021.csv')
df.head() # testing successful mount

"""This dataset has 2680 rows and 15 columns"""

df.shape #

"""Now we will check the dataframe for nulls . """

df.info() #Checking for nulls

"""There are some significant nulls in the people_fully_vaccinated_per_hundred, and people_fully_vaccinated columns, but we will not be using those in our analysis . Regardless, we will fill these nulls with an 'N/A'.

> Indented block

# **I will be working to analyze four hypotheses during this presentation.** 

---

They are listed below:
1.	How many people in the entire world have been vaccinated at least once?


2.	How many total vaccinations have been administered? 


3.	What are the top 5 countries in Daily Vaccinations?

4.	Is there a geographic relation in the top 10 countries regarding Daily Vaccinations?

# **Hypothesis 1**

**How many people in the entire world have been vaccinated at least once?**

We will begin by creating a bucket DF (hyp_1) for our specific columns used during this analysis.
"""

hyp_1 = df[['country', 'total_vaccinations', 'date']] # placing needed variables into bucket DF

hyp_1.dropna(how='any', inplace=True)

hyp_1.head()

"""There are 2680 rows and 2 columns in this dataframe. """

hyp_1.shape

"""There are 250 rows and 4 columns in the public dataframe. """

hyp_1['total_vaccinations'].describe().apply("{0:.5f}".format) # starter statistics

"""The mean is our most important number above. It shows a 1,249,890.33 average daily_vaccinations as averaged among all available countries. But this shows a drastic decline from the most vaccinations per country at 44,769,970.00.

The Histogram above shows that we have a normal distribution in our values within the column of Total Annual Cost.
"""

ax = sns.distplot(hyp_1['total_vaccinations'], kde=True) #normal distribution confirmed

sorted = hyp_1.sort_values(by='date')

month = pd.to_datetime(hyp_1['date'])

mon_year = month.dt.strftime('%b')

mon_year_dropped = mon_year[mon_year!= 'Dec']

sns.set_color_codes("pastel")

ax = sns.barplot(data=hyp_1, y='total_vaccinations', x=mon_year_dropped, color='b').set(xlabel='Month of 2021', ylabel='Total Vaccinations', title='Two Month Change')

total = hyp_1['total_vaccinations'].sum()

print(total)

print sum(hyp_1[i] for i in hyp_1['total_vaccinations'] if i != '2021-12-%%''2021-12-%%')

# Calculate the sample size, mean and variance of each sample...
# We will need this information to calculate standard errors


#!/usr/bin/env python
# coding: utf-8

# # Introduction
# *The data is pulled from NYC Open Data. It consists of records for Bus Breakdown and Delay system information from school bus vendors operating out in the field in real time. The key factors used in this data visualization are the reasons for the breakdown/delay, Bus Company Name, Number of students on the bus, county or state in which the delay occurred, Delay Notified or not.*
# 

# # Sources
# •	*The source code came from NYC Open Data
# •	The code retrieves data from API source 
# •	The link to create a account in Socrata 
# •	The code to create  plots using Seaborn Package*
# 

# # Explanation of the Code
# *The code begins by importing necessary Python packages:
# •	import seaborn as sns
# •	import matplotlib.pyplot as plt
# •	import datetime
# •	import calendar
# •	import pandas as pd
# •	from sodapy import Socrata*
# 

# In[11]:


import seaborn as sns
import matplotlib.pyplot as plt
import datetime
import calendar


# •	*Note:The following packages need to be installed:
# •	pip install seaborn
# •	pip install sodapy
# •	pip install pandas*
# 

# *We then import data from NYC Open Data using User Credentials and API Token by calling API .The following code extracts the data from its source using the API key by requesting the data from the host and reading their response. We then store the incoming data in a variable, read it, and then decode it so it can be used. In the following code, the data pulled using API is converted to a pandas data frame* 

# In[19]:


import pandas as pd
from sodapy import Socrata

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("data.cityofnewyork.us", None)

# Example authenticated client (needed for non-public datasets):
# client = Socrata(data.cityofnewyork.us,
#                  MyAppToken,
#                  userame="user@example.com",
#                  password="AFakePassword")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("ez4e-fazm", limit=2000)

df = pd.DataFrame.from_records(results)
df


# # Data Visualization:
# *The data extracted in the previous steps are used to visualize it for the first part of visualization, the below charts shows the different reasons reported by the driver, how much time each reasons are reported and the number of breakdown/delay occurred in different cities. The following code visualises the plot:*
# 
# 

# In[20]:


color = sns.color_palette()
reason = df['reason'].value_counts()
plt.figure(figsize=(12,8))
sns.barplot(reason.index, reason.values, alpha=0.8,  palette="deep")
plt.ylabel('Number of Occurrences', fontsize=12)
plt.xlabel('Reason type', fontsize=12)
plt.title('Count of Reason type', fontsize=15)
plt.xticks(rotation='vertical')
plt.show()

color = sns.color_palette()
loc = df['boro'].value_counts()
plt.figure(figsize=(12,8))
sns.barplot(x=loc.index, y= loc.values, palette="rocket")
plt.ylabel('Number of Occurrences', fontsize=12)
plt.xlabel('Location name', fontsize=12)
plt.title('Breakdown location count', fontsize=15)
plt.xticks(rotation='vertical')
plt.show()
plt.tight_layout()


# *The second part of visualization shows us the different bus companies and the number of breakdowns/delays for each company and it’s clear that the two companies LEESEL and RELIANT TRANS INC have the majority of breakdowns/delays. The following code visualises the Pie chart:*
# 

# In[21]:


#Using matplotlib
c=df["bus_company_name"].value_counts()
c=c.head(10)
pie, ax = plt.subplots(figsize=[10,6])
labels = c.keys()
plt.pie(x=c, autopct="%.1f%%", explode=[0.05]*10, labels=labels, pctdistance=0.5)
plt.title(" Bus Company name", fontsize=14)


# *The third part of visualisation shows the number of running late/breakdown buses in different cities and the number of Pre-K, school age students travelling by bus in different locations during a breakdown/running late. As evident from the plot, the busses running late due to traffic seems to be higher in all the cities and also the school age students travelling by bus are higher in all cities compared to the pre-k students. The following code visualises the plot:*
# 

# In[22]:


sns.set_theme(style="ticks")
i = sns.catplot(data=df,kind='count',x='boro',hue='school_age_or_prek', height=5,aspect=3)
plt.ylabel('Number of Occurrences', fontsize=12)
plt.xlabel('Location name', fontsize=12)
plt.title('Count of Pre-k and School-age students by location', fontsize=15)
ax = i.facet_axis(0,0)
for p in ax.patches:
    ax.text(p.get_x() , 
            p.get_height(), 
            '{0:.2f}'.format(p.get_height()), 
            color='black', rotation='horizontal', size='large')

sns.set_theme(style="ticks")
j = sns.catplot(data=df,kind='count',x='breakdown_or_running_late',hue='boro', height=6,aspect=3)
plt.ylabel('Number of Occurrences', fontsize=12)
plt.xlabel('Location name', fontsize=12)
plt.title('Breakdown/ Running late by location', fontsize=15)
ax = j.facet_axis(0,0)
for p in ax.patches:
    ax.text(p.get_x() + 0.015, 
            p.get_height() * 1.02, 
            '{0:.2f}'.format(p.get_height()), 
            color='black', rotation='horizontal', size='large')


# In[ ]:





# In[14]:


sns.set_theme(style="ticks")
g = sns.catplot(data=df,kind='count',x='boro',hue='has_contractor_notified_parents', height=6,aspect=3)
plt.ylabel('Number of Occurrences', fontsize=12)
plt.xlabel('Location name', fontsize=12)
plt.title('Notification to parents by location', fontsize=15)
ax = g.facet_axis(0,0)
for p in ax.patches:
    ax.text(p.get_x() + 0.015, 
            p.get_height() * 1.02, 
            '{0:.2f}'.format(p.get_height()), 
            color='black', rotation='horizontal', size='large')


# In[15]:


sns.set_theme(style="ticks")
h = sns.catplot(data=df,kind='count',x='boro',hue='has_contractor_notified_schools', height=6,aspect=3)
plt.ylabel('Number of Occurrences', fontsize=12)
plt.xlabel('Location name', fontsize=12)
plt.title('Notification to schools by location', fontsize=15)
ax = h.facet_axis(0,0)
for p in ax.patches:
    ax.text(p.get_x() + 0.015, 
            p.get_height() * 1.02, 
            '{0:.2f}'.format(p.get_height()), 
            color='black', rotation='horizontal', size='large')


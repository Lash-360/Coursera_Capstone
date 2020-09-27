import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
import pandas as pd
import matplotlib as mpl
import matplotlib.ticker as ticker
from sklearn import preprocessing
%matplotlib inline

!conda install -c anaconda xlrd --yes

#Download Seattle Police Department Accident data
!wget -O Data_Collisions.csv https://s3.us.cloud-object-storage.appdomain.cloud/cf-courses-data/CognitiveClass/DP0701EN/version-2/Data-Collisions.csv

df = pd.read_csv('Data_Collisions.csv')
df.head()

df.shape

df.columns

###Clean Data

Data visualization and pre-processing
Let’s see how many of each class is in our data set

<h4>Evaluating for Missing Data</h4>

The missing values are converted to Python's default. We use Python's built-in functions to identify these missing values. There are two methods to detect missing data:

missing_data = df.isnull()
missing_data.head

<h4>Count missing values in each column</h4>

for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")  

Based on the summary above, each column has 205 rows of data, seven columns containing missing data:
<ol>
        <li>"ADDRTYPE": 1926 missing data</li>
        <li>"INTKEY": 65070 missing data</li>
        <li>"LOCATION": 2677 missing data</li>
        <li>"EXCEPTRSNCODE": 84811 missing data</li>
        <li>"EXCEPTRSNDESC": 5638 missing data</li>
        <li>"COLLISIONTYPE": 4904 missing data </li>
        <li>"JUNCTIONTYPE": 6329 missing data</li>
        <li>"INATTENTIONIND": 164868 missing data</li>
        <li>"UNDERINFL": 4884 missing data</li>
        <li>"WEATHER": 5081 missing data</li>
        <li>"ROADCOND": 5012 missing data</li>
        <li>"LIGHTCOND": 5170 missing data</li>
        <li>"PEDROWNOTGRNT": 190006 missing data</li>
        <li>"SDOTCOLNUM": 79737 missing data</li>
        <li>"SPEEDING": 185340 missing data</li>
        <li>"ST_COLCODE": 18 missing data</li>
        <li>"ST_COLDESC": 4904 missing data</li>
        <li>"X": 5334 missing data</li>
        <li>"Y": 5334 missing data</li>
</ol>


The following columns will dropped as they have move missing datas under them which would affect the analysis:
<ol>
          <li>"INATTENTIONIND": 164868 missing data</li>
          <li>"PEDROWNOTGRNT": 190006 missing data</li>
          <li>"SPEEDING": 185340 missing data</li>
</ol>


#Drop data that are either irrelevant or the True value is more than 20%

to_drop =['SPEEDING', 'PEDROWNOTGRNT', 'INATTENTIONIND', 'INTKEY', 'SDOTCOLNUM',
         'INATTENTIONIND', 'JUNCTIONTYPE', 'EXCEPTRSNCODE', 'X', 'Y', 'OBJECTID',
          'COLDETKEY', 'EXCEPTRSNDESC', 'INCDATE', 'INCDTTM', 'SDOT_COLCODE',
         'SDOT_COLDESC', 'SDOTCOLNUM', 'ST_COLCODE', 'ST_COLDESC', 'SEGLANEKEY', 
          'CROSSWALKKEY', 'INTKEY', 'REPORTNO', 'STATUS', 'HITPARKEDCAR', 'LOCATION',
          'SEVERITYDESC', 'COLLISIONTYPE', 'INCKEY', 'PEDCOUNT', 'PEDCYLCOUNT', 
          'SEVERITYCODE.1', 'UNDERINFL', 'LIGHTCOND']
df.drop(to_drop, axis = 1, inplace = True)

df.shape

df.columns

df.info()

df['SEVERITYCODE'].value_counts()

df['ADDRTYPE'].value_counts()

df['PERSONCOUNT'].value_counts()

df['VEHCOUNT'].value_counts()

df['WEATHER'].value_counts()

df['ROADCOND'].value_counts()


# Remove values from ROADCOND because they are unknown
df = df [df['ROADCOND'] != 'Unknown']

# Remove values from WEATHER because they are unknown
df = df [df['WEATHER'] != 'Unknown']

df.info()

#The number columns that contain blank cells
df.isnull().sum(axis = 0)

#Drop all null values
df.dropna(inplace=True)

#install seaborn
!conda install -c anaconda seaborn -y

bins = np.arange(df.PERSONCOUNT.min(),8,1)
plt.hist(df.VEHCOUNT, bins = bins)
    
plt.title('No of Vehicles In Accidents')
plt.ylabel('Number of Accidents')
plt.xlabel('Number of Vehicle')
    
bins = np.arange(df.PERSONCOUNT.min(),17,2)
plt.hist(df.PERSONCOUNT, bins = bins)
    
plt.title('No of People In Accidents')
plt.ylabel('Number of Accidents')
plt.xlabel('Number of People')

X = df.ADDRTYPE.unique()
Data = df.ADDRTYPE.value_counts()
plt.bar(X, height=Data)
plt.xlabel('Location')
plt.ylabel('No of Accidents')
plt.title('No of Accidents In Reltions to Locations')

X = df.WEATHER.unique()
Data = df.WEATHER.value_counts()
plt.bar(X, height=Data)
plt.xlabel('Weather')
plt.ylabel('No of Accidents')
plt.title('No of Accidents In Reltions to Weather')
plt.xticks(rotation= 90)
plt.show()

X = df.ROADCOND.unique()
Data = df.ROADCOND.value_counts()
plt.bar(X, height=Data)
plt.xlabel('Road Condiction')
plt.ylabel('No of Accidents')
plt.title('No of Accidents In Reltions to Road Condiction')
plt.xticks(rotation= 90)
plt.show()

import seaborn as sns

bins = np.linspace(df.VEHCOUNT.min(), df.VEHCOUNT.max(), 10)
g = sns.FacetGrid(df, col="ADDRTYPE", hue="SEVERITYCODE", palette="Set1", col_wrap=2)
g.map(plt.hist, 'VEHCOUNT', bins=bins, ec="k")
g.axes[-1].legend()
plt.show()

bins = np.linspace(df.PERSONCOUNT.min(), df.PERSONCOUNT.max(), 18)
g = sns.FacetGrid(df, col="ADDRTYPE", hue="SEVERITYCODE", palette="Set1", col_wrap=2)
g.map(plt.hist, 'PERSONCOUNT', bins=bins, ec="k")
g.axes[-1].legend()
plt.show()



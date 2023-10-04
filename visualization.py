import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd 

data = pd.read_csv('C:/Users/No Name/OneDrive/Desktop/vezba/1923.csv')

sns.barplot(x='Date', y='Occurrence', data=data)

plt.show()


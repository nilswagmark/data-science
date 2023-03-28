import numpy as np
data = np.genfromtxt('data.csv', delimiter=',')


import csv
opened_file = open('hacker_news.csv')
read_file = csv.reader(opened_file)
hn = list(read_file)
headers = hn[0]
hn = hn[1:]
print(headers)
print(hn[0:5])



import pandas as pd
f500 = pd.read_csv('f500.csv',index_col=0)
f500.index.name = None

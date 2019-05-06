import pandas as pd
import glob
import shutil
import os

data = pd.read_csv("final-classes.csv")
code = pd.read_csv("class-descriptions-boxable.csv")
classes = []
codes = []

for i, row in data.iterrows():
	classes.append(row['Classes'])
	
for i, row in code.iterrows():
	if row['Tortoise'] in classes: 
		codes.append(row['/m/011k07'])
	
i = 0
for j,k in zip(codes,classes):
	temp = "new_f.loc[new_f['LabelName'] == '"+j+"', 'ClassNumber'] =" + str(i)
	print(temp.strip())
	i+=1
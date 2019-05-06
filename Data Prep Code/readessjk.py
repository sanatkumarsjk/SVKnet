import pandas as pd
import glob
import shutil
import os

data = pd.read_csv("final-classes.csv")
folderpath = []
str = ''

dst_dir = ""

for i, row in data.iterrows():
	for jpgfile in glob.iglob(os.path.join("OIDv4_ToolKit/OID/Dataset/train/"+row['Classes'].replace(" ", "-"), "*.jpg")):
		shutil.copy(jpgfile, dst_dir)
	str += row['Classes'].replace(" ", "_")+ ' '

print("python main.py downloader --classes "+str +" --type_csv train")
# print (folderpath)
	# folderpath.append("OIDv4_ToolKit/OID/Dataset/train/"+row['Classes'].replace(" ", "-"))


import pandas as pd
import os
Folder_Path = r'results/tabular'          
SaveFile_Name = r'all.csv'             
file2 = r'tabular-2022-04-06 20-21-41.csv'
file1 = r'tabular-2022-04-07 02-01-19.csv'
 
os.chdir(Folder_Path)

df = pd.read_csv(file1)  
 
df.to_csv(SaveFile_Name,encoding="utf_8_sig",index=False)
 
df = pd.read_csv(file2)
df.to_csv(SaveFile_Name,encoding="utf_8_sig",index=False, header=False, mode='a+')

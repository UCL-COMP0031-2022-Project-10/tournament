
import pandas as pd
import os
Folder_Path = r'results/dqn'          
SaveFile_Name = r'all.csv'             
file2 = r'dqn-1hl-2022-04-07 01-43-25.csv'
file1 = r'dqn-1hl-2022-04-07 01-03-04.csv'
 
os.chdir(Folder_Path)

df = pd.read_csv(file1)  
 
df.to_csv(SaveFile_Name,encoding="utf_8_sig",index=False)
 
#循环遍历列表中各个CSV文件名，并追加到合并后的文件
df = pd.read_csv(file2)
df.to_csv(SaveFile_Name,encoding="utf_8_sig",index=False, header=False, mode='a+')

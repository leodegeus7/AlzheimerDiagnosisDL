import pandas as pd
import fnmatch
import shutil

data = pd.read_csv('finalDataFrame.csv')
data.head()

directory = os.getcwd()
if not os.path.exists(directory + "/ProcessedImage/" + "AD"):
            os.makedirs(directory + "/ProcessedImage/" + "AD")
if not os.path.exists(directory + "/ProcessedImage/" + "Normal"):
            os.makedirs(directory + "/ProcessedImage/" + "Normal")
    
for index, row in data.iterrows():
    image = row["Image Name"]
    dx = row["DX Group"]
    if dx == "Normal":
        fullname = directory + "/ProcessedImage/" + image
        shutil.move(fullname, directory + "/ProcessedImage/Normal/" + image)
    if dx == "AD":
        fullname = directory + "/ProcessedImage/" + image
        shutil.move(fullname, directory + "/ProcessedImage/AD/" + image)
    


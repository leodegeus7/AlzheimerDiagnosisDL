
# coding: utf-8

# In[87]:


import numpy as np
import pandas as pd


# In[92]:


dataFrame = pd.read_csv("idaSearch_3_19_2018.csv")
dataFrame.head()


# In[93]:


dataFrame = dataFrame.drop(['Description','Structure'],axis=1)
dataFrame.head()


# In[94]:


import os
import fnmatch
images = []
imageNames = []
for path,dirs,files in os.walk('.'):
    for f in fnmatch.filter(files,'*.png'):
        fullname = os.path.abspath(os.path.join(path,f))
        splits = f.split("_")
        subject = splits[1] + "_S_" + splits[3]
        imageNames.append(f)
        images.append(subject)
        index = [str(i) for i in range(1, len(images)+1)]
        imagesDF = pd.DataFrame(images, index=index)
        
        
imagesDF #subject
imagesDF["Image Name"] = imageNames
imagesDF.columns = ["Subject ID", "Image Name"]
imagesDF.head()


# In[97]:



dataFrame = dataFrame.drop_duplicates()
dataFrame

merged_data = pd.merge(left=imagesDF, right=dataFrame, how='left', on="Subject ID")
merged_data.head()
merged_data.to_csv('finalDataFrame.csv')


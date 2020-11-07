
# coding: utf-8

# In[1]:


import tarfile
import pandas as pd
with tarfile.open("TrafficEvents_Aug16_June20_Publish.csv.tar.gz", "r:*") as tar:
    csv_path = tar.getnames()[0]
    df = pd.read_csv(tar.extractfile(csv_path), header=0, sep=",")
    


# In[2]:


df.head()


# In[ ]:


#import pandas
#import feather
#df = feather.read_dataframe('df.feather')


# In[ ]:


import csv


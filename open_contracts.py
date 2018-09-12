
# coding: utf-8

# In[451]:


import pandas as pd
import numpy as np
import json


# In[452]:


dt = pd.read_csv('trading_record.csv',index_col=False)
try:
    del dt['Date']
except:
    pass


# In[453]:


dt_group = dt.groupby(['Underlying','Contract Month','Strike Price','Long/Short','Call/Put'])

labels = ['Underlying','Contract Month','Strike Price','Long/Short','Call/Put','Avg Price','Total Size']
dt_summary = pd.DataFrame([],columns=labels)
for group_name in list(dt_group.groups):
    option_data = dt_group.get_group(group_name)
    total_size = sum(option_data['Size'])
    avg_price = (sum(option_data['Price'] * option_data['Size']))/total_size
    summary = [group_name[0], group_name[1], group_name[2], group_name[3], group_name[4], avg_price, total_size]
    dt_summary = dt_summary.append(pd.Series(summary, index=labels),ignore_index = True)

def long_short(row):
    if row['Long/Short'] == 'L':
        return row['Total Size']
    if row['Long/Short'] == 'S':
        return row['Total Size'] * -1
    

dt_summary['direction'] = dt_summary[['Long/Short','Total Size']].apply(long_short, axis=1)


# In[454]:


labels = ['Underlying','Contract Month','Strike Price','Call/Put','Avg Long Price','Avg Short Price','Total Size','P/L','Net Size']

dt_summary_group = dt_summary.groupby(['Underlying','Contract Month','Strike Price','Call/Put'])

option_summary = pd.DataFrame([],columns=labels)

with open('stock_lots.json') as outputfile:
    lot_size = json.load(outputfile)
    


for group_name in list(dt_summary_group.groups):
    group_data = dt_summary_group.get_group(group_name)
    
    try:
        avg_long_price = float(group_data[group_data['Long/Short'] == 'L' ]['Avg Price'])
    except:
        avg_long_price = 0
        
    try:
        avg_short_price = float(group_data[group_data['Long/Short'] == 'S' ]['Avg Price'])
    except:
        avg_short_price = 0
    
    try:
        avg_long_price = float(group_data[group_data['Long/Short'] == 'L' ]['Avg Price'])
    except:
        avg_long_price = 0
        
    try:
        avg_short_price = float(group_data[group_data['Long/Short'] == 'S' ]['Avg Price'])
    except:
        avg_short_price = 0
    
    total_size = max(group_data['Total Size'])
    
    profit_per = (avg_short_price - avg_long_price) * total_size
    
    profit = int(profit_per * int(lot_size[str(group_name[0])]))
    
    data = [group_name[0], group_name[1], group_name[2] ,group_name[3] ,avg_long_price ,avg_short_price , total_size, profit, sum(group_data['direction'])]
    
    option_summary = option_summary.append(pd.Series(data, index=labels),ignore_index = True)


# In[456]:


#print (option_summary.sort_values(['Contract Month','Underlying'], ascending=True))

print ((option_summary.sort_values(['Contract Month','Underlying'], ascending=True)).to_string(index=False))


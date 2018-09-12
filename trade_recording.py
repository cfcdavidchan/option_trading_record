
# coding: utf-8

# In[41]:


import datetime, sys
import pandas as pd
todays_date = datetime.datetime.now().date()
today_month = datetime.datetime.now().month



def input_data():

    date = input('Date (yyyymmdd)? Today is %s. Press enter for today\n'%(str(todays_date)))
    if date == '':
        date = todays_date
    if type(date) == str:
        try:
            date = datetime.datetime.strptime(date, '%Y%m%d').date()
        except:
            sys.exit('%s is incorrect formate' %date)
    date = date.strftime('%Y-%m-%d')

    while True:
        call_put = input('Call (C) or Put (P) ?\n')
        if call_put.upper() not in ['C','P']:
            print ('%s is incorrect formate' %call_put)
        else:
            call_put = call_put.upper()
            break

    while True:
        long_short = input('Long(L) or Short(S) ?\n')
        if long_short.upper() not in ['L','S']:
            print ('%s is incorrect formate' %long_short)
        else:
            long_short = long_short.upper()
            break

    underlying = input('Underlying ?\n')

    contract_month = input('Contract Month ? This month is %s. Press enter for %s\n'%(str(today_month),str(today_month)))
    
    if contract_month == '':
        contract_month = str(today_month)


    strike_price = input('Strike Price ?\n')

    price = float(input('Pirce? \n'))
    
    size = int(input('Size? \n'))
    
    return [date , underlying,call_put ,long_short, contract_month, strike_price, price, size]


# In[120]:


if __name__ == '__main__':

    while True:
        labels = ['Date' ,'Underlying', 'Call/Put','Long/Short','Contract Month','Strike Price','Price','Size']
        record = input_data()
        
        try:
            dt = pd.read_csv('trading_record.csv',index_col=False)
            dt = dt.append(pd.Series(record, index=labels),ignore_index = True)
        except:
            
            dt = pd.DataFrame([record],columns=labels)
        
        dt.to_csv('trading_record.csv', index=False)
        
        end_message = input('Finished ? \n')
        if end_message == '' or end_message in ['Y','y']:
            break


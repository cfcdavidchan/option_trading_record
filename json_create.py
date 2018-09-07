
# coding: utf-8
import json

def stock_info():
    stock = input('Stock ?\n')
    lots = input('Lot size ?\n')
    
    return stock, lots

if __name__ == "__main__":
    while True:
        stock, lots = stock_info()
        
        try:
            with open('stock_lots.json') as outputfile:
                stock_data = json.load(outputfile)
                
                if stock in stock_data:
                    print ('%s is already with %s lot size' %(stock, lots))
                    pass
                else:
                    stock_data[stock] = lots
                    
                    with open('stock_lots.json' ,'w') as outputfile:
                        json.dump(stock_data, outputfile, sort_keys=True)
                
        except :
            stock_data = dict()
            stock_data[stock] = lots
            with open('stock_lots.json' ,'w') as outputfile:######aasdasd
                json.dump(stock_data, outputfile, sort_keys=True)
            print ('Now create json file')
        
        end_message = input('Finished ? \n')
        if end_message == '' or end_message in ['Y','y']:
            break


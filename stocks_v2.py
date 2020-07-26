
#when adding new stock create the object with name of stock and define its parameters(minprice or maxprice or both) and ADD THE stock to the object list as well!!!!

import requests
import json
import os

def telegram(telegram_token,chat_id,message):
    url=f'https://api.telegram.org/bot{telegram_token}/sendMessage'
    payload={"chat_id":chat_id,"text": message}
    telegram_data=requests.post(url=url,json=payload)
    return telegram_data.json()

class Stock:
    def __init__(self,stock_code):
        self.stock_code=stock_code
    @property
    def stockprice(self):
        data=requests.get(f'https://in.finance.yahoo.com/quote/{self.stock_code}?p={self.stock_code}').text
        x=data.find('currentPrice')
        pos=x+21
        prc=''
        while True:
            if data[pos].isnumeric()==True:
                prc+=data[pos]
                pos+=1
            else:
                break
        return int(prc)
    @property
    def isLessThanMinPrice(self):
        if self.stockprice<=self.minprice:
            return True
        else:
            return False
    
    @property
    def isGreaterThanMaxPrice(self):
        if self.stockprice>=self.maxprice:
            return True
        else:
            return False

website_is_running=requests.get('https://in.finance.yahoo.com').ok  #tests if the website is up

stock_dict={
    'HDFCBANK.NS':{'minprice':900,'maxprice':2000},
    'TCS.NS':{'minprice':2000,'maxprice':2500},
    'RELIANCE.NS':{'minprice':1500,'maxprice':2500},
    'BHARTIARTL.NS':{'minprice':400,'maxprice':900},
    'HINDUNILVR.NS':{'minprice':1900,'maxprice':2500},
    'INFY.NS':{'minprice':800,'maxprice':1200},
    'HCLTECH.NS':{'minprice':500,'maxprice':1000},
    'ASIANPAINT.NS':{'minprice':1500,'maxprice':2000},
    'KOTAKBANK.NS':{'minprice':1100,'maxprice':1500},
    'IRCTC.NS':{'minprice':1100,'maxprice':1500},
    'PIDILITIND.NS':{'minprice':1100,'maxprice':1500}

    
    
    }




d_min={}
d_max={}
for key in stock_dict:
    obj=Stock(key)
    obj.minprice=stock_dict[key]['minprice']
    obj.maxprice=stock_dict[key]['maxprice']
    if obj.isLessThanMinPrice is True:
        d_min[key]=obj.stockprice
    if obj.isGreaterThanMaxPrice is True:
        d_max[key]=obj.stockprice

message=''

if d_min=={} and d_max=={}:
    pass
elif d_min!={} and d_max=={}:
    message+='These stocks are low in price: \n'
    for k in d_min:
        message+= f'{k} : {d_min[k]} \n' 

elif d_min=={} and d_max!={}:
    message+='These stocks are high in price: \n'
    for k in d_max:
        message+= f'{k} : {d_max[k]} \n' 

elif d_min!={} and d_max!={}:
    message+='These stocks are low in price: \n'
    for k in d_min:
        message+= f'{k} : {d_min[k]} \n' 

    message+='\nThese stocks are high in price: \n'

    for k in d_max:
        message+= f'{k} : {d_max[k]} \n'

def lambda_handler(event,context):
    telegram_token=os.getenv('TELEGRAM_TOKEN')
    chat_id=os.getenv('CHAT_ID')
    log_chat_id=os.getenv('LOG_CHAT_ID')
    if message!='':
        data=telegram(telegram_token,chat_id,message)
        return data
    elif message=='':
        return 'All OK'
    

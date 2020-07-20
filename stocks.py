import requests
import json
import os
class Stock:
    def __init__(self,stock_code):
        self.stock_code=stock_code
    @property
    def stockprice(self):
        data=requests.get(f'https://in.finance.yahoo.com/quote/{self.stock_code}?p={self.stock_code}').text
        x=data.find('currentPrice')
        pos=x+21
        price=''
        while True:
            if data[pos].isnumeric()==True:
                price+=data[pos]
                pos+=1
            else:
                break
        return int(price)
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

hdfcbank=Stock('HDFCBANK.NS')
hdfcbank.minprice=900

reliance=Stock('RELIANCE.NS')
reliance.minprice=1500

airtel=Stock('BHARTIARTL.NS')
airtel.minprice=400

hindustan_unilever=Stock('HINDUNILVR.NS')
hindustan_unilever.minprice=1900
hindustan_unilever.maxprice=2500

tcs=Stock('TCS.NS')
tcs.minprice=2000
tcs.maxprice=2500

infosys=Stock('INFY.NS')
infosys.minprice=800
infosys.maxprice=1200

hcl=Stock('HCLTECH.NS')
hcl.minprice=500
hcl.maxprice=1000

asian_paints=Stock('ASIANPAINT.NS')
asian_paints.minprice=1500
asian_paints.maxprice=2000

kotak_mahindra=Stock('KOTAKBANK.NS')
kotak_mahindra.minprice=1100
kotak_mahindra.maxprice=1500

irctc=Stock('IRCTC.NS')
irctc.minprice=1100
irctc.maxprice=1500

pidilite=Stock('PIDILITIND.NS')
pidilite.minprice=1100
pidilite.maxprice=1500




def lambda_handler(event,context):
    assert website_is_running is True
    d_min={}
    d_max={}
    obj_list_min=[hdfcbank,airtel,reliance,tcs,hindustan_unilever,infosys,hcl,asian_paints,kotak_mahindra,irctc,pidilite]
    obj_list_max=[tcs,hindustan_unilever,infosys,hcl,asian_paints,kotak_mahindra,irctc,pidilite]
    for i in obj_list_min:
        if i.isLessThanMinPrice is True:
            d_min[i.stock_code]=i.stockprice
        else:
            continue
    for j in obj_list_max:
        if i.isGreaterThanMaxPrice is True:
            d_max[i.stock_code]=i.stockprice
        else:
            continue
    
    if d_min=={} and d_max=={}:
           return 'All OK'
        
    
    elif d_min!={} and d_max=={}:
        message='These stocks are low in price \n'+json.dumps(d_min)
        telegram_token=os.getenv('TELEGRAM_TOKEN')
        chat_id=os.getenv('CHAT_ID')

        bot_url=f'https://api.telegram.org/bot{telegram_token}/sendMessage'
        payload={"chat_id":chat_id,"text": message}

        telegram_data=requests.post(url=bot_url,json=payload)
        return telegram_data.json()
    
    elif d_min=={} and d_max!={}:
        message='These stocks are high in price \n'+json.dumps(d_max)
        telegram_token=os.getenv('TELEGRAM_TOKEN')
        chat_id=os.getenv('CHAT_ID')

        bot_url=f'https://api.telegram.org/bot{telegram_token}/sendMessage'
        payload={"chat_id":chat_id,"text": message}

        telegram_data=requests.post(url=bot_url,json=payload)
        return telegram_data.json()
    
    elif d_max!={} and d_min!={}:
        message='These stocks are low in price \n' + json.dumps(d_min) + '\n These stocks are high in price \n' + json.dumps(d_max)
        telegram_token=os.getenv('TELEGRAM_TOKEN')
        chat_id=os.getenv('CHAT_ID')

        bot_url=f'https://api.telegram.org/bot{telegram_token}/sendMessage'
        payload={"chat_id":chat_id,"text": message}

        telegram_data=requests.post(url=bot_url,json=payload)
        return telegram_data.json()
    



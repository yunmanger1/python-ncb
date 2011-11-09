# -*- mode: python; coding: utf-8; -*-
import time, urllib
from xml.etree.ElementTree import fromstring

rates = {}

url = 'http://www.nationalbank.kz/rss/rates_all.xml'

def get_rates():
    et = fromstring(urllib.urlopen(url).read())
    date = time.strftime('%Y-%m-%d',time.localtime())
    results = et.findall('channel/item')
    for item in results:
        curr =  item.find('title').text
        date = item.find('pubDate').text
        rate = float(item.find('description').text)
        n = int(item.find('quant').text)
        rates[curr] = (rate, date, n)
    return rates

def in_kzt(amount = 1):
    if not rates.has_key('RUB'):
        get_rates()
    rate, date, n = rates.get('RUB')
    return float(amount) * rate 

def get_rate(curr):
    if not rates.has_key(curr):
        get_rates()
    try:
        rate, date, n = rates.get(curr)
        return rate
    except:
        return None
    
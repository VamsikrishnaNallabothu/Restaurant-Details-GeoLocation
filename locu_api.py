#!/usr/bin/env python

import urllib2
import json

locu_api = str(raw_input('your apikey: '))

def locu_search(query):
	api_key = locu_api
	url = 'https://api.locu.com/v1_0/venue/search/?api_key=' + api_key
	locality = query.replace(' ', '%20')
	final_url = url+ "&locality=" + locality + "&category=restaurant&country=United%20States"
	Data = urllib2.urlopen(final_url)
	jsn_data = json.load(Data)
	for items in jsn_data['objects']:
		print 'Hotel:'+items['name'],'Street_address:'+items['street_address'],'Phone:'+items['phone']
		print 'longitude:'+str(items['long']),'Latitude:'+str(items['lat']),'Postal code:'+items['postal_code']
		print '\n'


'''
Search using: locu_search('new york')

'''



#! /usr/bin/env python
# Basic script to grab the current time for a few different locations that I need to know the time of often
 
import requests

r = requests.get('http://www.timeanddate.com/worldclock/')

direct = r.text

newyork = direct.split('New York')[1].split('rbi>')[1].split('<')[0]

brisbane = direct.split('Brisbane')[1].split('rbi>')[1].split('<')[0]

brno = direct.split('Brussels')[1].split('rbi>')[1].split('<')[0]

print "Brno: " + brno + ''
print "Brisbane: " + brisbane + ''
print "New York: " + newyork + ''

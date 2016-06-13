#! /usr/bin/env python
# Basic script that allows you to start a google search from command line 
import os
import urllib
google_input = raw_input("Google: ")
google = urllib.quote(google_input)
os.system('firefox http://www.google.com/search?q=%s' % (google))

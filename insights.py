import os, sys
os.dup2(2,3)
stderr = os.fdopen(2,'a')
stderr.close()
import matplotlib
matplotlib.use('Agg')
from pylab import *
os.dup2(3,2)
sys._stderr_ = sys.stderr = os.fdopen(2,'a')
import csv

# tools for debugging
import sys
import cgitb
cgitb.enable()
sys.stderr = sys.stdout

# chunks of html
html_start = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Fatal Crashes in Australia</title>
<link rel="stylesheet" href="pivot_table.css" type="text/css" media="screen" charset="utf-8" />
</head>
<body><div class="container"> '''

html_end = '''
</div></body></html>'''

# csv file location
csv_loc = "fatal_crashes_5_years.csv"

# hypothesis titles ....[PHILIP, EDIT THEM AFTER ALL GRAPHS HAS BEEN GENERATED]
ht_header1 = 'The number of fatalities due to road crashes has decreased in\
              the last 5 years.'
ht_header2 = 'There has been more fatalities due to road crashes between\
              1pm-6pm than any other 5-hour interval in the last 5 years.'
ht_header3 = 'There has been more fatalities due to road crashes in NSW than\
              any other state in the last 5 years.'
ht_header4 = 'There has been more fatalities due to road crashes in Friday\
              and the weekends than the other weekdays.'
ht_header5 = 'Speed Limit lower than 50 has very few fatalities.

# hypothesis explanations [PHILIP, WRITE THESE AFTER ALL GRAPHS HAS BEEN GENERATED]
ht_xpln1 = ''
ht_xpln2 = ''
ht_xpln3 = ''
ht_xpln4 = ''





# main function which controls all the action
main()



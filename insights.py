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
from collections import defaultdict

# tools for debugging
#import sys
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
ht_header5 = 'Speed Limit lower than 50 has very few fatalities.'

# hypothesis explanations [PHILIP, WRITE THESE PARAGRAPHS AFTER ALL GRAPHS HAS BEEN GENERATED]
ht_xpln1 = ''
ht_xpln2 = ''
ht_xpln3 = ''
ht_xpln4 = ''

# independent variable for data dictionaries for each hypothesis
ht_var1 = 'Year'
ht_var2 = 'Hour'
ht_var3 = 'State'
ht_var4 = 'Dayweek'
ht_var5 = 'Speed Limit'

dep_var = 'Number of Fatalities' # depedendent variable

def vs_year(data): #ASIR, line graph
    print data # test



def vs_time(data): #MUBASHWER, Histogram
    print data # test



def vs_state(data): #ASIR, bar chart
    print data # test



def vs_day(data): #PHILIP, Pie Chart
    print data # test



def vs_speed_limit(data): #MUBASHWER, Scatter Plot
    print data # test

# main function which controls all the action                    
def main():
    # load data from csv file
    csvfile = open(csv_loc)
    data = csv.DictReader(csvfile)
    
    # data dictionaries for each hypothesis are initialized
    ht_data1, ht_data2 = defaultdict(int), defaultdict(int) 
    ht_data3, ht_data4 = defaultdict(int), defaultdict(int)
    ht_data5 = defaultdict(int)
    
    for row in data:
        fatalities = int(row[dep_var])
        ht_data1[row[ht_var1]] += fatalities
        if '-9' not in row[ht_var2]:
            ht_data2[int(row[ht_var2])] += fatalities
        ht_data3[row[ht_var3]] += fatalities
        ht_data4[row[ht_var4]] += fatalities
        if '-9' not in row[ht_var2]:
            ht_data5[int(row[ht_var5])] += fatalities
    csvfile.close()
    print 'Content-Type: text/html\n'        
    
    vs_year(ht_data1)
    vs_time(ht_data2)
    vs_state(ht_data3)
    vs_day(ht_data4)
    vs_speed_limit(ht_data5)
    
        
# main function which controls all the action
main()



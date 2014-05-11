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



def webshow(img): # call this function and serve to check graph
    savefig(img, dpi=50)
    print '<img width="400" height="300" src="'+img+'" />'



def vs_year(data): #ASIR, line graph
    clf()
    print data # test



def vs_hour(data): #MUBASHWER, histogram
    clf()
    hist(data.keys(), bins = arange(0,25), weights = data.values(), facecolor="green")
    xticks(arange(0,24,2), ['{:02d}'.format(hour) for hour in arange(0,24,2)])
    grid(True) 
    xlabel('Time (Hours in a Day)')
    ylabel('Number of fatalities')
    title('Histogram for Fatalities vs Time')
    webshow('vs_hour.png')
    



def vs_state(data): #ASIR, bar chart
    clf()
    print data # test



def vs_day(data): #PHILIP, Pie Chart
    clf()
    print data # test



def vs_speed_limit(data): #MUBASHWER, Scatter Plot
    clf()
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
    
    # store data in dictionaries for each hypothesis
    for row in data:
        fatalities = int(row[dep_var])
        ht_data1[row[ht_var1]] += fatalities
        if '-9' not in row[ht_var2]:
            ht_data2[int(row[ht_var2])] += fatalities
        ht_data3[row[ht_var3]] += fatalities
        ht_data4[row[ht_var4]] += fatalities
        if '-9' not in row[ht_var5]:
            ht_data5[int(row[ht_var5])] += fatalities
    csvfile.close()
    print 'Content-Type: text/html\n'        
    
    # remove the hashtag for the function you are working on to test them
    #vs_year(ht_data1)
    vs_hour(ht_data2)
    #vs_state(ht_data3)
    #vs_day(ht_data4)
    #vs_speed_limit(ht_data5)
    
        
# main function which controls all the action
main()



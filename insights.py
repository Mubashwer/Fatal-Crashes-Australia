import os, sys
os.dup2(2,3)
stderr = os.fdopen(2,'a')
stderr.close()
import matplotlib
matplotlib.use('Agg')
from pylab import *
os.dup2(3,2)
sys._stderr_ = sys.stderr = os.fdopen(2,'a')
from numpy import *
import csv
from collections import defaultdict
import calendar

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
<link rel="stylesheet" href="insights.css" type="text/css" media="screen" charset="utf-8" />
</head>
<body><div class="container"> '''

html_end = '''
</div></body></html>'''

# csv file location
csv_loc = "fatal_crashes_5_years.csv"

# hypothesis titles ....[PHILIP, EDIT THEM AFTER ALL GRAPHS HAS BEEN GENERATED]
ht_header1 = '''The total number of fatalities due to road crashes decreased in the last 5 years.'''
ht_header2 = '''There were more fatalities due to road crashes towards the end of the week.'''
ht_header3 = '''There were more fatalities due to road crashes between 1pm-6pm than any other 5-hour interval.'''
ht_header4 = '''There were more fatalities due to road crashes in New South Wales than any other state.'''
ht_header5 = '''There were very few fatalities due to crashes in roads with speed limit lower than 50 km/h.'''

# hypothesis explanations [PHILIP, WRITE THESE PARAGRAPHS AFTER ALL GRAPHS HAS BEEN GENERATED]
ht_xpln1 = '''efwsegwsegeswrtfwegws'''
ht_xpln2 = '''qrfqt3eqftq3et3qt'''
ht_xpln3 = '''etqetrw3trwt4t4t4t4t'''
ht_xpln4 = '''It can be seen in the bar chart that the number of fatalities in New South Wales is larger than all
 other states by a great margin. One of the possible reasons is that it is the most populated state. States with relatively low
 population had very few fatalities such as Northern Territory, Australian Capital Territory and Tasmania.'''
ht_xpln5 = '''q3erfefrewqr343r3rer'''

# independent variable for data dictionaries for each hypothesis
ht_var1 = 'Year'
ht_var2 = 'Dayweek'
ht_var3 = 'Hour'
ht_var4 = 'State'
ht_var5 = 'Speed Limit'

dep_var = 'Number of Fatalities' # depedendent variable

# file names for each visualisation
ht_img1 = 'vs_year.png'
ht_img2 = 'vs_day.png'
ht_img3 = 'vs_hour.png'
ht_img4 = 'vs_state.png'
ht_img5 = 'vs_speed_limit.png'

page ='''
<h1>When and where in Australia have fatal crashes occured the most in the last 5 years?</h1>
<div class="hypothesis" id="hypothesis1">
    <h2 class="header">{}</h2>
    <div class="visual"><img src="{}" alt="image1" width="500" height="375"></div>
    <p class="explain">{}</p>
</div>
<div class="hypothesis">
    <h2 class="header" id="header2">{}</h2>
    <div class="visual"><img src="{}" alt="image2" width="500" height="375"></div>
    <p class="explain">{}</p>
</div>
<div class="hypothesis" id="hypothesis3">
    <h2 class="header">{}</h2>
    <div class="visual"><img src="{}" alt="image2" width="500" height="375"></div>
    <p class="explain">{}</p>
</div>
<div class="hypothesis">
    <h2 class="header">{}</h2>
    <div class="visual""><img src="{}" alt="image2" width="500" height="375"></div>
    <p class="explain">{}</p>
</div>
<div class="hypothesis">
    <h2 class="header">{}</h2>
    <div class="visual"><img src="{}" alt="image2" width="500" height="375"></div>
    <p class="explain"">{}</p>
</div>
'''.format(ht_header1, ht_img1, ht_xpln1, ht_header2, ht_img2, ht_xpln2,
           ht_header3, ht_img3, ht_xpln3, ht_header4, ht_img4, ht_xpln4,
           ht_header5, ht_img5, ht_xpln5)


def vs_year(data): #ASIR, line graph
    clf()
    y = [item[1] for item in sorted(data.items(), key=lambda x: x[0])]
    plot(y, color='purple')
    xticks(arange(5), sorted(data.keys()), rotation=30)
    grid(True)
    xlabel('Time (Year)')
    ylabel(dep_var)
    title('Line Graph for Fatalities vs Time')
    savefig(ht_img1, dpi=100)

    
def vs_day(data): #PHILIP, Pie Chart
    clf()
    values = []
    labels = list(calendar.day_name)
    for day in labels:
        values += [data[day]]
    colors = ['b','g','r','c','m','y','#cccccc']
    pie(values, explode=None, labels=labels, autopct='%1.1f%%', shadow=True,
        colors=colors)

    title('Number of Fatalities Due to Road Crashes in Different Days of a Week',
          bbox={'facecolor':'0.8', 'pad':5})
    savefig(ht_img2, dpi=100)


def vs_hour(data): #MUBASHWER, histogram
    clf()
    hist(data.keys(), bins = arange(0,25), weights = data.values(), facecolor='green')
    xticks(arange(0,24,2), ['{:02d}'.format(hour) for hour in arange(0,24,2)])
    grid(True) 
    xlabel('Time (Hours in a Day)')
    ylabel(dep_var)
    title('Histogram for Fatalities (Road Crashes) vs Time')
    savefig(ht_img3, dpi=100)

    
    
def vs_state(data): #ASIR, bar chart
    clf()
    bars = arange(len(data))
    heights = [item[1] for item in sorted(data.items(), key=lambda x: x[0])]
    bar(bars, heights, align='center', facecolor='orange')
    xticks(bars, sorted(data.keys()), rotation=30)
    grid(True) 
    xlabel('State')
    ylabel(dep_var)
    title('Bar Chart for Fatalities (Road Crashes) vs State')    
    savefig(ht_img4, dpi=100)

    
def vs_speed_limit(data): #MUBASHWER, Scatter Plot
    clf()
    scatter(data.keys(), data.values(), s = data.values(), color = 'red')
    yticks(arange(0,3000,500))
    grid(True) 
    xlabel('Speed Limit (km/h)')
    ylabel(dep_var)
    title('Scatter Plot for Fatalities (Road Crashes) vs Speed Limit')
    savefig(ht_img5, dpi=100)

    
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
        ht_data2[row[ht_var2]] += fatalities
        if '-9' not in row[ht_var3]:
            ht_data3[int(row[ht_var3])] += fatalities
        ht_data4[row[ht_var4]] += fatalities
        if '-9' not in row[ht_var5]:
            ht_data5[int(row[ht_var5])] += fatalities
    csvfile.close()
    print 'Content-Type: text/html\n'        
    
    # generate visualisations
    vs_year(ht_data1)
    vs_day(ht_data2)
    vs_hour(ht_data3)
    vs_state(ht_data4)
    vs_speed_limit(ht_data5)
    
    print html_start
    print page
    print html_end
        
# main function which controls all the action
main()
​

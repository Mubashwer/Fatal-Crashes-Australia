# --- fix to IVLE's problem in using matplotlib
import os, sys
os.dup2(2, 3)
stderr = os.fdopen(2, 'a')
stderr.close()
# ---
import matplotlib
matplotlib.use('Agg')
from pylab import *
# --- fix to IVLE's problem in using matplotlib
os.dup2(3, 2)
sys.__stderr__ = sys.stderr = os.fdopen(2, 'a')
# ---
from numpy import *
import csv
from collections import defaultdict
import calendar

# tools for debugging
import cgitb
cgitb.enable()
sys.stderr = sys.stdout

# cgi script which generats the form for pivot table report editor
form_script = 'form.py'

# data source url
source_url = 'https://www.bitre.gov.au/statistics/safety/fatal_road_crash_database.aspx'

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

# hypothesis titles
ht_header1 = '''The total number of fatalities due to road crashes decreased in the last 5 years.'''
ht_header2 = '''There were more fatalities due to road crashes towards the end of the weeks.'''
ht_header3 = '''There were more fatalities due to road crashes in every hour between 1pm-6pm than any other hour.'''
ht_header4 = '''There were more fatalities due to road crashes in New South Wales than any other state.'''
ht_header5 = '''There were very few fatalities due to crashes in roads with speed limit lower than 50 km/h.'''

# hypothesis explanations
ht_xpln1 = '''From this graph it can be observed that fatalities have decreased in the last 5 years. This could be due to \
stricter road laws being enforced in the country or higher levels of safety requirements in newer car models. '''
ht_xpln2 = '''It can be observed from the bar chart that the number of fatalities is relatively larger in Fridays, Satudays \
and Sundays, but it is not larger by a great margin. One of the possible reasons may be a lot of family travelling at the end \
of weekdays.'''
ht_xpln3 = '''It can be observed from the bar chart that the road is most dangerous during the hours of 1-6pm. This could be \
a result of higher levels of traffic that occur during these hours from people moving from their work to home.'''
ht_xpln4 = '''The bar chart shows that the number of fatalities in New South Wales is larger than all other states by a great \
margin. The obvious reason is that it is the most populated state. States with relatively low population had very \
few fatalities such as Northern Territory, Australian Capital Territory and Tasmania. A chart with Number of Fatalities \
per capita would give a more accurate relationship between variables.'''
ht_xpln5 = '''The scatter plot chart gives indication as to the relationship between higher speed limit zones and the number of \
fatalities. The graph shows a clear difference in the level of fatalities in roads with speed limit higher than 40km/h and those \
below 40km/h showing that roads with higher speed limit are more prone to accidents.'''

# independent variable for data dictionaries for each hypothesis
ht_var1 = 'Year'
ht_var2 = 'Dayweek'
ht_var3 = 'Hour'
ht_var4 = 'State'
ht_var5 = 'Speed Limit'

dep_var = 'Number of Fatalities'  # depedendent variable

# file names for each visualisation
ht_img1 = 'vs_year.png'
ht_img2 = 'vs_day.png'
ht_img3 = 'vs_hour.png'
ht_img4 = 'vs_state.png'
ht_img5 = 'vs_speed_limit.png'

page = '''
<h1>When and where in Australia have fatal crashes occured the most in the last 5 years?</h1>
<div class="hypothesis" id="hypothesis1">
    <h2 class="header">{}</h2>
    <div class="visual"><img src="{}" alt="image1" width="500" height="375" /></div>
    <p class="explain">{}</p>
</div>
<div class="hypothesis">
    <h2 class="header" id="header2">{}</h2>
    <div class="visual"><img src="{}" alt="image2" width="500" height="375" /></div>
    <p class="explain">{}</p>
</div>
<div class="hypothesis" id="hypothesis3">
    <h2 class="header">{}</h2>
    <div class="visual"><img src="{}" alt="image2" width="500" height="375" /></div>
    <p class="explain">{}</p>
</div>
<div class="hypothesis">
    <h2 class="header">{}</h2>
    <div class="visual"><img src="{}" alt="image2" width="500" height="375" /></div>
    <p class="explain">{}</p>
</div>
<div class="hypothesis">
    <h2 class="header">{}</h2>
    <div class="visual"><img src="{}" alt="image2" width="500" height="375" /></div>
    <p class="explain">{}</p>
</div>
'''.format(ht_header1, ht_img1, ht_xpln1, ht_header2, ht_img2, ht_xpln2,
           ht_header3, ht_img3, ht_xpln3, ht_header4, ht_img4, ht_xpln4,
           ht_header5, ht_img5, ht_xpln5)

html_links = '''
<span class="links"><a href="{}">Data source</a></span>
<span class="links"><a href="{}">Pivot Table Builder</a></span>'''.format(source_url, form_script)

w3_valid = '''<a href="http://validator.w3.org/check?uri=referer"><img\
 src="http://www.w3.org/Icons/valid-xhtml10" alt="Valid XHTML 1.0 Strict" height="31" width="88" /></a>'''


def vs_year(data):
    '''Line Graph for Fatalities vs Time'''
    clf()
    y = [item[1] for item in sorted(data.items(), key=lambda x: x[0])]
    plot(y, color='purple')
    xticks(arange(5), sorted(data.keys()), rotation=30)
    grid(True)
    xlabel('Time (Year)')
    ylabel(dep_var)
    title('Line Graph for Fatalities vs Time')
    savefig(ht_img1, dpi=100)


def vs_day(data):
    '''Bar Chart for Fatalities (Road Crashes) vs Days in Week'''
    clf()
    bars = arange(len(data))
    labels = list(calendar.day_name)
    heights = []
    for day in labels:
        heights += [data[day]]
    bar(bars, heights, align='center', facecolor='grey')
    xticks(bars, labels, rotation=30)
    ylim([0,max(heights)+50])
    grid(True)
    xlabel('Days in Week')
    ylabel(dep_var)
    title('Bar Chart for Fatalities (Road Crashes) vs Days in Week')
    savefig(ht_img2, dpi=100)
    
    
def vs_hour(data):
    '''Histogram for Fatalities (Road Crashes) vs Time'''
    clf()
    hist(data.keys(), bins=arange(0, 25),
         weights=data.values(), facecolor='green')
    xticks(arange(0, 24, 2), ['{:02d}'.format(hour)
           for hour in arange(0, 24, 2)])
    grid(True)
    xlabel('Time (Hours in a Day)')
    ylabel(dep_var)
    title('Histogram for Fatalities (Road Crashes) vs Time')
    text = '*Time for 1 fatal crash is unknown which is not taken into account.'
    plt.figtext(0, 0, text)    
    savefig(ht_img3, dpi=100)


def vs_state(data):
    '''Bar Chart for Fatalities (Road Crashes) vs State'''
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


def vs_speed_limit(data):
    '''Scatter Plot for Fatalities (Road Crashes) vs Speed Limit'''
    clf()
    scatter(data.keys(), data.values(), s=data.values(), color='red')
    yticks(arange(0, 3000, 500))
    grid(True)
    xlabel('Speed Limit (km/h)')
    ylabel(dep_var)
    title('Scatter Plot for Fatalities (Road Crashes) vs Speed Limit')
    text = '*Speed limits for 46 fatal crashes are unknown which are not taken into account.'
    plt.figtext(0, 0, text)    
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
    print w3_valid
    print html_links
    print html_end

# main function which controls all the action
main()

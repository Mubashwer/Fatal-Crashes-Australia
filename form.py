import cgi

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
<link rel="stylesheet" href="form.css" type="text/css" media="screen" charset="utf-8" />
</head>
<body><div class="container"> '''

html_end = '''
</div></body></html>'''

html_form ='''
<h2 class="header">Fatal Crashes in Australia (2009-2013)</h2>
<form action="pivot_table.py" method="post">
    <fieldset id="pivot_table">
            <legend>Pivot Table Report Editor</legend>
            <div class="field_select">
                <label for="rows">Rows:</label>
                <select class="menu menu_row" name="rows" id="rows">
                    <option value="State">State</option>
                    <option value="Month" selected="selected">Month</option>
                    <option value="Year">Year</option>
                    <option value="Dayweek">Day of week</option>
                    <option value="Hour">Hour</option>
                    <option value="Crash Type">Crash Type</option>
                    <option value="Bus Involvement">Bus Involvement</option>
                    <option value="Rigid Truck Involvement">Rigid Truck Involvement</option>
                    <option value="Articulated Truck Involvement ">Articulated Truck Involvement</option>
                    <option value="Number of Fatalities">Number of Fatalities</option>
                    <option value="Speed Limit">Speed Limit</option>
                    <option value="Day">Day of month</option>
                </select>
                <input type="radio" name="order_row" id="row_ascending" value="0" checked="checked"/><span>Ascending</span>    
                <input type="radio" name="order_row" id="row_descending" value="1" /><span>Descending</span>
            </div>
            <div class="field_select">
                <label for="columns">Columns:</label>
                <select class="menu menu_col" name="columns" id="columns">
                <option value="State">State</option>
                <option value="Month">Month</option>
                <option value="Year">Year</option>
                <option value="Dayweek">Day of week</option>
                <option value="Hour">Hour</option>
                <option value="Crash Type">Crash Type</option>
                <option value="Bus Involvement">Bus Involvement</option>
                <option value="Rigid Truck Involvement">Rigid Truck Involvement</option>
                <option value="Articulated Truck Involvement ">Articulated Truck Involvement</option>
                <option value="Number of Fatalities">Number of Fatalities</option>
                <option value="Speed Limit">Speed Limit</option>
                <option value="Day">Day of month</option>
                </select>
                <input type="radio" name="order_col" id="col_ascending" value="0" checked="checked"/><span>Ascending</span>    
                <input type="radio" name="order_col" id="col_descending" value="1" /><span>Descending</span>
            </div>    
            <div class="field_select">
                <label for="values">Values:</label>
                <select class="menu menu_values" name="values" id="values">
                <option value="Number of Fatalities">Number of Fatalities</option>
                <option value="Speed Limit">Speed Limit</option>                
                <option value="Day">Day of Month</option>                
                <option value="Month">Month</option>
                <option value="Year">Year</option>
                </select>
            </div>
            <div class="field_select">
                <label for="values">Formula:</label>
                <select class="menu menu_formula" name="formula" id="formula">
                <option value="SUM">SUM</option>
                <option value="COUNT">COUNT</option>                
                <option value="AVERAGE">AVERAGE</option>                
                <option value="MAX">MAX</option>
                <option value="MIN">MIN</option>
                </select>
            </div>
            <div class="field_select">
                <label for="filter">Filter:</label>
                <select class="menu menu_filter" name="filter" id="filter">
                <option value="blank"></option>
                <option value="Crash Type">Crash Type</option>
                <option value="Bus Involvement">Bus Involvement</option>
                <option value="Speed Limit">Speed Limit</option>
                <option value="Dayweek">Day of week</option>
                <option value="Hour">Hour</option>
                <option value="Min">Minute</option>
                <option value="Rigid Truck Involvement">Rigid Truck Involvement</option>
                <option value="Time">Time</option>
                <option value="Crash ID">Crash ID</option>
                <option value="Month">Month</option>
                <option value="Number of Fatalities">Number of Fatalities</option>
                <option value="State">State</option>
                <option value="Articulated Truck Involvement ">Articulated Truck Involvement </option>
                <option value="Year">Year</option>
                <option value="Date">Date</option>
                <option value="Day">Day of month</option>
                </select>
            </div>
            <div class="field_select">
                <label for="filter_value">Filter value:</label>
                <input name="filter_value" id="filter_value" type="text" />
            </div>
    </fieldset>
    <div id="buttons" class="button_select">
        <input type="reset" value="Reset" />
        <input type="submit" value="Submit" />
    </div>
</form>'''

html_links = '''
<span class="data_source"><a href="https://www.bitre.gov.au/statistics/safety/fatal_road_crash_database.aspx">Data source</a></span>'''

def main():
    print 'Content-Type: text/html\n'
    print html_start
    print html_form
    print html_links
    print html_end

main()

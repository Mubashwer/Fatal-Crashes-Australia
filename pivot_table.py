import cgi
import csv
from collections import defaultdict



# some debugging tools, for gracefully displaying error messages
import sys
import cgitb
cgitb.enable()
sys.stderr = sys.stdout

# html chunks
html_start = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Fatal Crashes in Australia</title>
<link rel="stylesheet" href="css/pivot_table.css" type="text/css" media="screen" charset="utf-8" />
</head>
<body><div class="container"> '''

html_end = '''
</div></body></html>'''

def give_value(values, formula):
    """It performs given formula on values."""
    if formula == "COUNT":
        return len(values)
    if formula == "SUM":
        return sum(values)
    if formula == "AVERAGE":
        return float(sum(values))/len(values)
    if formula == "MIN":
        if not values:
            return 0
        else:
            return min(values)
    if formula == "MAX":
        if not values:
            return 0
        else:
            return max(values)

def give_header(val, header_var):
    """It converts the header values of months and hours to
    appropriate format."""
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",
              "Aug", "Sep", "Oct", "Nov", "Dec"]
    
    if header_var == 'Month':
        return months[int(val)-1]
    if header_var == 'Hour':
        return "{}-{:02d}".format(val, int(val)+1)
    return val

def split(value, minimum, maximum):
    value = round(value)
    interval_len = round((abs(maximum) - abs(minimum))/5)+1
    td_classes = ['vlow', 'low', 'medium', 'high', 'vhigh']
    color = 0
    current_value = minimum
    while(current_value <= value - interval_len):
        current_value += interval_len
        color+= 1
    return td_classes[color]

def error_response():
    error = '<div class="error"><br /><span class="error_text">Filtered data is empty</span><br/>'
    error +='<a href="form.py">Go back</a></div>'
    return error
        

     

def gen_table(values, formula, col_headers, col_var, col_totals,  row_var, row_totals, row_sort_key, row_reverse,all_total, minimum, maximum):
    table = '<table class="pivot_table">\n'
    table += "<tr><th>&nbsp;</th>"
    
    for header in col_headers:
        table += '<th>{}</th>'.format(give_header(header, col_var))
        
    table += "<th>Grand Total</th></tr>\n"
    row_index = 0
    for row_key in sorted(values.keys(), key=row_sort_key, reverse=row_reverse):
        table += '<tr><th>{}</th>'.format(give_header(row_key, row_var))
        for col_key in col_headers:
            if col_key in values[row_key]:
                value = values[row_key][col_key]
                table += '<td class="{}">{}</td>'.format(split(value, minimum, maximum),value)
            else:
                table += '<td class="blank">&nbsp;</td>'
            
            
        table += '<td class="total">{}</td>'.format(row_totals[row_index])
        table += "</tr>\n"
        row_index += 1                                                 
    
    table += '<tr><th>Grand Total</th>'
    for total in col_totals:
        table += '<td class="total">{}</td>'.format(total)     
    table += '<td class="total">{}</td></tr>\n</table>\n'.format(all_total)
    return table

def to_int(value):
    try:
        output = int(value)
    except ValueError:
        output = 1
    return output

def redirect_form():
    url = "http://students.informatics.unimelb.edu.au/~mskh/foi/mywork/Project3/form.py"    
    print 'Content-Type: text/html\n'
    print html_start
    print '<a href="form.py">Fatal Crashes in Australia (2009-2013)</a></div>'
    print html_end
    sys.exit()
    

    
def main():
    # load data from csv file
    csvfile = open("fatal_crashes_10_years.csv")
    data = csv.DictReader(csvfile)
    form = cgi.FieldStorage()
    if len(form) == 0:
        redirect_form()
    var_list = ['Crash Type', 'Bus Involvement', 'Speed Limit', 'Dayweek', 'Hour',
            'Min', 'Rigid Truck Involvement', 'Time', 'Crash ID', 'Month',
            'Number of Fatalities', 'State', 'Articulated Truck Involvement ',
            'Year', 'Date', 'Day']
     
    dayweek_keys = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']    
    
                                      
    row_var = form.getfirst('rows')
    row_sort_key = None
    row_reverse = int(form.getfirst('order_row'))                                  
    col_var = form.getfirst('columns')
    col_sort_key = None
    col_reverse = int(form.getfirst('order_col'))                                   
    
    if row_var == 'Day' or row_var == 'Month' or row_var == 'Speed Limit' or row_var == "Number of Fatalities":
        row_sort_key = int
    if col_var == 'Day' or col_var == 'Month' or col_var == 'Speed Limit' or col_var == "Number of Fatalities":
        col_sort_key = int
    if row_var == 'Dayweek':
        row_sort_key = dayweek_keys.index
    if col_var == 'Dayweek':
        col_sort_key = dayweek_keys.index
    
    val_var = form.getfirst('values')
    formula = form.getfirst('formula')                            
    filter_var = form.getfirst('filter')
    filter_val = form.getfirst('filter_value')
    values = {}
    values_list = []
    col_headers = []
    
    valid_filter = True
    if(filter_var == 'blank' or filter_val == None or filter_val[0] == ' '):
        valid_filter = False                                
                                
                                
    for row in data:
        row_key = row[row_var]
        if row_key[-1] == ' ': row_key = row_key[:-1]                         
        col_key = row[col_var]
        if col_key[-1] == ' ': col_key = col_key[:-1]                         
        # vaues which are empty, unknown or residue from filtering
        # are ignored
        if len(row_key) == 0 or len(col_key) == 0: continue 
        if '-9' in row_key or '-9' in col_key: continue
        if 'N/A' in row_key or 'N/A' in col_key: continue                        
        if valid_filter and filter_val != row[filter_var]: continue
        if col_key not in col_headers:
            col_headers += [col_key]

        if row_key not in values:
            values[row_key] = defaultdict(int)
        if col_key not in values[row_key]:
            values[row_key][col_key] = []
        values[row_key][col_key] += [to_int(row[val_var])]
        
    csvfile.close()
    
    col_headers = sorted(col_headers, key=col_sort_key, reverse=col_reverse)
    row_totals = []
    col_totals = []
    all_values = []
    for row in values:
        row_totals.append([])
        
    for col in col_headers:
        col_totals.append([])

    row_index = 0
    for row_key in sorted(values.keys(), key=row_sort_key, reverse=row_reverse):
        col_index = 0
        for col_key in col_headers:
            if col_key in values[row_key]:
                col_totals[col_index].extend(values[row_key][col_key])
            col_index += 1
            
        for col_key in values[row_key]:
            value = give_value(values[row_key][col_key], formula)
            row_totals[row_index].extend(values[row_key][col_key])
            values_list += [value]
            all_values.extend(values[row_key][col_key])
            values[row_key][col_key] = value
            
        row_index += 1
        
    for row_index in range(len(row_totals)):
        row_totals[row_index] = give_value(row_totals[row_index], formula)
        
    for col_index in range(len(col_totals)):
        col_totals[col_index] = give_value(col_totals[col_index], formula)
    
    all_total = give_value(all_values, formula)

    
    print 'Content-Type: text/html\n'
    print html_start

    if values_list:
        minimum = min(values_list)
        maximum = max(values_list) 
        print gen_table(values, formula, col_headers, col_var, col_totals, row_var, row_totals, row_sort_key, row_reverse, all_total, minimum, maximum)
    else:
        print error_response()

    print html_end

main()

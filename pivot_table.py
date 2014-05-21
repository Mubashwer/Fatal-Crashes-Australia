import cgi
import csv
from collections import defaultdict
from math import ceil
import calendar


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

# texts to be printed when some data are ignored
unknown_time = '<div class="unknown">*Time for 1 fatal crash is unknown which is not taken into account.</div>\n'
unknown_sl = '<div class="unknown">*Speed limits for 46 fatal crashes are unknown which are not taken into account.</div>\n'

# csv file location
csv_loc = "fatal_crashes_5_years.csv"

# cgi script which generates the form
form_script = 'form.py'
go_back = '<a href="{}">Go back</a>'.format(form_script)


def apply_formula(values, formula):
    """It performs given formula on values."""
    if formula == "COUNT":
        return len(values)
    if formula == "SUM":
        return sum(values)
    if formula == "AVERAGE":
        return float(sum(values)) / len(values)
    if formula == "MIN":
        if not values:  # if values is an empty list
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
    if header_var == 'Month':
        return calendar.month_abbr[int(val)]
    if header_var == 'Hour':
        return "{}-{:02d}".format(val, int(val) + 1)
    return val


def give_class(value, minimum, maximum):
    """It takes a value and the minimum and maximum of all values and returns
    the appropriate td class."""
    value = round(value)
    # interval length is the length of each interval after
    # the gap between minimum and maximum is divided by 5 and rounded up
    interval_len = ceil((abs(maximum) - abs(minimum) + 1) / float(5))
    td_classes = ['vlow', 'low', 'medium', 'high', 'vhigh']

    color = - 1  # it is the index for td_classes
    current_value = minimum

    # color value increases by 1 as the minimum value is being
    # incremented by the interval length until it's the given value
    while(current_value <= value):
        current_value += interval_len
        color += 1

    # for safety, so that index is not out of bound
    if color < 0:
        color = 0
    if color > 4:
        color = 4

    return td_classes[color]


def error_response():
    """User is being told that the table is empty and is offered to go back to the form."""
    error = '<div class="error"><br /><span class="error_text">Filtered data is empty</span><br/>'
    error += go_back + '</div>'
    return error


def gen_table(values, col_headers, col_var, col_totals, row_var, row_totals,
              row_sort_key, row_reverse, all_total, minimum, maximum):
    """It generates the pivot table"""
    table = '<table class="pivot_table">\n'
    table += "<tr><th>&nbsp;</th>"

    for header in col_headers:  # html code for column headers is generated
        table += '<th>{}</th>'.format(give_header(header, col_var))
    table += "<th>Grand Total</th></tr>\n"

    # html code for each row is generated in ascending or descending order
    for row_key in sorted(values.keys(), key=row_sort_key, reverse=row_reverse):
        table += '<tr><th>{}</th>'.format(give_header(row_key, row_var))
        for col_key in col_headers:
            if col_key in values[row_key]:
                value = values[row_key][col_key]
                table += '<td class="{}">{}</td>'.format(
                    give_class(value, minimum, maximum), value)
            else:
                table += '<td class="blank">&nbsp;</td>'
        # html code for row totals is generated
        table += '<td class="total">{}</td>'.format(row_totals[row_key])
        table += "</tr>\n"

    # html code for column grand totals and total of grand totals are generated
    table += '<tr><th>Grand Total</th>'
    for col_key in col_headers:
        table += '<td class="total">{}</td>'.format(col_totals[col_key])
    table += '<td class="total">{}</td></tr>\n</table>\n'.format(all_total)
    return table


def to_int(value):
    """Safer conversion to integer. It converts invalid literals to 1."""
    try:
        output = int(value)
    except ValueError:
        output = 1
    return output


def redirect_form():
    """User is offered to go to the form instead of this script."""
    print 'Content-Type: text/html\n'
    print html_start
    print '<a href="{}">Fatal Crashes in Australia (2009-2013)</a></div>'.format(form_script)
    print html_end
    sys.exit()

# main function which controls all the action


def main():
    # load data from csv file
    csvfile = open(csv_loc)
    data = csv.DictReader(csvfile)

    # load data from submitted form
    form = cgi.FieldStorage()
    if len(form) == 0:
        # if this script is run, user is to be redirected to the form
        redirect_form()

    val_var = form.getfirst('values')  # selected value variable
    formula = form.getfirst('formula')  # selected formula
    filter_var = form.getfirst('filter')  # selected filter variable
    filter_val = form.getfirst('filter_value')  # selected filter value
    row_var = form.getfirst('rows')  # selected row variable
    row_sort_key = None
    # 0 for ascending and 1 for descending
    row_reverse = int(form.getfirst('order_row'))
    col_var = form.getfirst('columns')
    col_sort_key = None
    col_reverse = int(form.getfirst('order_col'))  # variable for column

    dayweek_key = list(calendar.day_name).index  # sort key for days in week

    # sort keys are int for numerical data, dayweek_keys for days of week and
    # none for others
    if row_var in ['Day', 'Month', 'Speed Limit', 'Number of Fatalities']:
        row_sort_key = int
    if col_var in ['Day', 'Month', 'Speed Limit', 'Number of Fatalities']:
        col_sort_key = int
    if row_var == 'Dayweek':
        row_sort_key = dayweek_key
    if col_var == 'Dayweek':
        col_sort_key = dayweek_key

    # data containers for storing values for pivot table
    # dictionary of dictionary with list as value e.g values['Sunday']['VIC']
    # = [1,2,1,1...1,2]
    values = {}
    col_headers = []  # list of column headers

    # col_totals is a dictionary with column key/header being its key and a list of all values in that column
    # being its value. row_totals is similar. all_values is a list of all
    # values.
    col_totals = {}
    row_totals = {}
    all_values = []

    # if filter variable was not selected or filter value was not given, then
    # data is not to be filtered
    filter_given = True
    if(filter_var == 'blank' or filter_val == None or filter_val[0] == ' '):
        filter_given = False

    for row in data:
        # trailing space is ignored for row and col keys
        row_key = row[row_var]
        if row_key[-1] == ' ':
            row_key = row_key[:-1]
        col_key = row[col_var]
        if col_key[-1] == ' ':
            col_key = col_key[:-1]

        # values which are empty, unknown or residue from filtering
        # are ignored
        if len(row_key) == 0 or len(col_key) == 0:
            continue
        if '-9' in row_key or '-9' in col_key:
            continue
        if filter_given and filter_val != row[filter_var]:
            continue

        # col headers are put in a list and col_totals is initialized
        if col_key not in col_headers:
            col_headers += [col_key]
            col_totals[col_key] = []

        # row_totals and values are initialized
        if row_key not in values:
            values[row_key] = defaultdict(int)
            row_totals[row_key] = []
        if col_key not in values[row_key]:
            values[row_key][col_key] = []

        # values are assigned to containers
        value = to_int(row[val_var])
        values[row_key][col_key] += [value]
        row_totals[row_key] += [value]
        col_totals[col_key] += [value]
        all_values += [value]
    csvfile.close()

    # column headers are sorted with appropriate key
    col_headers = sorted(col_headers, key=col_sort_key, reverse=col_reverse)

    # the given formula is performed on all the organized data
    # all_total is the grand total of all the values by applying formula
    all_total = apply_formula(all_values, formula)
    # all_values is now to be a list with all values after formula is applied
    all_values = []
    # formula is being applied to all the values and totals
    for col_key in col_headers:
        col_totals[col_key] = apply_formula(col_totals[col_key], formula)
    for row_key in values:
        row_totals[row_key] = apply_formula(row_totals[row_key], formula)
        for col_key in values[row_key]:
            value = apply_formula(values[row_key][col_key], formula)
            values[row_key][col_key] = value
            all_values += [value]

    print 'Content-Type: text/html\n'
    print html_start

    if all_values:
        # min and max of values are needed for colouring table cells
        minimum = min(all_values)
        maximum = max(all_values)
        # table is generated and printed
        print gen_table(values, col_headers, col_var, col_totals, row_var,
                        row_totals, row_sort_key, row_reverse, all_total,
                        minimum, maximum)
        if col_var == 'Hour' or row_var == 'Hour':
            print unknown_time
        if col_var == 'Speed Limit' or row_var == 'Speed Limit' or\
           val_var == 'Speed Limit':
            print unknown_sl
        print go_back
    else:
        # if table is empty (usually due to invalid filter value)
        # then the response is printed
        print error_response()

    print html_end


main()

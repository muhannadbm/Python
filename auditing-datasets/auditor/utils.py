"""
Module providing utility functions for this project.

These functions are general purpose utilities used by other modules in this project.
Some of these functions were exercises in early course modules and should be copied
over into this file.

The preconditions for many of these functions are quite messy.  While this makes writing 
the functions simpler (because the preconditions ensure we have less to worry about), 
enforcing these preconditions can be quite hard. That is why it is not necessary to 
enforce any of the preconditions in this module.

Author: Muhannad Bani Almarje
Date: 03/16/2021
"""
import csv
import json
import os
from dateutil.parser import parse
import datetime
import pytz

def read_csv(filename):
    """
    Returns the contents read from the CSV file filename.
    
    This function reads the contents of the file filename and returns the contents as
    a 2-dimensional list. Each element of the list is a row, with the first row being
    the header. Cells in each row are all interpreted as strings; it is up to the 
    programmer to interpret this data, since CSV files contain no type information.
    
    Parameter filename: The file to read
    Precondition: filename is a string, referring to a file that exists, and that file 
    is a valid CSV file
    """
                        # Implement this function
    file = open(filename,'r')
    csvob = csv.reader(file)
    list=[]
    for row in csvob:
        list.append(row)
    file.close()
    return list


def write_csv(data,filename):
    """
    Writes the given data out as a CSV file filename.
    
    To be a proper CSV file, data must be a 2-dimensional list with the first row 
    containing only strings.  All other rows may be any Python value.  Dates are
    converted using ISO formatting. All other objects are converted to their string
    representation.
    
    Parameter data: The Python value to encode as a CSV file
    Precondition: data is a  2-dimensional list of strings
    
    Parameter filename: The file to read
    Precondition: filename is a string representing a path to a file with extension
    .csv or .CSV.  The file may or may not exist.
    """
                        # Implement this function
    file = open(os.path.join(filename),'w')
    wrapper = csv.writer(file)
    for row in data:
        wrapper.writerow(row)
    file.close()


def read_json(filename):
    """
    Returns the contents read from the JSON file filename.
    
    This function reads the contents of the file filename, and will use the json module
    to covert these contents in to a Python data value.  This value will either be a
    a dictionary or a list. 
    
    Parameter filename: The file to read
    Precondition: filename is a string, referring to a file that exists, and that file 
    is a valid JSON file
    """
                       # Implement this function
    text = {}
    file = open(os.path.join(filename))
    text = file.read()
    text1=json.loads(text)
    file.close()
    return text1


def str_to_time(timestamp,tz=None):
    """
    Returns the datetime object for the given timestamp (or None if stamp is invalid)
    
    This function should just use the parse function in dateutil.parser to
    convert the timestamp to a datetime object.  If it is not a valid date (so
    the parser crashes), this function should return None.
    
    If the timestamp has a timezone, then it should keep that timezone even if
    the value for tz is not None.  Otherwise, if timestamp has no timezone and 
    tz if not None, this this function will assign that timezone to the datetime 
    object. 
    
    The value for tz can either be a string or a time OFFSET. If it is a string, 
    it will be the name of a timezone, and it should localize the timestamp. If 
    it is an offset, that offset should be assigned to the datetime object.
    
    Parameter timestamp: The time stamp to convert
    Precondition: timestamp is a string
    
    Parameter tz: The timezone to use (OPTIONAL)
    Precondition: tz is either None, a string naming a valid time zone,
    or a time zone OFFSET.
    """
    # HINT: Use the code from the previous exercise and update the timezone
    # Use localize if timezone is a string; otherwise replace the timezone if not None

    try:
        d = parse(timestamp)
        if d.tzinfo != None:
            newdate = d
        else:
            if type(tz) == datetime.datetime:
                tz1 = tz.tzinfo
                newdate=d.replace(tzinfo=tz1)
                return newdate
            if type(tz) != str:
                newdate=d.replace(tzinfo=tz)
            else:
                tz1=pytz.timezone(tz)
                newdate=tz1.localize(d)
        return newdate
    except:
        return None


def daytime(time,daycycle):
    """
    Returns true if the time takes place during the day.
    
    A time is during the day if it is after sunrise but before sunset, as
    indicated by the daycycle dicitionary.
    
    A daycycle dictionary has keys for several years (as int).  The value for
    each year is also a dictionary, taking strings of the form 'mm-dd'.  The
    value for that key is a THIRD dictionary, with two keys "sunrise" and
    "sunset".  The value for each of those two keys is a string in 24-hour
    time format.
    
    For example, here is what part of a daycycle dictionary might look like:
    
        "2015": {
            "01-01": {
                "sunrise": "07:35",
                "sunset":  "16:44"
            },
            "01-02": {
                "sunrise": "07:36",
                "sunset":  "16:45"
            },
            ...
        }
    
    In addition, the daycycle dictionary has a key 'timezone' that expresses the
    timezone as a string. This function uses that timezone when constructing
    datetime objects from this set.  If the time parameter does not have a timezone,
    we assume that it is in the same timezone as the daycycle dictionary
    
    Parameter time: The time to check
    Precondition: time is a datetime object
    
    Parameter daycycle: The daycycle dictionary
    Precondition: daycycle is a valid daycycle dictionary, as described above
    """
    # HINT: Use the code from the previous exercise to get sunset AND sunrise
    # Add a timezone to time if one is missing (the one from the daycycle)
    d = time
    month = d.month
    day = d.day
    year = d.year
    if d.month < 10:
        month = '0'+ str(d.month)
    if d.day < 10:
        day = '0' + str(d.day)
    try:
        sunset = daycycle[str(d.year)][str(month)+'-'+str(day)]['sunset']
        sunrise = daycycle[str(d.year)][str(month)+'-'+str(day)]['sunrise']
    except:
        return None
    timezonedefault = daycycle['timezone']
    
    isosunset = str(d.year)+'-'+ str(month)+'-'+ str(day) +'T'+str(sunset)
    isosunrise = str(d.year)+'-'+ str(month)+'-'+ str(day) +'T'+str(sunrise)
    
    sunsettemp = str_to_time(isosunset,timezonedefault)
    sunrisetemp = str_to_time(isosunrise,timezonedefault)
    
    if d.tzinfo != None:
        newdate = d
        
    else:
        tz1=pytz.timezone(timezonedefault)
        newdate=tz1.localize(d)
    
    
    if newdate > sunrisetemp and newdate < sunsettemp:
        return True
    
    else:
        return False




def get_for_id(id,table):
    """
    Returns (a copy of) a row of the table with the given id.
    
    Table is a two-dimensional list where the first element of each row is an identifier
    (string).  This function searches table for the row with the matching identifier and
    returns a COPY of that row. If there is no match, this function returns None.
    
    This function is useful for extract rows from a table of pilots, a table of instructors,
    or even a table of planes.
    
    Parameter id: The id of the student or instructor
    Precondition: id is a string
    
    Parameter table: The 2-dimensional table of data
    Precondition: table is a non-empty 2-dimension list of strings
    """
                        # Implement this function
    row=len(table)
    col=len(table[0])
    result=[]
    for r in range(row):
        for c in range(col):
            if table[r][c] == id:
                result = table[r]
    if len(result)!=0:
        return result
    else:
        return None
            


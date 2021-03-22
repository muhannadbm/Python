"""
Module for currency exchange

This module provides several string parsing functions to implement a simple
currency exchange routine using an online currency service. The primary function
in this module is exchange().

Author: MUHANNAD BANI ALMARJE
Date:   12/25/2020
"""
import introcs
APIKEY='XocnUEf3r0KYrlJ1XUhhRnuTKwOO7ZQH1WAAwCUJsjUe'

def before_space(s):
    """
    Returns the substring of s up to, but not including, the first space.

    Example: before_space('Hello World') returns 'Hello'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """
    assert type(s)==str,'S is not a String'
    assert introcs.find_str(s,' ')!=-1,'S has no spaces'
    space= introcs.find_str(s,' ')
    string=s[:space]
    return string


def after_space(s):
    """
    Returns the substring of s after the first space

    Example: after_space('Hello World') returns 'World'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """
    assert type(s)==str,'S is not a String'
    assert introcs.find_str(s,' ')!=-1,'S has no spaces'
    space= introcs.find_str(s,' ')
    string=s[space+1:]
    return string


def first_inside_quotes(s):
    """
    Returns the first substring of s between two (double) quote characters

    Note that the double quotes must be part of the string.  So "Hello World" is a 
    precondition violation, since there are no double quotes inside the string.

    Example: first_inside_quotes('A "B C" D') returns 'B C'
    Example: first_inside_quotes('A "B C" D "E F" G') returns 'B C', because it only 
    picks the first such substring.

    Parameter s: a string to search
    Precondition: s is a string with at least two (double) quote characters inside
    """
    assert type(s)==str,'S is not a String'
    assert introcs.find_str(s,'"')!=-1
    firstquote= introcs.find_str(s,'"')
    secondquote=introcs.find_str(s,'"',firstquote+1)
    assert secondquote!=-1
    string=s[firstquote+1:secondquote]
    return string


def get_src(json):
    """
    Returns the src value in the response to a currency query.

    Given a JSON string provided by the web service, this function returns the string
    inside string quotes (") immediately following the substring '"src"'. For example,
    if the json is
    
    '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns '2 United States Dollars' (not '"2 United States Dollars"'). 
    On the other hand if the json is 
    
    '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns the empty string.

    The web server does NOT specify the number of spaces after the colons. The JSON
    
    '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'
    
    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'
    assert type(json)==str
    src= introcs.find_str(json,'"src"')
    substr=json[src+6:]
    result=first_inside_quotes(substr)
    return result
    
    
def get_dst(json):
    """
    Returns the dst value in the response to a currency query.

    Given a JSON string provided by the web service, this function returns the string
    inside string quotes (") immediately following the substring '"dst"'. For example,
    if the json is
    
    '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns '1.772814 Euros' (not '"1.772814 Euros"'). On the other
    hand if the json is 
    
    '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns the empty string.

    The web server does NOT specify the number of spaces after the colons. The JSON
    
    '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'
    
    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    assert type(json)==str
    src= introcs.find_str(json,'"dst"')
    substr=json[src+6:]
    result=first_inside_quotes(substr)
    return result
    
    
def has_error(json):
    """
    Returns True if the response to a currency query encountered an error.

    Given a JSON string provided by the web service, this function returns True if the
    query failed and there is an error message. For example, if the json is
    
    '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns True (It does NOT return the error message 
    'Source currency code is invalid'). On the other hand if the json is 
    
    '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns False.

    The web server does NOT specify the number of spaces after the colons. The JSON
    
    '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'
    
    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    assert type(json)==str
    error= introcs.find_str(json,'"error"')
    substr=json[error+8:]
    result=first_inside_quotes(substr)
    result2=bool(result)
    return result2


def service_response(src,dst,amt):
    """
    Returns a JSON string that is a response to a currency query.

    A currency query converts amt money in currency src to the currency dst. The response 
    should be a string of the form

    '{"success": true, "src": "<src-amount>", dst: "<dst-amount>", error: ""}'

    where the values src-amount and dst-amount contain the value and name for the src 
    and dst currencies, respectively. If the query is invalid, both src-amount and 
    dst-amount will be empty, and the error message will not be empty.

    There may or may not be spaces after the colon.  To test this function, you should
    chose specific examples from your web browser.

    Parameter src: the currency on hand
    Precondition src is a nonempty string with only letters

    Parameter dst: the currency to convert to
    Precondition dst is a nonempty string with only letters

    Parameter amt: amount of currency to convert
    Precondition amt is a float or int
    """
    assert type(src)==str
    assert type(dst)==str
    assert introcs.find_str(src,' ')==-1
    assert introcs.find_str(dst,' ')==-1

    amt=str(amt)
    q = 'https://ecpyfac.ecornell.com/python/currency/fixed?src='+\
    src+'&dst='+dst+'&amt='+amt+'&key=XocnUEf3r0KYrlJ1XUhhRnuTKwOO7ZQH1WAAwCUJsjUe'
    result= introcs.urlread(q)
    return result


def iscurrency(currency):
    """
    Returns True if currency is a valid (3 letter code for a) currency.

    It returns False otherwise.

    Parameter currency: the currency code to verify
    Precondition: currency is a nonempty string with only letters
    """
    assert len(currency)!=0
    assert introcs.isalpha(currency)==True
    result = not(has_error(service_response(currency,currency,2.5)))
    return result


def exchange(src,dst,amt):
    """
    Returns the amount of currency received in the given exchange.

    In this exchange, the user is changing amt money in currency src to the currency 
    dst. The value returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter src: the currency on hand
    Precondition src is a string for a valid currency code

    Parameter dst: the currency to convert to
    Precondition dst is a string for a valid currency code

    Parameter amt: amount of currency to convert
    Precondition amt is a float or int
    """
    assert iscurrency(src)==True
    assert iscurrency(dst)==True
    result=service_response(src,dst,amt)
    resp=get_dst(result)
    space=introcs.find_str(resp,' ')
    result=resp[:space]
    return float(result)
    
    
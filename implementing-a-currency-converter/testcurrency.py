"""
Unit tests for module currency

When run as a script, this module invokes several procedures that test
the various functions in the module currency.

Author: MUHANNAD BANI ALMARJE
Date:   12/25/2020
"""

import introcs
import currency


def test_before_space():
    """Test procedure for before_space"""
    print('Testing before_space')
    introcs.assert_equals('hello',currency.before_space('hello world'))
    introcs.assert_equals('hello',currency.before_space('hello  world'))
    introcs.assert_equals('',currency.before_space(' helloworld'))
    introcs.assert_equals('hello',currency.before_space('hello world '))
    
    
def test_after_space():
    """Test procedure for after_space"""
    introcs.assert_equals('world',currency.after_space('hello world'))
    introcs.assert_equals(' world',currency.after_space('hello  world'))
    introcs.assert_equals('',currency.after_space('helloworld '))
    introcs.assert_equals('world ',currency.after_space('hello world '))    
    print('Testing after_space')
    
    
def test_first_inside_quotes():
    """Test procedure for first_inside_quotes"""
    introcs.assert_equals('hello world',currency.first_inside_quotes('"hello world"'))
    introcs.assert_equals(' helloworld',currency.first_inside_quotes('" '+
    'helloworld" hope you are doing fine'))
    introcs.assert_equals(' helloworld',currency.first_inside_quotes('" helloworld"'+
    ' hope you are doing "fine"'))
    introcs.assert_equals('',currency.first_inside_quotes('""'))  
    print('Testing first_inside_quotes')
    
    
def test_get_src():
    """Test procedure for get_src"""
    print('Testing get_src')
    introcs.assert_equals('2'+
    ' United States Dollars',currency.get_src('{"success": true,'+\
    ' "src": "2 United States Dollars","dst": "1.772814 Euros", "error": ""}'))
    introcs.assert_equals('',currency.get_src('{"success":false,'+\
    '"src":"","dst":"","error":"Source currency code is invalid."}'))
    introcs.assert_equals('United States Dollars',currency.get_src('{"success": true,'+\
    ' "src":"United States Dollars", "dst": "1.772814 Euros", "error": ""}'))
    introcs.assert_equals('',currency.get_src('{"success":false,'+\
    '"src": "","dst":"","error":"Source currency code is invalid."}'))

    
def test_get_dst():
    """Test procedure for get_dst"""
    print('Testing get_dst')
    introcs.assert_equals('1.772814 Euros',currency.get_dst('{"success": true,'+\
    ' "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'))
    introcs.assert_equals('',currency.get_dst('{"success": false,'+\
    ' "src": "", "dst": "", "error": "Source currency code is invalid."}'))
    introcs.assert_equals('',currency.get_dst('{"success": false,'+\
    ' "src": "", "dst":"", "error": "Source currency code is invalid."}'))
    introcs.assert_equals('1.772814 Euros',currency.get_dst('{"success": true,'+\
    ' "src":"2 United States Dollars", "dst":"1.772814 Euros", "error": ""}'))
    
    
def test_has_error():
    """Test procedure for has_error"""
    print('Testing has_error')
    introcs.assert_false(currency.has_error('{"success": true,'+\
    ' "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'))
    introcs.assert_true(currency.has_error('{"success": false,'+\
    ' "src": "", "dst": "", "error":"Source currency code is invalid."}'))
    introcs.assert_true(currency.has_error('{"success": false,'+\
    ' "src": "", "dst":"", "error": "Source currency code is invalid."}'))
    introcs.assert_false(currency.has_error('{"success": true,'+\
    ' "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'))
    
    
def test_service_response():
    """Test procedure for service_response"""
    print('Testing service_response')
    introcs.assert_equals('{"success": true,'+\
    ' "src": "2.5 United States Dollars", "dst": "2.2160175 Euros", "error": ""}',currency.service_response('USD','EUR',2.5))
    introcs.assert_equals('{"success": false,'+\
    ' "src": "", "dst": "", "error": "The rate for currency SSD is not present."}',currency.service_response('SSD','EUR',2.5))
    introcs.assert_equals('{"success": true,'+\
    ' "src": "-2.5 United States Dollars", "dst": "-2.2160175 Euros", "error": ""}',currency.service_response('USD','EUR',-2.5))
    introcs.assert_equals('{"success": false,'+\
    ' "src": "", "dst": "", "error": "The rate for currency URS is not present."}',currency.service_response('USD','URS',2.5))
    
    
def test_iscurrency():
    """Test procedure for iscurrency"""
    print('Testing iscurrency')
    introcs.assert_true(currency.iscurrency('USD'))
    introcs.assert_false(currency.iscurrency('us'))
    
    
def test_exchange():
    """Test procedure for exchange"""
    print('Testing exchange')
    introcs.assert_floats_equal(2.2160175,currency.exchange('USD','EUR',2.5))
    introcs.assert_floats_equal(-2.2160175,currency.exchange('USD','EUR',-2.5))
    
    
test_first_inside_quotes()
test_after_space()
test_first_inside_quotes()
test_get_src()
test_get_dst()
test_has_error()
test_service_response()
test_iscurrency()
test_exchange()
print("All tests completed successfully.")
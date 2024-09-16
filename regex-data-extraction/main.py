#!/usr/bin/python3


import re

def test_regex(pattern, test_strings, expected_results):
    regex = re.compile(pattern)
    for test_string, expected in zip(test_strings, expected_results):
        match = regex.search(test_string)
        result = bool(match)
        print(f"Testing '{test_string}': {'Passed' if result == expected else 'Failed'}")

# Email addresses
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
email_tests = ['user@example.com', 'firstname.lastname@company.co.uk', 'invalid-email@', 'another.invalid.email']
email_expected = [True, True, False, False]
print("Testing Email Addresses:")
test_regex(email_pattern, email_tests, email_expected)

# URLs
url_pattern = r'^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$'
url_tests = ['https://www.example.com', 'http://subdomain.example.org/page', 'invalid-url', 'ftp://invalid.com']
url_expected = [True, True, False, False]
print("\nTesting URLs:")
test_regex(url_pattern, url_tests, url_expected)

# Phone numbers
phone_pattern = r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$'
phone_tests = ['(123) 456-7890', '123-456-7890', '123.456.7890', '12345', '+1 (123) 456-7890']
phone_expected = [True, True, True, False, True]
print("\nTesting Phone Numbers:")
test_regex(phone_pattern, phone_tests, phone_expected)

# Credit card numbers
cc_pattern = r'^(\d{4}[-\s]?){4}$'
cc_tests = ['1234 5678 9012 3456', '1234-5678-9012-3456', '12345678', '1234 5678 9012 3456 7890']
cc_expected = [True, True, False, False]
print("\nTesting Credit Card Numbers:")
test_regex(cc_pattern, cc_tests, cc_expected)

# Time
time_pattern = r'^(([01]?[0-9]|2[0-3]):[0-5][0-9])|((1[0-2]|0?[1-9]):([0-5][0-9]) ([AaPp][Mm]))$'
time_tests = ['14:30', '2:30 PM', '25:00', '7:60 AM', '9:30 am']
time_expected = [True, True, False, False, True]
print("\nTesting Time Formats:")
test_regex(time_pattern, time_tests, time_expected)

# HTML tags
html_pattern = r'<[^>]+>'
html_tests = ['<p>', '<div class="example">', '<img src="image.jpg" alt="description">', 'Not a tag', '<>']
html_expected = [True, True, True, False, False]
print("\nTesting HTML Tags:")
test_regex(html_pattern, html_tests, html_expected)

# Hashtags
hashtag_pattern = r'#[a-zA-Z0-9_]+'
hashtag_tests = ['#example', '#ThisIsAHashtag', '#123', 'Not a #hashtag', '#']
hashtag_expected = [True, True, True, True, False]
print("\nTesting Hashtags:")
test_regex(hashtag_pattern, hashtag_tests, hashtag_expected)

# Currency amounts
currency_pattern = r'^\$\d{1,3}(,\d{3})*(\.\d{2})?$'
currency_tests = ['$19.99', '$1,234.56', '$1000', '19.99', '$1,23.45']
currency_expected = [True, True, True, False, False]
print("\nTesting Currency Amounts:")
test_regex(currency_pattern, currency_tests, currency_expected)

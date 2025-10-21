#Strong password

import re

test_list = [
    'Hello, world.',   #test invalid pass
    ',,,,,rrttgg.....banana....rrr',   #test invalid pass
    'Tr4sf6fsf42324s',   #test valid pass
    'PASSW0RD',   #test invalid
    'passw0rd',   #test invalid
    'pAssw0rd',   #test valid
]

#Get string out after applying regex
def regex_apply(pattern,string_value):
    regex_pattern = re.compile(pattern)
    find_pattern = regex_pattern.search(string_value)
    if(find_pattern is not None):
        return find_pattern.group()

#Get all strings from a string
def regex_findall(pattern,string_value):
    regex_pattern = re.compile(pattern)
    find_pattern = regex_pattern.findall(string_value)
    if(find_pattern is not None):
        return find_pattern
        
#Strip the string from the passed characters
def strip(full_string, characters):
    if(characters == ''):
        str_list = regex_findall(r'\S+',full_string)
        return ''.join(str_list)
    else:
        str_list = regex_findall(r'[^' + characters + r']+',full_string)
        return ''.join(str_list)
        
for item in test_list:
    print(strip(item, ',.grt'))

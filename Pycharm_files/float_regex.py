def float_regex():
    import re
    floatRegex = re.compile(r'^[+|-]?\d+[.]?(\d+)?$')
    regex = input('Enter a numeric value: ')
    regex = regex.strip().replace(',', '')
    mo = floatRegex.search(regex)
    while mo == None:
        regex = input('Enter only numeric values: ')
        regex = regex.strip().replace(',', '')
        mo = floatRegex.search(regex)
    if regex.isnumeric() is True:
        regex = int(regex)
    else:
        regex = float(regex)
        regex = round(regex)
    return regex

#Example of how to use

# print('How many gallons of gas did you use? ')
# gas_used = float_regex()
# print(gas_used)



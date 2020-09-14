import re
def float_regex(message):
    floatRegex = re.compile(r'^[+|-]?\d+[.]?\d+?$')
    regex = input(message)
    regex = regex.strip().replace(',', '')
    mo = floatRegex.search(regex)
    while mo == None:
        regex = input('Enter only numeric values: ').strip().replace(',', '')
        mo = floatRegex.search(regex)
    if regex.isnumeric():
        regex = int(regex)
    else:
        regex = round(float(regex), 2)
    return regex

#Example of how to use

gas_used = float_regex(message="How many gallons of gas did you use?:")
print(f'{gas_used} gallons')
#
#
#
# # import re
# #
# # word = re.compile(r'\Acat', re.I)
# # result = bool(word.search('Concatinate'))
# # print(result)


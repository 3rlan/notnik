import re
def sumnumber(string):
    if len(string) > 13:
        return False
    sum = re.findall('\+996\d{9}', string)
    return len(sum)>0



print(sumnumber('+996708114750'))
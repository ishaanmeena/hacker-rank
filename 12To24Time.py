def timeConversion(n):
    s = n.split(':')
    if('PM' in s[-1] and s[0] != '12'):
        s[0] = str(int(s[0]) + 12)
        s[-1] = s[-1].strip('PM')
        time = ':'.join(s)
    elif('PM' in s[-1] and s[0] == '12'):
        s[-1] = s[-1].strip('PM')
        time = ':'.join(s)
    elif('AM' in s[-1] and s[0] != '12'):
        s[-1] = s[-1].strip('AM')
        time = ':'.join(s)
    elif('AM' in s[-1] and s[0] == '12'):
        s[0] = '00'
        s[-1] = s[-1].strip('AM')
        time = ':'.join(s)
    return(time)

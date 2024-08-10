def tenlines(datain):
    count = 0
    frontdiv = 'div'
    enddiv = '/div'
    line = frontdiv
   
    if x < 9:
        line += datain
        count += 1
    else:
        line += datain
        line += enddiv
        count = 0
    return (line) #"ten lines of data"

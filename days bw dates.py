# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
#


def nextDay(year, month,day):
    if(day < 30 ):
        if(month <= 12):
            day = day + 1
    elif(day >= 30):
        day = 1
        if(month < 12):
            month = month + 1
        elif(month >= 12):
            month = 1
            year = year + 1
    return year,month,day

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    dy = (year2 - year1) * 12 * 30
    dm = (month2 - month1) * 30
    d = day2 - day1
    dt = dy + dm + d
    return dt

def test():
    test_cases = [((2012,9,30,2012,10,30),30),
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print ("Test with data:" , args, "failed")
        else:
            print ("Test case passed!")

test()

try:
    from timeDuration import *
except ImportError:
    print("Unable to import 'timeDuration'. Create an Empty Python file with that name.")

def getTotalEventSpan(eventName):
    f= open('Events.txt', 'r')
    lines = f.readlines()
    weeks=0
    days=0
    hours=0
    for single in lines:
        if (single[4:11] == eventName):
            if(single[20] == 'w'):
                weeks += int(single[18:20])*int(single[31])
            elif(single[20] == 'd'):
                days += int(single[18:20])*int(single[31])
            elif(single[20] == 'h'):
                hours += int(single[18:20])*int(single[31])
    days += int(hours / 24)
    weeks += int(days / 7 )
    days %= 7
    hours %= 24

    return TimeSpan(weeks,days,hours)


def rankEventsBySpan(*args):
    ll = []
    for event in args:
        totaltime = getTotalEventSpan(event)
        ll.append(totaltime.getTotalHours())
    ll.sort()
    returnll = []
    for time in ll:
        for event in args:
            total = getTotalEventSpan(event)
            if(time == total.getTotalHours()):
                returnll.append(event)
    final = []
    for i in range(1, len(returnll)+1):
        final.append(returnll[-i])

    return final
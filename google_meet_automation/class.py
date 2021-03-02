import sys
from Todays_Classes import *
from time import sleep
from random_quotes import random_quote
from print_timetable import *
from join_meet import *

inp = sys.argv[1].upper()

try:
    inp2 = sys.argv[2].upper()
    if inp2 == 'JM':
        join_meet(classesnick[inp])

    if inp2 == 'OM':
        if inp in classesnick:
            open_link(classes[inp])
    if inp2 != 'OM' and inp2 != 'JM':
        print('\n' + '\t' + 'INVALID COMMAND')
        print('\n' + '\t' + 'Try class -h for help menu')

except IndexError or AttributeError:
    if inp in classes:
        open_link(classes[inp])



if inp == 'TODAY' or inp == '-T':
    print()
    random_quote()
    classes_today()
elif inp == 'HELP' or inp == '-H':
    help()

elif inp == "TIME TABLE" or inp == '-TT':
    print_timetable()

elif inp == 'AUTOMATE' or inp == '-A':
    subs = find_classes()
    c = 0
    while True:
        if c == 1:
            break
        time = datetime.now().time()
        time = str(time).split(':')
        for i in subs:
            if time[0] == i[0:2] and time[1] == i[3:5]:
                print('Opened ' + i[20:] + ' link')
                open_link(classes[i[20:]])
                if i == subs[-1]:
                    c = 1
                if i == subs[-1] and i == 1:
                    time.sleep(6600)
                if i == 2:
                    time.sleep(3600)
                else:
                    time.sleep(3000)
                break

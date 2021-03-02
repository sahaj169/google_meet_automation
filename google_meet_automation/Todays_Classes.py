import calendar
from datetime import datetime
import webbrowser
from class_details import *


def findDay():
    date_and_time = datetime.now()
    date = str(date_and_time.day) + ' ' + str(date_and_time.month) + ' ' + str(date_and_time.year)
    date = datetime.strptime(date, '%d %m %Y').weekday()
    day = calendar.day_name[date]
    return day.lower()


def find_classes():
    subs = []
    day = findDay()
    classes = subjects[day]
    n = len(classes)
    if classes:
        if day == 'wednesday' or day == 'tuesday':
            timings = ['09:00 am - 10:40 am','10:50 am - 12:30 pm','12:30 pm - 13:20 pm','13:20 pm - 14:10 pm','14:10 pm - 15:50 pm']
            for i in range(n):
                formatted = f'{timings[i]} {classes[i]}'
                subs.append(formatted)
        if day == 'monday' or day == 'thursday' or day == 'friday':
            timings = ['09:00 am - 10:40 am', '10:50 am - 11:40 am','11:40 am - 12:30 pm','12:30 pm - 13:20 pm', '13:20 pm - 14:10 pm', '14:10 pm - 15:50 pm']
            for i in range(n):
                formatted = f'{timings[i]} {classes[i]}'
                subs.append(formatted)
    else:
        print("There is NO classes today")
    return subs


def classes_today():
    subs = find_classes()
    for i in subs:
        time = datetime.now().time()
        time = str(time).split(":")
        if time[0] == i[0:2] and time[1] <= i[3:5]:
            print('\n' + '\t' + i, ' <== Present Session')
        elif time[0] == i[11:13] and time[1] <= i[14:16]:
            print('\n' + '\t' + i, ' <== Present Session')
        else:
            print('\n' + '\t' + i)

def help():
    print('\n' + '\t' + 'class [-a or automate] To automate')
    print('\n' + '\t' + 'class [-h or help] To see this menu')
    print('\n' + '\t' + 'class [subject_name] To open subject_name\'s link')
    print('\n' + '\t' + 'class [subject_name] [om] To open subject_name\'s link')
    print('\n' + '\t' + 'class [subject_name] [jm] join subject_name\'s link')
    print('\n' + '\t' + 'class [-t or today] To see today\'s classes')
    print('\n' + '\t' + 'class [-tt or time table] To see full week time table')


def open_link(url):
    webbrowser.open(url)
    print("Opened the requested link")

subject = {
    'tuesday': ['PQT', 'APP', 'LUNCH BREAK', 'OS', 'SEPMLAB'],
    'wednesday': ['CCT', 'SEPM', 'LUNCH BREAK', 'DAA', 'APPLAB'],
    'thursday': ['OS', 'PQT', 'DAA', 'LUNCH BREAK', 'SE', 'OSLAB'],
    'friday': ['DAA', 'SE', 'ES', 'LUNCH BREAK', 'SEPM', 'DAALAB'],
    'monday': ['CC', 'OS', 'APP', 'LUNCH BREAK', 'PQT', 'CCLAB'],
    'saturday': ['DAY OFF'],
    'sunday': ['DAY OFF']
}
def Dclasses(day):
    subs = []
    classes = subject[day]
    n = len(classes)
    if classes:
        if day == 'tuesday' or day == 'wednesday':
            timings = ['09:00 am - 10:40 am', '10:50 am - 12:30 pm',
                        '12:30 pm - 13:20 pm', '13:20 pm - 14:10 pm', '14:10 pm - 15:50 pm']
            for j in range(n):
                formatted = f'{timings[j]} => {classes[j]}'
                subs.append(formatted)
        if day == 'monday' or day == 'friday' or day == 'thursday':
            timings = ['09:00 am - 10:40 am', '10:50 am - 11:40 am', '11:40 am - 12:30 pm',
                        '12:30 pm - 13:20 pm', '13:20 pm - 14:10 pm', '14:10 pm - 15:50 pm']
            for j in range(n):
                formatted = f'{timings[j]} => {classes[j]}'
                subs.append(formatted)
            
    return subs

def print_timetable():
    dayorders = ['monday','tuesday','wednesday','thursday','friday']
    for i in range(5):
        subs = Dclasses(dayorders[i])
        print(f"{dayorders[i]} ==> {subs}")


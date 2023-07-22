handle = open("mbox-short.txt")
hoursdict = dict()

for line in handle:
    if line.startswith("From "):
        linesofhours = line.strip().split()
        time = linesofhours[5].split(":")
        hour = time[0]
        hoursdict[hour] = hoursdict.get(hour, 0)+1

for hour,count in sorted(hoursdict.items()):
    print(hour, count)
import re
handle = open("mbox-short.txt")
numberList = list()

for line in handle:
    line = line.strip()
    stuff = re.findall("^X-DSPAM-Confidence: ([0-9.]+)",line)
    if len(stuff) !=1 : continue
    num = float(stuff[0])
    numberList.append(num)
print("Maximum:", max(numberList))
import re
handle = open("mbox-short.txt")
for line in handle:
    line = line.strip()
    # if re.search("^From: ",line):
    #     #print(line)
    # if re.search("^X-.*:",line):
    #     print(line)
    # if re.search("^X-.\S+",line):
    # #\S = match any non-whitespace character
    # #+ = one or more times
    #     print(line)
    # numbers = re.findall("[0-9]+",line)
    # print(numbers)
    #email = re.findall("^From (\S+@\S+)",line)
    # print(email)
    mail2ndPart = re.findall('@([^ ]*)', line)
    mail2ndPart = re.findall('^From .*@([^ ]*)',line)
    print(mail2ndPart)
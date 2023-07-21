handle = open("mbox-short.txt")
numerofSenders = dict()
emailList= list()
for line in handle:
    if line.startswith("From "):
        line = line.strip().split()
        emailList.append(line[1])
for email in emailList:
    numerofSenders[email] = numerofSenders.get(email,0)+1

listofmail = dict()
for line in handle:
    if line.startswith("From "):
        words = line.strip().split()
        for mail in words:
            print(mail)

print(listofmail)
bigCount = None
bigWord = None
for word,count in numerofSenders.items():
    if bigCount is None or count>bigCount:
        bigWord = word
        bigCount = count
print(bigWord, bigCount)


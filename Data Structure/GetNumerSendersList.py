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
    wordslist = line.strip().split()
    for word in wordslist:
        listofmail[word] = listofmail.get(word,0)+1

print(listofmail)

largest = -1
theword = None
for key,value in listofmail.items():
    if value> largest:
        largest = value
        theword = key
print(theword, largest)

bigCount = None
bigWord = None
for word,count in numerofSenders.items():
    if bigCount is None or count>bigCount:
        bigWord = word
        bigCount = count
print(bigWord, bigCount)


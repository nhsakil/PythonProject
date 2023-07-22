#Dictionery = Assosiative Array_in Perl/PHP, Properties, Map, HashMap in Java, Property Bag in C#/.net
#To stroe value with tag or metadata

purse = dict()
purse["Money"] =12
purse["Candy"] = 43
purse["Tissues"] = 54
purse["Candy"] = 43
purse["Candy"] = purse["Candy"]*3

#Count dictionery Values

listofPeople =dict()
names = ["Jhon", "Mark", "Wood", "Jhon", "Sam", "Mark", "Wood", "Ducket", "Sam", "Mark", "Wood"]
for name in names:
    if name not in listofPeople:
        listofPeople[name] = 1
    else:
        listofPeople[name] = listofPeople[name] + 1
print(listofPeople)

for name in names:
    listofPeople[name] = listofPeople.get(name,0) + 1
print(listofPeople)

#Count words from file

#wordsfile = input("Please Provide the file name\n")
lineofwords  = open("romeo.txt")
listofWords = dict()
for word in lineofwords:
    words = word.strip().split()
    for word in words:
        listofWords[word] = listofWords.get(word,0)+1
print(listofWords)

#for key in listofWords:
    #print(listofWords[key])
#print(list(listofWords))
#print(listofWords.keys())
#print(listofWords.values())
#print(listofWords.items())

for word,values in listofWords.items():
    print(word,values)



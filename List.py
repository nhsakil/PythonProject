#concatinate list
number_people = ["Joseph", "Jhon", "Shahd"]
salary_people = [45000, 43000, 4333.3, 43030, 99433]
salary_of_people = number_people+ salary_people
print(salary_of_people)

"Joseph" in number_people

455 not in salary_people

#Slicing list

print(salary_people[1:3])
print(number_people[:2])

#Building the list
staff = list()
staff.append(input("Please type your name\n"))
staff.append(34)
staff.append("Smith")
print(staff)
print(len(staff))
print(min(salary_people))
print(sum(salary_people))

#Building list

numlist = list()
while True:
    inputNumber = input("Please enter the value: \n")
    if inputNumber == "done": break
    value = float(inputNumber)
    numlist.append(value)
average = sum(numlist)/len(numlist)
print("Average:", average)


#split the list

new_people = "The new memory will kill the virus"

staff1 = new_people.split()
print(staff1)


#Split list from file

fileopen = open("mbox-short.txt")
for line in fileopen:
    line = line.strip()
    if not line.startswith("From "): continue
    words = line.split()
    #print(words[2])
    emails = words[1]
    firstHalf = emails.split("@")
    print(firstHalf[0])
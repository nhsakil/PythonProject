import re
handle = open("regex_sum_1843127.txt")
numberList = list()

for line in handle:
    line = line.strip()
    numbers = re.findall(r'\d+',line)
    if not numbers: continue
    for num in numbers:
        numberList.append(int(num))
print(sum(numberList))
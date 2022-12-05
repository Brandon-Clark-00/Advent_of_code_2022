


file = open("1.txt")
lines = file.readlines()
# print(file.read())
current = 0
first = 0
second = 0
third = 0
for line in lines:
    if line == "" or line == "\n":
        if current > first:
            third = second
            second = first
            first =current
            current = 0
        elif current > second:
            third = second
            second = current
            current = 0
        elif current > third:
            third = current
            current = 0
        else:
            current = 0
            
    else:
        current = current+ int(line)

print("The elf carrying the most calories is carrying " + str(first) + " calories and the top three elfs have " + str(first) + ", " + str(second) +", " + str(third) +" for a total of " + str(first+second+third) )

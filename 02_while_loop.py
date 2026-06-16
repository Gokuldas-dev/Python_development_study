# this is a sample program to print even numbers from 1 to 10 using while loop
i = 1
count2 = 0
while i <= 10:
    if i % 2 == 0:
        print(i)
        count2 += 1
    i += 1
print("Total even numbers printed:", count2)  

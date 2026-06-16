# This is the second problem  that i am working 
print ("-----------------------------------------")
age = int(input("Enter your age  : "))
print (f"You given your age as :" ,{age})
print ("Processing .....")
if  age >18 :
	print ("Good news ! Your are eligible to vote in election ")
elif age  < 18 :
	print ("Your are not eligible to vote in election as you are under the age criteria")
elif age == 18 :
	print ("Congratulations! You are eligible to vote in election now  ")
else :
	print ("Ehh ! Something went wrong , Are you sure u entered the age correctly")

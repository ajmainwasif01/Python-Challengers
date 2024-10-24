a = int(input("Enter first speed:"))
b = int(input("Enter second speed:"))
c = int(input("Enter third speed:"))

average = (a+b+c) / 3
print(average)
if average > a and average > b and average > c :
     print("Average speed is higher than A,B,C")
elif average > a and average > b:
     print("Average speed is higher than A,B")
elif average > a and average > c:
     print("Average speed is higher than A,C")    
elif average > b and average > c:
     print("Average speed is higher than B,C") 
elif average > a:
     print("Average speed is higher than A")
elif average > b:
     print("Average speed is higher than B")
elif average > c:
     print("Average speed is higher than C")     
## 1 Program to Print a Sequene of Numbers
for i in range(1,10):
    print(i)

## 2 Program to print a Name using a Funtion
def nam(name):
    print("Hello", name)

nam("Abdul Qadoos")

## 3 Program to take 3 Numbers from the User and Print the Largest Number
n1 = int(input("Enter First No: "))
n2 = int(input("Enter Seond No: "))
n3 = int(input("Enter Third No: "))

if n1>n2 and n1>n3:
    print("The Largest No is", n1)
elif n2>n1 and n2>n3:
    print("The Largest No is", n2)
else:
    print("The Largest No is", n3)

## 4 Program to take 3 Numbers from the User and Print Seond Largest
n1 = int(input("Enter First No: "))
n2 = int(input("Enter Seond No: "))
n3 = int(input("Enter Third No: "))

if n1>n2 and n1>n3:
    Largest=n1
elif n2>n1 and n2>n3:
    Largest = n2
else:
    Largest=n3

if Largest==n1:
    if n2>n3:
        second=n2
    else:
        second=n3

elif Largest==n2:
    if n1>n3:
        second=n1
    else:
        second=n3

else:
    if n1>n2:
        second=n1
    else:
        second=n2

print("Second Largest Number is",second)

## 5 
name ="Hello Abdul";
age = 15;
print(name, age)
list= [1,2,3,4,5]
print(list)
list.append(6)
print(list)
list.insert(0,0)
print(list)
list.remove(6)
print(list)
list.reverse()
print(list)
print(len(list))
print(min(list))
print(max(list))

a = 2e2
b = 2E2
c = 2e3
print(a)
print(b)
print(c)
print(type(a))
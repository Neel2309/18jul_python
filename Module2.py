# 1)
number=int(input("Enter the value of number:"))

if number is 0:
    print("The number is zero")
elif number>=0:
    print("The number is positive")
elif number<0:
    print("The number is negative")


# 2)
n=int(input("Enter the value of n:"))
fact = 1

for i in range(1, n+1):
	fact = fact * i
        
print("The factorial of n is : ", end="")
print(fact)


# 3)
n=int(input("Enter the value of n:"))

n1=0
n2=1
print(n1)
print(n2)

for i in range(2,n+1):
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3


# 4)Memory management in Python involves a private heap containing all Python objects and data structures.The management of this private heap is ensured internally by the Python memory manager.


# 5)The continue statement in Python returns the control to the beginning of the while loop. The continue statement rejects all the remaining statements in the current iteration of the loop and moves the control back to the top of the loop.


# 6)
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))

a,b=b,a

print("A=",a)
print("B=",b)


# 7)
num=int(input("Enter a number:"))

if num%2==0:
    print("It is an even number")

else:
    print("It is an odd number")

l=input("Enter the letter:")

if l in ("a,e,i,o,u"):
    print("The letter is vowel")
else:
    print("The letter is not vowel")


# 8)
n1=int(input("Enter the value of n1:"))
n2=int(input("Enter the value of n2:"))
n3=int(input("Enter the value of n3:"))
sum=n1+n2+n3

if n1==n2 or n1==n3 or n2==n3:
    print("The sum is 0")
else:
    print("SUM",sum)


# 9)
num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))

if num1==num2 or num1+num2==5 or num1-num2==5:
    print("True")
else:
    print("Fasle")


# 10)
n=int(input("Enter the number:"))
sum=(n*(n+1))/2
print("The sum of first", n ,"integers is :",sum)


# 11)
mystr=input('Enter the string:')
print(len(mystr))


# 12)
mystr="Hello and Welcome to tops!"
print(mystr.count("a"))


# 13)
# negative index


# 14) Negative Indexing is used to in Python to begin slicing from the end of the string.


# 15)
mystr="Hello and Welcome to tops!"
print(mystr.count("and"))


# 16)
mystr="Hello and Welcome to tops!"
print(mystr.count("Hello"))
print(mystr.count("end"))
print(mystr.count("Welcome"))
print(mystr.count("to"))
print(mystr.count("tops"))


# 17)
mystr1="Hello and"
mystr2="Welcome to tops!"

print(mystr1.replace('H','W'),end=" ")
print(mystr2.replace('W','H'))


# 18)
mystr=input("Enter the string:")

if len(mystr)<3:
    print("Unchanged",mystr)
   
if mystr.endswith('ing'):
    mystr+='ly'

elif len(mystr)>=3:
    mystr+='ing'

print(mystr)


# 19)
str=input("Enter a string:")
print(str)

not_index=str.index('not')
poor_index=str.index('poor')

if not_index!=-1 and poor_index!=-1 and not_index<poor_index:
    print(str[:not_index]+"good"+str[poor_index+4:])
else:
    print(str)


# 20)
mystr=input('Enter a string:')

length=len(mystr)

print("Length=",length)

if length%4==0:
    print("Reverse of String is",mystr[::-1])

else:
    print("The string is not reversed")


# 21)
mystr="Welcome"
if mystr.index<2:
    print([])
else:
    print(mystr[:2]+mystr[-2:])


# 22)
mystr=("Welcome to the python programing")

split=mystr.split()
split.insert(1,"Students")
final=" ".join(split)
print(final)

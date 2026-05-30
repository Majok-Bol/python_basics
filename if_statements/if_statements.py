a=34
b=45
c=56
#if...else statement
if a>b:
    print(f"{a} is greater than {b}")
else:
    print(f"{b} is greater than {a}")

#45 is greater than 34
#elif statement
if a>b:
    print(f"{a} is greater than {b}")
elif b>a:
    print(f"{b} is greater than {a}")
else:
    print(f"{c} is greater than {a} and {b}")
#45 is greater than 34

#shorthand for if...else statement
print(f"{a} is greater than {b}") if a>b else  print(f"{b} is greater than {a}")
#45 is greater than 34

#and logical statement
if b>a and c>a:
    print(f"{b} and {c} are greater than {a}")
#45 and 56 are greater than 34

#or logical statement
if a>b or c>b:
    print(f"{c} is greater than {b}")

#56 is greater than 45
#reverse result
if not a>b:
    print(f"{b} is greater than {a}")
#45 is greater than 34

#nested if
x=11
if x>10:
    print("Above ten")
    if x>20:
        print("and also above 20")
    else:
        print("but not above 20")
#Above ten
#but not above 20


#pass statement
#if statements cant be empty
#use pass if if statement is not having content
a=200
b=33
if a>b:
    pass # condition is true...nothing is executed
else:
    print(f"{a} is greater than {b}")
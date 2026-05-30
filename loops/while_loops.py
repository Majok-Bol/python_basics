#while loops
num1=0
print("\nCounting numbers from 0 to 20")
while num1<=20:
    #prints numbers 0-20
    print(num1)
    #increment counter by 1 for after each iteration
    num1+=1



#break statement
#break loop even if the while condition true
#stop at number 10
num1=0
print("\nCounting numbers from 0 and stopping at 10")
while num1<=20:
    #prints numbers 0-20
    print(num1)
    #stop at number 10
    if num1==10:
        break
    #increment counter by 1 for after each iteration
    num1+=1


    
#continue keyword
#used to skip current iteration
#counting numbers from 0 to 20 but skip number 3
num1=0
print("\nCounting numbers from 0 to 20 but skip number 3")
while num1<=20:
 
    #skip number 3
    if num1==3:
        #increment counter by 1 for after each iteration
        num1+=1
        continue
       #prints numbers 0-20
    print(num1)
    num1+=1
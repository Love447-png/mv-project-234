'''Name = input("enter your name")
pront("Welcome!",Name)'''
'''arr = [10,20,30,40]
def LShift(arr,n):
    L=len(arr)
    for x in range(0,n):
        y = arr[0]
        for i in range(0,L-1):
           arr[i]=arr[i+1]
        arr[L-1] = y
    print(arr)
LShift(arr,2)'''
'''principal = int(input("enter principal value"))
rate = float(input("enter rate of interest"))
time = int(input("enter the time period"))
Simple_interest = principal*rate*time/100
Amount = principal + Simple_interest
print("Simple interest:",Simple_interest)
print("Amount:",Amount)'''
'''radius = float(input("enter the radius: "))
area = 3.14*radius**2
print("Area of circle: ",area)'''
'''result = 0
num1 = float(input("enter the first no."))
num2 = float(input("enter the second no."))
op = input("enter the operator(+,-,*,/): ")
if op == '+':
    result = num1+num2
elif op == '-':
    result = num1-num2
elif op == '*':
    result = num1*num2        
elif op == '/':
    if num2 == 0:
        print("please! enter no. rather than 0")
    else:
        result = num1/num2    
else:    
    print("Enter the operator(+,-*,/): ")
print("The result is : ",result)'''

'''basic = int(input("enter your basic salary: ")) 
savings = int(input("enter your total savings: "))
if basic <= 250000:
    tax = 0
elif basic <= 500000:
    if savings > 150000:
        savings = 150000     
    tot_income = basic-savings-250000
    tax = tot_income*0.05
elif basic <= 1000000:
    if savings > 150000:
        savings = 150000
    tot_income_5salab = 500000-savings-250000
    tot_income_20salab = basic-500000
    tax = tot_income_5salab*0.05 + tot_income_20salab*0.02
else:
    if savings > 150000:
        savings = 150000
    tot_income_5salab  = 500000-savings-250000
    tot_income_30salab = basic-1000000                
    tax = tot_income_5salab*0.05 + tot_income_30salab*0.03 + 100000

print("Total income tax to be paid = ",tax)'''

'''for i in range(2,100):
    print("Cube of the no: ",i,end ='',)
    print("is",i**3)'''

'''*num1 = int(input("enter the first no." ))
num2 = int(input("enter the second no." ))
product = 0
i = num1
while i > 0 :
    i = i - 1
    product = product + num2
print("product of ",num1,'and',num2,'is',product)'''    

'''val = int(input("enter the value: "))
fact = 1
i = 1
while i<=val:
    fact = fact*i
    i = i+1
print("The factorial of ",val,'is', fact)'''    

'''f = open("myfile.txt",'+w')
writer = f.write("what will me my plan for 4years of my college")
print("I will crack GSoc")
f.close()'''

f = open("myfile.txt",'+r')
reader = f.readline()
f.close()





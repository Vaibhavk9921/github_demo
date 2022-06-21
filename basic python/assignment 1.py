#1.Write a Program to calculate Gross Salary.
#In this program we will take basic salary as an input and on the basis of following calculations we calculate gross salary.
# da is 20% of basic salary
#• hra is 40% of basic salary
#• Gross Salary = basic salary + da + hra
x=int(input("basic salary"))

da=x*0.2
print(da)
hra=x*0.4
print(hra)
gs=x+da+hra
print(gs)
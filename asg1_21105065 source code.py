#question 1
print('question 1')
#taking input from the user 
number_1=int(input('enter first number-'))
number_2=int(input('enter second number-'))
number_3=int(input('enter third number-'))

#using the formula to calculate the average
average=(number_1+number_2+number_3)/3

#printing the average
print(average)

#--------------------------------

#question 2
print('question 2')
# taking input from user
gross_income=float(input('enter your gross income-'))
num_dependents=int(input('enter number of dependents-'))

#rounding of gross income to nearest penny
gross_income=round(gross_income,2)

standard_deduction=10000
dependent_deduction=3000
             
#formula to find the taxable amount
taxable_income = gross_income-standard_deduction-(dependent_deduction*num_dependents)
tax=(taxable_income*20)/100

if tax<0:
    print('your income tax is 0$')
else:
    print('tax=',tax)


#----------------------------------
#question 3
print('question 3')
#taking input from user
SID=int(input('SID-'))
Name=input('Name-')
Gender=input('gender(F,M or U)-')
Course_name=input('course name-')
CGPA=float(input('CGPA-'))

#storing all the data in a list
student=[SID,Name,Gender,Course_name,CGPA]

print(student)


#---------------------------
#question 4
print('question 4')
#input from user
M1=float(input('enter the marks of student 1='))
M2=float(input('enter the marks of student 2='))
M3=float(input('enter the marks of student 3='))
M4=float(input('enter the marks of student 4='))
M5=float(input('enter the marks of student 5='))


#list
Marks=[M1,M2,M3,M4,M5]
Marks.sort()
print(Marks)



#----------------------------
#question 5
print('question 5(a)')
#list of colour as given in question
color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

#part(a) is to remove the 4th element and print a new list
color.pop(3)
print(color)

print('question 5(b)')
#list of colour as given in question
color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#part(b) is to remove 'black' and 'pink' and replace them with a 'purple'
color[3:5]=['purple']
print(color)

#question 1
print('the solution of question 1 is')
input_str='Python is a case sensitive language'

#a. find the length of the input string
length=len(input_str)
print(f'(a)\t the length of the input string is :{length}')
reversed_str=input_str[::-1]
print(f'(b)\t the string in the reverse order is:{reversed_str}')
new_string=input_str[10:26]
print(f'(c)\t the new string is:{new_string}')
replaced_string=input_str.replace('a case sensitive','object oriented')
print(f'(d)\t the replaced string is : {replaced_string}')
req_index=input_str.index('a')
print(f'(e)\t the index of substring a in input string is :{req_index}')
no_white_space_str=input_str.replace(' ','')
print(f'(f)\t the input string without white spaces :{no_white_space_str}')


#question 2
print('the solution of question 2 is')
#inputs from user
name=input('enter your name:')
SID=int(input('enter your SID:'))
dept_name=input('enter your departnment name:')
cgpa=float(input('enter your cgpa:'))

print('HEY,%s Here!\n MY SID is %d\n I am from %s and my CGPA is %f'%(name,SID,dept_name,cgpa))


#question 3
print('the solution of question 3 is')
a=56
b=10
print('(a)\t a&b is :',a&b)
print('(b)\t a|b is :',a|b)
print('(c)\t a^b is :',a^b)
print('(d)\t left shift both a and b with 2 bits:a=%d,b=%d'%(a<<2,b<<2))
print('(e)\t right shift a with 2 bits and b with 4 bits:a=%d,b=%d'%(a>>2,b>>4))


#question 4
print('the solution of question 4 is')
first_num=int(input('enter first number:'))
second_num=int(input('enter second number:'))
third_num=int(input('enter third number:'))
         
if first_num >= second_num:
    if first_num >= third_num:
        print('the greatest no is ',first_num)
    else:
        print('the greatest number is ',second_num)
else:
    if second_num >= third_num:
        print('the largest number is ',second_num)
    else:
        print('the largest number is',third_num)

#question 5
        
print('the solution of question 5 is')
user_input=input('enter the string-')

if 'name' in user_input:
    print('yes')
else:
    print('no')
    


#question 6
print('the solution of question 6 is')


side_1=int(input('enter the first side of triangle-'))
side_2=int(input('enter the second side of the triangle-'))
side_3=int(input('enter the third side of the triangle-'))


if  side_1>side_2+side_3 or side_2>side_1+side_3 or side_3>side_1+side_2:
    print('no...the given input sides cannot form a triangle')
           
          
else:
    print('yes.. the given input sides can form a triangle')



#question 1
print('the solution of question 1 is:')
input_str=input('enter the string:')
x=input_str.lower()
#splitting the string
list=x.split()


letter_list=[]
word_list=[]



if len(list)==1:#if the string is a word
    for i in x:
        letter_list.append(i)

    dict1={}
    for j in letter_list:
        if j in dict1:
            dict1[j]=dict1[j]+1
        else:
            dict1[j]=1
    print(dict1)
    


else:
    for p in list:##if the string is not a single word
        word_list.append(p)

    dict2={}
    for s in word_list:
        if s in dict2:
            dict2[s]=dict[2]+1


        else:
            dict2[s]=1
    print(dict2)


#question2
print('the solution of question 2')
day=int(input('enter the day-'))
month=int(input('enter the month-'))
year=int(input('enter the year-'))


#removings the false cases
if month>12:
    condition=False
elif day>31:
    condition =False
elif day>30 and month in {2,4,6,9,11}:
    condition =False
elif day>29 and month==2:
    condition =False
elif day==29 and month==2 and year%4!=0:
    condition=False
else:
    condition =True


if condition:
    if day==31 and month==12:
        n_year=year+1
        n_month=1
    else:
        n_year=year
        n_month=month



    if month in {1,3,5,7,8,10,12}:
        if day==31:
            n_day=1
            if month!=12:
                n_month=month+1
            else:
                n_month=1
        else:
            n_day=day+1

    elif month==2:
        if year%4==0:
            if day==29:
                n_day=1
                n_month=3
            else:
                n_day=day+1
        else:
            if day==28:
                n_day=1
                n_month=3
            else:
                n_day=day+1
    else:
        if day==30:
            n_day=1
            n_month=month+1
        else:
            n_day=day+1



    print(f'next date is:{n_day}/{n_month}/{n_year}')
else:
    print('this is an invalid date')
    
    
#question 3
print('the solution of question 3')    
list1=eval(input('enter the list:'))
list2=[]
for x in list1:
    list2.append((x,x**2))
print('output is-',list2)    
    
    

#question 4
print('the solution of question 4:')
grade_table=[['A+','Outstanding',10],
             ['A','Excellent',9],
             ['B+','Very Good',8],
             ['B','Good',7],
             ['C+','Average',6],
             ['C','Below Average',5],
             ['D','Poor',4]]
grade_points=eval(input('enter the grade point given to studend:'))
if 10>=grade_points>=4:
   for x in grade_table:
    for y in x:
        if y==int(grade_points):
            print('your grade is %s and %s performance'%(x[0],x[1]))
            
else:
    print('the grade point of the student must be between 4 and 10')

            
    
#question 5
print('the solution of question 5 is-')

string='ABCDEFGHIJK'
j=0
for row in range(1,7):
    for column in range(0,row-1):
        print(' ',end='')


    x=string[0:11-j]
    print(x)
    j+=2
    

#question 6
print('the solotion of question 6 is:')
dictionary1={}
while True:
    name=input('enter the name of the student:')
    SID=int(input('enter the SID the student:'))
    dictionary1[SID]=name
    while True:
        more_details=input('do you want to enter more deatils press Y/N ')
        if more_details==('Y'):
            more_details=1
            break
        elif more_details==('N'):
            more_details=0
            break
        else:
            print('enter only Y/N')
            continue
    if more_details==0:
        break
    
print('a:the students details are-')
for x in dictionary1:
    print(f'the SID of %s is %d:'%(dictionary1[x],x))
print('b:sorting  details using student names')
dictionary2={}
for sorted_value in sorted(dictionary1.values()):
    for key,value in dictionary1.items():
        if value==sorted_value:
            dictionary2[key]=value
for x in dictionary2:
    print('the SID of %s is %d :'%(dictionary2[x],x))
print('c:sorting details using SID:')    
dictionary3={}
for sorted_key in sorted(dictionary1.keys()):
    for key,value in dictionary1.items():
        if key==sorted_key:
            dictionary3[key]=value
for x in dictionary3:
    print('the SID of %s is %d :'%(dictionary3[x],x))
print('d: search a student details with SID anf print name:')
while True:
    search_sid=int(input('enter the SID of student whose details you want to search:'))
    if search_sid in dictionary1:
        print('the name of the student whose SID is %d is %s'%(search_sid,dictionary1[search_sid]))
        break
    else:
        print('the SID you entered is invalid:')
        continue




#quetion 7
print('the solution of question 7 is-')
x=0  #first no of fibonacci series
y=1   #second no of fibonacci series
sum=0  #sum of fibonacci series
while True:
    num=int(input('the no of terms in the fibonacci series:'))
    if num<0:
        print('the no of terms must be positive')
        continue    
    if num==0:
        print('as the no of terms is 0 so average of fibonaaci series =0')
        break
    else:
        print('the fibonacci series is:')
        print(x,end=' ')
        for i in range(1,num):
            sum+=y
            print(y,end=' ')
            z=x+y
            x=y
            y=z
        print('the average of the %d terms of the fibonacci series is %0.3f'%(num,sum/num))
        break
        
        
    
#question 8
print('the solution of question 8')
set1={1,2,3,4,5}
set2={2,4,6,8}
set3={1,5,9,13,17}
print('a:a new set of all elements that are in set1 and set2 but not both-')
set4=set1^set2
print(set4)
print('b:set of elements that are only in one of three sets set1,set2 and set3')
set5=set1^set2^set3
print(set5)
print('c:set of elements that are in exactly two of sets')
set6=(set1|set2|set3)-(set1^set2^set3)-(set1&set2&set3)
print(set6)
print('d:set of integers in the range 1 to 10 that are not in set1')
set7=set(range(1,11))-set1

print(set7)
print('e:the set of all integers in the range 1 to 10 that are not in set1 ,set2 and set3')
set8=set(range(1,11))-(set1|set2|set3)
print(set8)
      
        
    

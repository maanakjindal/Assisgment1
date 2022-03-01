
# ## defining the function :
print('question1')
def tower_of_harnoi(n,source,destination,auxillary): 
    if n==1 :
        print('Move disk 1 from source',source,'to destination',destination)
        return 
    tower_of_harnoi(n-1,source,auxillary,destination) 
    print('move disk',n,'from source',source,'to destination',destination)
    tower_of_harnoi(n-1,auxillary,destination,source)

# ## taking no. of disk as a input 
n=int(input('Enter the no. of disk :'))
tower_of_harnoi(n,'S','D','A')   

print()

## defining factorial recursive function
print('question2')
def pascal_triangle(n):
    def factorial(n) :
        if n==0 :
           return 1
        else :
           return n*factorial(n-1)
    for i in range(n+1):
        c=int(factorial(n)/(factorial(i)*factorial(n-i)))
        print(c,end=' ')


        
## Printing pascal triangle with factorial recursion :
no_rows=int(input(('enter the no. of rows for passcal triangle :')))
print('with recursion \n')
if no_rows>0 :
    for i in range(no_rows) :  
        for c in range(i,no_rows-1):
            print(' ',end='')
        pascal_triangle(i)
        print()
    print()
## Printing without recursion 
    print('Without recursion \n')

    for i in range(no_rows) :  
            for c in range(i,no_rows-1):
                print(' ',end='')
            for j in range(i+1):
                a,b,d=1,1,1
                for k in range(i+1):
                    if k>0:       ## calculating the factorials by help of for loops 
                        a=a*k
                        if k<=j:
                            b=b*k
                        if k<=i-j:
                            d=d*k
                print(int(a/(b*d)),end=' ')
            print()
      
else :
    print('invalid input')


print('question3')
a=int(input('enter first no. :'))  
b=int(input('enter secod no. :'))
if b==0 :
    print('Denominator cant be 0 , error')
else :
    result=divmod(a,b)    
    print(result)
    print('\nPart a)')
    print(callable(divmod))   

    print('\nPart b)')
    if result[0] == 0 :   
        if result[1] == 0 :
            print('both values are zero ')
    else :
       if result[1] == 0 :
            print('one value is zero')
       else :
            print('both values are non zero')    
    
    print('\nPart c)')
    lis=[result[0],result[1],4,5,6]   
    print(lis)
    set1=set()
    for i in lis :
        if i > 4 :
            print(i,end=' ')
            set1.add(i)   
    print()


    print('\nPart d)')
    print(set1)

    print('\nPart e)')
    fr_set=frozenset(set1)  
    print('the immutable set is :',fr_set)

    print('\nPart f)')
    b=max(set1)
    print('max value :',b)    
    print('Hash value :',hash(b))


print('question4')

class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no

    def __del__(self):
        print('record of',self.name,'is destroyed')



name=input('enter the name of the student:')
roll_no=int(input('enter the roll no the student:'))
student1=Student(name,roll_no)

print(f'the roll no of the student {student1.name} is {student1.roll_no}')


del student1

print('question5')
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
    def __del__(self):
      print('the record of ',self.name ,'is destroyed')
        
employee1=Employee('mehak',40000)
employee2=Employee('ashok',50000)
employee3=Employee('viren',60000)


print('the salary of %s is %d'%(employee1.name,employee1.salary))
print('the salary of %s is %d'%(employee2.name,employee2.salary))
print('the salary of %s is %d'%(employee3.name,employee3.salary))


print('part a')
employee1.salary=70000
print('the updated salary of %s is %d'%(employee1.name,employee1.salary))



print('part b')
del employee3

print('question6')

def anagrams(s):
    if s=='':
        return [s]
    else:
        word=[]
        for i in anagrams(s[1:]):
            for p in range(len(i)+1):
                word.append(i[:p]+s[0]+i[p:])
                
        return word


word1=input('give a word to your friend:')


word2=input('make a meaningfull word with same letters as given by your friend:')

    

if word2 in anagrams(word1):
    x=input('is the word2 entered by the 2nd friend is meaningfull ? give answer in (y/n)')
    if x=='y':
        print('the test is passed and the friendship is true')
    elif x=='n':
        print('the test is failed and the friendship is fake')
        
    else:
        print('please give the input in (y/n)')


else:
    print('word not contain the same letters so friendship is fake')
    

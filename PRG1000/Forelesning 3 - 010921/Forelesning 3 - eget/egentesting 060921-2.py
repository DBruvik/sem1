#This program determines whether a bank customer
#qualifies for a loan.

MINSALARY=30000.0
MINYEARS=2

#The minimun annual salar and years on the job

#Get the customer's annual salary
salary=float(input('Enter your annual salary: ' ))

#Get the number of years on the current job
yearsOnJob=int(input('Enter the number of years employed: '))

#Determine whether the customer qualifies.
if salary>=MINSALARY:
    if yearsOnJob>=MINYEARS:
        print('You qualify for the loan.')
    else:
        print('You must have been emplyed for atleast', MINYEARS, ' to qualify.')
else:
    print('You must earn at least $', MINSALARY, ' per year to qualify')

# File: stadiumSeating.py
# 
# Purpose: Calculates the total income generated for a stadium
#          based upon the number of tickets sold.  Different
#          class tickets can be sold with different prices.
#          Calculate each income for each class ticket as 
#          well as the overall income and print out these
#          statistics.
#
# Programmer: CHASE

# declare global constants to be used in program
CLASS_A_SEATS = 20.00
CLASS_B_SEATS = 15.00
CLASS_C_SEATS = 10.00


def main():
    # prompt the user to enter the amount of 
    # A seats, then read it in
    countAseats = int(input('Enter a count of A seats: '))
    # prompt the user to enter the amount of 
    # B seats, then read it in
    countBseats = int(input('Enter a count of B seats: '))
    # prompt the user to enter the amount of 
    # C seats, then read it in
    countCseats = int(input('Enter a count of C seats: '))
    # calculate the A income
    incomeAseats = countAseats * CLASS_A_SEATS
    # calculate the B income
    incomeBseats = countBseats * CLASS_B_SEATS
    # calculate the C income
    incomeCseats = countCseats * CLASS_C_SEATS

    # call function calcIncome() to sum up the total
    # income for all tickets
    total = calcIncome(incomeAseats, incomeBseats,
                       incomeCseats)
    # call function displayIncome() to print out statistics
    displayIncome(incomeAseats, incomeBseats,
                  incomeCseats, total)
    # call function goodBye() to end program    
    goodBye()
# end function main

def goodBye():
    print('\nThis program was written by chase cantrell' + 
          '\nEnd of program')
# end function goodBye

def displayIncome(incomeA, incomeB, incomeC, totalIncome):
    print('\nIncome from class A seats is $',
          format(incomeA, ',.2f'))
    print('Income from class B seats is $: ',
          format(incomeB, ',.2f'))
    print('Income from class C seats is $: ',
          format(incomeA, ',.2f'))
    print('\nTotal income for stadium is $: ',
          format(totalIncome, ',.2f'))
# end function displayIncome

def calcIncome(incomeA, incomeB, incomeC):
    totalIncome = incomeA + incomeB + incomeC
    return totalIncome
# end function calcIncome

# call/invoke the function main()
main()


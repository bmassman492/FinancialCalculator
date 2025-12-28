#use python library tkinter to create a popup that prompts user inputs and then references other Utils

import extraPaymentCalculationUtils as extra
import oneTimeCalculationUtils as one


print("Debt/Investment Calculator . . .")

going = 1

while (going == 1):

    selection = input("Calculate for a one time payment (Enter 1) or for recurring payments (Enter 2): ")
    going = 0

    if selection == 1:
        one.InvestmentReturnRate = input("Enter the expected return rate on your investments as a decimal (e.g. .08): ")
        one.LoanAmount = input("Enter the loan amount in dollars (that is subject to interest): ")
        one.DownPayment = input("Enter the amount that you are considering putting down on the loan immediately or investing in the stock market immediately: ")
        one.LoanInterestRate = input("Enter the loan's interest rate as a decimal (e.g. .031): ")
        one.LoanLength = input("Enter the length of the loan in years: ")
        one.PeriodsPerYear = input("Enter the number of periods per year for the loan: ")

        print("The net benefit of investing the down payment rather than putting it towards the loan is $" + one.InvestBenefit)
        if (one.InvestBenefit > 0):
            print("It is financially wise to invest the down payment immediately")
        else:
            print("It is financially wise to put the down payment towards the loan")
    elif selection == 2:
        extra.InvestmentReturnRate = input("Enter the expected return rate on your investments as a decimal (e.g. .08): ")
        extra.LoanAmount = input("Enter the loan amount in dollars (that is subject to interest): ")
        extra.ExtraPayOrInvestPerPeriod = input("How much do you plan to put towards the loan or invest each period? Enter here: ")
        extra.LoanInterestRate = input("Enter the loan's interest rate as a decimal (e.g. .031): ")
        extra.LoanLength = input("Enter the length of the loan in years: ")
        extra.PeriodsPerYear = input("Enter the number of periods per year for the loan: ")

        print("The net benefit of investing the regular payments rather than putting them towards the loan is $" + extra.InvestBenefit)
        if (extra.InvestBenefit > 0):
            print("It is financially wise to invest regular payments")
        else:
            print("It is financially wise to put the regular payments towards the loan")
    else:
        going = 1
        print("The number you entered is not a 1 or a 2. Please enter one of those options. ")
#use python library tkinter to create a popup that prompts user inputs and then references other Utils

import extraPaymentCalculationUtils as extra
import oneTimeCalculationUtils as one


print("Debt/Investment Calculator . . .")

going = 1

while (going == 1):

    selection = input("Calculate for a one time payment (Enter 1) or for recurring payments (Enter 2): ")
    going = 0

    if selection == "1":
        one.InvestmentReturnRate = float(input("Enter the expected return rate on your investments as a decimal (e.g. .08): "))
        one.LoanAmount = float(input("Enter the loan amount in dollars (that is subject to interest): "))
        one.DownPayment = float(input("Enter the amount that you are considering putting down on the loan immediately or investing in the stock market immediately: "))
        one.LoanInterestRate = float(input("Enter the loan's interest rate as a decimal (e.g. .031): "))
        one.LoanLength = float(input("Enter the length of the loan in years: "))
        one.PeriodsPerYear = int(input("Enter the number of periods per year for the loan: "))

        one.calculate_invest_benefit()
        print(f"The net benefit of investing the down payment rather than putting it towards the loan is ${one.InvestBenefit:.2f}")
        if (one.InvestBenefit > 0):
            print("It is financially wise to invest the down payment immediately")
        else:
            print("It is financially wise to put the down payment towards the loan")
    elif selection == "2":
        extra.InvestmentReturnRate = float(input("Enter the expected return rate on your investments as a decimal (e.g. .08): "))
        extra.LoanAmount = float(input("Enter the loan amount in dollars (that is subject to interest): "))
        extra.ExtraPayOrInvestPerPeriod = float(input("How much do you plan to put towards the loan or invest each period? Enter here: "))
        extra.LoanInterestRate = float(input("Enter the loan's interest rate as a decimal (e.g. .031): "))
        extra.LoanLength = float(input("Enter the length of the loan in years: "))
        extra.PeriodsPerYear = int(input("Enter the number of periods per year for the loan: "))

        extra.calculate_invest_benefit()
        print(f"The net benefit of investing the regular payments rather than putting them towards the loan is ${extra.InvestBenefit:.2f}")
        if (extra.InvestBenefit > 0):
            print("It is financially wise to invest regular payments")
        else:
            print("It is financially wise to put the regular payments towards the loan")
    else:
        going = 1
        print("The number you entered is not a 1 or a 2. Please enter one of those options. ")
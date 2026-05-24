# import libraries
import numpy as np
import numpy_financial as npf

InvestmentReturnRate = .08
# This is the percentage rate of return you expect to earn from your investments. 
# I recommend around 8% as that's slightly lower than the long-term average growth rate of the S&P500.

LoanAmount = 460000
# This is the total amount of the loan that is subject to interest.

DownPayment = 45000
# This is the amount that you are considering putting down on the loan immediately OR investing into the stock market immediately.

LoanInterestRate = .031
# This is the loan's interest rate. 

LoanLength = 30
# This is the length of the loan, in years. 
# If your loan has a partial year you will have to enter the years as a decimal. 
# For example, a 50 month loan would be entered as 50/12 = 4.16.

PeriodsPerYear = 12
# This is the number of payments you'll pay on the loan each year. Most loans are paid monthly. 
# A monthly payment would enter 12 into this box. If you only pay quarterly, you would put 4 into this box.

def calculate_invest_benefit():
    global InvestBenefit, InvestmentLengthYears, PrincipalInvested, TotalInvestmentAccountValue, InvestmentGain, Payment1, TotalInterestOnLoan1, Payment2, TotalInterestOnLoan2
    InvestmentLengthYears = LoanLength
    # This is the number of years the investment grows. In this case it is equal to the loan length for an accurate comparison.

    PrincipalInvested = DownPayment
    # This is the amount you choose to put in the stock market, rather than put towards your loan in a down payment.

    TotalInvestmentAccountValue = PrincipalInvested*np.exp(InvestmentReturnRate*InvestmentLengthYears)
    # This is the value of the principal investment plus the growth of the Investments

    InvestmentGain = TotalInvestmentAccountValue - PrincipalInvested
    # This is your total investment account value which is the amount of money your investments have made you plus the originally invested principal amount added together. 

    #Variables for Total interest on loan with down payment not used to reduce the loan amount
    Payment1 = npf.pmt(LoanInterestRate/PeriodsPerYear, LoanLength*PeriodsPerYear, LoanAmount*-1)
    TotalInterestOnLoan1 = LoanLength*PeriodsPerYear*Payment1 - LoanAmount

    #Variables for Total interest on loan with down payment used to reduce the loan amount
    Payment2 = npf.pmt(LoanInterestRate/PeriodsPerYear, LoanLength*PeriodsPerYear, (LoanAmount-DownPayment)*-1)
    TotalInterestOnLoan2 = LoanLength*PeriodsPerYear*Payment2 - (LoanAmount-DownPayment)

    InvestBenefit = (TotalInvestmentAccountValue-(npf.fv(InvestmentReturnRate/PeriodsPerYear, LoanLength*PeriodsPerYear, (Payment1-Payment2)*-1, pv=0)) - (TotalInterestOnLoan1-TotalInterestOnLoan2))

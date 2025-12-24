import numpy as np
import numpy_financial as npf

InvestmentReturnRate = .08
LoanAmount = 460000
ExtraPayOrInvestPerPeriod = 400
LoanInterestRate = .031
LoanLength = 30
PeriodsPerYear = 12

TotalAmountInvested = ExtraPayOrInvestPerPeriod*LoanLength*PeriodsPerYear
TotalInvestmentAccountValue = npf.fv(InvestmentReturnRate/PeriodsPerYear, LoanLength*PeriodsPerYear, ExtraPayOrInvestPerPeriod*-1, pv=0)
InvestmentGain = TotalInvestmentAccountValue-TotalAmountInvested

#Calculations for Total interest on loan with extra money invested from the start
Payment1 = npf.pmt(LoanInterestRate/PeriodsPerYear, LoanLength*PeriodsPerYear, LoanAmount*-1)
TotalInterestOnLoan1 = LoanLength*PeriodsPerYear*Payment1 - LoanAmount

#Calculations for Total interest on loan with extra money put towards the loan from the start
Payment2 = Payment1 + ExtraPayOrInvestPerPeriod
TotalInterestOnLoan2 = npf.nper(LoanInterestRate/PeriodsPerYear, Payment2, LoanAmount*-1) * Payment2 - LoanAmount
#note that this uses a simpler method to sum the interest payments than what is used in the speadsheet, but it provides a similar result that is typically within $1 of the spreadsheet's result 

#For Investment Account Value Investing Monthly Payment After Loan is Paid Off
InvestmentLengthYrs = LoanLength - npf.nper(LoanInterestRate/PeriodsPerYear, Payment2, LoanAmount*-1, 0)/12
TotalInvestmentAccountValue2 = npf.fv(InvestmentReturnRate/PeriodsPerYear, InvestmentLengthYrs*PeriodsPerYear, Payment2*-1, pv=0)

InvestBenefit = TotalInvestmentAccountValue - (TotalInterestOnLoan1-TotalInterestOnLoan2) - TotalInvestmentAccountValue2
print(InvestBenefit)
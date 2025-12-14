# This file will convert all of the excel functions from the google sheets debt/investments calculator into usable python code for the widget

# DEFINE USER INPUT VARIABLES:
    # One time payment calculation variables (OT):

OTInvestmentReturnRate = .08
# This is the percentage rate of return you expect to earn from your investments. 
# I recommend around 8% as that's slightly lower than the long-term average growth rate of the S&P500.

OTLoanAmount = 460,000
# This is the total amount of the loan that is subject to interest.

OTDownPayment = 45,000
# This is the amount that you are considering putting down on the loan immediately OR investing into the stock market immediately.

OTLoanInterestRate = .031
# This is the loan's interest rate. 

OTLoanLength = 30
# This is the length of the loan, in years. 
# If your loan has a partial year you will have to enter the years as a decimal. 
# For example, a 50 month loan would be entered as 50/12 = 4.16.

OTPeriodsPerYear = 12
# This is the number of payments you'll pay on the loan each year. Most loans are paid monthly. 
# A monthly payment would enter 12 into this box. If you only pay quarterly, you would put 4 into this box.

OTNumYearsFuture = 30
# The number of years into the future you want to see the different investment account values at!

   
    # Paying extra each period calculation variables (RE):

        #PLACEHOLDER, DO THESE LATER


#DEFINE FUNCTIONS FOR ONE TIME PAYMENT CALCULATOR


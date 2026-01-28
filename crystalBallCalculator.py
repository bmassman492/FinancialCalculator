import numpy as np
import statistics

print("\nDebt vs. Investing calculator . . .")
print("This program aims to determine the likelihood and amount that investing money rather than using it to pay off debt will pay off.")
print("Please fill in the appropriate information relating to the investment.\n")

version = ""

while version not in ("1", "2"):
    version = input("Calculate for a one time payment (Enter 1) or for recurring payments (Enter 2): ")

loanAmount = float(input("Enter the loan amount, e.g. 400000: "))
loanLengthYrs = int(input("Enter the loan length in years e.g. 30: "))
loanIntRate = float(input("Enter the loan interest rate as a decimal e.g. .031: "))

periodsPerYear = 12

if version == 1:
    downPayment = float(input("Enter the down payment amount that you are considering putting towards the loan vs investing e.g. 40000: "))
if version == 2:
    extraPayOrInvest = float(input("Enter the amount that you would pay off or invest each period (there are " + periodsPerYear + " periods in a year: "))

meanYearlyReturn = float(input("Enter the average yearly return that you anticipate from your investments. The average for large cap growth stocks is .122. If you are taking a safer or more aggressive approach, feel free to enter more or less. It is suggested you enter a lower amount to be safe. "))
print("\nSelect the type of investments you plan on using:")
print("1. Large Cap Stocks")
print("2. Small Cap Stocks")
print("3. Long Term Corporate Bonds")
print("4. Long Term Government Bonds")
print("5. Intermediate Term Government Bonds")
print("6. U.S. Treasury Bills")

choice = input("\nEnter the number corresponding with your investment type (1-6): ")

investment_options = {
    "1": "Large Cap Stocks",
    "2": "Small Cap Stocks",
    "3": "Long Term Corporate Bonds",
    "4": "Long Term Government Bonds",
    "5": "Intermediate Term Government Bonds",
    "6": "U.S. Treasury Bills"
}

investmentType = investment_options.get(choice, "Invalid selection")

returnStandardDeviation = 0

if investmentType == "Large Cap Stocks":
    returnStandardDeviation = .197
elif investmentType == "Small Cap Stocks":
    returnStandardDeviation = .31
elif investmentType == "Long Term Corporate Bonds":
    returnStandardDeviation = .084
elif investmentType == "Long Term Government Bonds":
    returnStandardDeviation = .102
elif investmentType == "Intermediate Term Government Bonds":
    returnStandardDeviation = .055
elif investmentType == "U.S. Treasury Bills":
    returnStandardDeviation = .031

def createReturnsArray(loanLengthYrs, meanYearlyReturn, returnStandardDeviation):
    returnsArray = []

    for i in range(loanLengthYrs):
        z = np.random.normal(0, 1)
        returnsArray.append(round(meanYearlyReturn + z*returnStandardDeviation, 3))
    
    return returnsArray




